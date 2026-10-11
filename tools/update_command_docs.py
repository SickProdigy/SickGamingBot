#!/usr/bin/env python3
"""Regenerate SickGamingBot command catalogs from an AdvancedHelp docsreport."""

import argparse
import json
import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path


MODULES = {
    "Admin": ("admin", "Administration", "Community and server management"),
    "AdvancedHelp": ("advancedhelp", "Advanced Help", "Getting started and bot controls"),
    "Alias": ("alias", "Aliases", "Community and server management"),
    "Ark": ("ark", "ARK", "Games and gaming communities"),
    "Audio": ("audio", "Audio", "Music, media, and feeds"),
    "Avatar": ("avatar", "Avatar", "Economy, information, and utilities"),
    "Cleanup": ("cleanup", "Cleanup", "Moderation and safety"),
    "Coc": ("coc", "Clash of Clans", "Games and gaming communities"),
    "CogManagerUI": ("cogmanagerui", "Cog Manager", "Bot administration"),
    "Core": ("core", "Core", "Getting started and bot controls"),
    "CustomCommands": ("customcom", "Custom Commands", "Community and server management"),
    "DayZ": ("dayz", "DayZ", "Games and gaming communities"),
    "Dictionary": ("dictionary", "Dictionary", "Economy, information, and utilities"),
    "Downloader": ("downloader", "Downloader", "Bot administration"),
    "Economy": ("economy", "Economy", "Economy, information, and utilities"),
    "Filter": ("filter", "Filter", "Moderation and safety"),
    "GMod": ("gmod", "Garry's Mod", "Games and gaming communities"),
    "GameRoles": ("gameroles", "Game Roles", "Community and server management"),
    "General": ("general", "General", "Economy, information, and utilities"),
    "Giveaways": ("giveaways", "Giveaways", "Community and server management"),
    "Icarus": ("icarus", "Icarus", "Games and gaming communities"),
    "Image": ("image", "Image", "Music, media, and feeds"),
    "Meme": ("meme", "Meme", "Music, media, and feeds"),
    "Mod": ("mod", "Moderation", "Moderation and safety"),
    "ModLog": ("modlog", "Moderation Log", "Moderation and safety"),
    "MovieReleases": ("movies", "Movie Releases", "Music, media, and feeds"),
    "Mutes": ("mutes", "Mutes", "Moderation and safety"),
    "Navidrome": ("navidrome", "Navidrome", "Music, media, and feeds"),
    "Nsfw": ("nsfw", "NSFW", "NSFW"),
    "Permissions": ("permissions", "Permissions", "Moderation and safety"),
    "Pokemon": ("pokemon", "Pokémon", "Games and gaming communities"),
    "Reports": ("reports", "Reports", "Moderation and safety"),
    "RocketLeague": ("rocketleague", "Rocket League", "Games and gaming communities"),
    "RoleTools": ("roletools", "Role Tools", "Community and server management"),
    "RSS": ("rsspublisher", "RSS Publisher", "Music, media, and feeds"),
    "RuneScape": ("runescape", "RuneScape", "Games and gaming communities"),
    "Streams": ("streams", "Streams", "Music, media, and feeds"),
    "Trivia": ("trivia", "Trivia", "Games and gaming communities"),
    "Warnings": ("warnings", "Warnings", "Moderation and safety"),
    "Welcome": ("welcome", "Welcome", "Community and server management"),
    "Wolfram": ("wolfram", "Wolfram", "Economy, information, and utilities"),
}

MERGED_MODULES = {"Memeify": "Meme", "Other": "Core"}
SECTION_ORDER = (
    "Getting started and bot controls",
    "Community and server management",
    "Moderation and safety",
    "Music, media, and feeds",
    "Games and gaming communities",
    "Economy, information, and utilities",
    "NSFW",
    "Bot administration",
)
AUDIENCES = {
    "member": ("members", "Member commands", "Member"),
    "staff": ("staff", "Staff commands", "Staff"),
    "server_owner": ("server-owners", "Server-owner commands", "Server owner"),
    "bot_owner": ("maintainers", "Bot-maintainer commands", "Bot maintainer"),
}


def normalized_module(record):
    return MERGED_MODULES.get(record["module"], record["module"])


def table_text(records, access_heading="Access"):
    lines = [
        f"| Command | Aliases | {access_heading} | Description |",
        "| --- | --- | --- | --- |",
    ]
    for record in sorted(records, key=lambda item: item["path"].casefold()):
        aliases = ", ".join(f"`{escape(value)}`" for value in record["aliases"]) or "—"
        lines.append(
            f"| `-{escape(record['path'])}` | {aliases} | "
            f"{escape(record['declared_access']['label'])} | "
            f"{escape(record['description']) or 'No short description is declared.'} |"
        )
    return "\n".join(lines)


def escape(value):
    return str(value).replace("\\", "\\\\").replace("|", "\\|").replace("\n", " ").strip()


def reference_page(title, package, records):
    return f"""# {title} commands

Loaded package: `{package}`

## Reading this reference

Each command is shown as its complete path. To see detailed help, put that path after
`-help` without repeating the leading hyphen:

```text
-help <command>
-help <command> <subcommand>
-help <command> <subcommand> <nested-subcommand>
```

The access column comes from the command checks declared by the running bot. Live
permissions, disabled commands, parent checks, role hierarchy, and server rules can
further restrict availability. See [Using SickGamingBot help](../using-help.md).

{table_text(records)}

Live `-help` output remains authoritative for syntax, enabled state, hidden commands,
arguments, cooldowns, and server-specific access.
"""


def audience_intro(key, title, count):
    descriptions = {
        "member": "These are ordinary member and self-service command paths. Staff and server owners also retain commands available to them through the live permission system.",
        "staff": "These command paths declare moderator, administrator, or specific Discord permission requirements. Delegated managers may receive narrower access.",
        "server_owner": "These command paths declare Discord server ownership as their primary boundary. Server owners also use member and staff commands allowed by the live permission system.",
        "bot_owner": "These command paths control the hosted bot, global configuration, installed code, or cross-server behavior. Discord server ownership does not grant this tier.",
    }
    return f"""# {title}

{descriptions[key]}

Use live help for current syntax and checks:

```text
-help <command>
-help <command> <subcommand>
-help <command> <subcommand> <nested-subcommand>
```

The catalog is generated from the sanitized production command inventory. Server
rules, role hierarchy, disabled commands, channel permissions, and module configuration
can further restrict availability. [Learn how to use command help](../using-help.md).

## Catalog ({count} command paths)
"""


def build_reference_index(data, grouped):
    generated = datetime.fromisoformat(data["generated_at"]).date().isoformat()
    sections = defaultdict(list)
    for module, records in grouped.items():
        slug, title, section = MODULES[module]
        sections[section].append((title, slug, len(records)))
    lines = [
        "# Complete command reference",
        "",
        "## Reference baseline",
        "",
        f"- **Generated from production:** {generated}",
        "- **Bot:** Official SickGamingBot instance",
        f"- **Runtime:** Red {data['red_version']} with the `{data['prefix']}` prefix",
        f"- **Scope:** {len(data['loaded_cogs'])} loaded cogs and {data['command_count']:,} command paths",
        f"- **Inventory schema:** {data['schema_version']} from AdvancedHelp {data['advancedhelp_version']}",
        "",
        "## How to use this reference",
        "",
        "Open a module below, then put its complete command path after `-help`:",
        "",
        "```text",
        "-help pokemon",
        "-help pokemon party",
        "-help warningset mywarnings sendtodms",
        "```",
        "",
        "The report records declared metadata from the running bot. Live `-help` remains",
        "authoritative for visibility, syntax, disabled state, permissions, and server rules.",
    ]
    for section in SECTION_ORDER:
        lines.extend(["", f"## {section}", ""])
        for title, slug, count in sorted(sections[section]):
            noun = "command" if count == 1 else "commands and subcommands"
            lines.append(f"- [{title}]({slug}.md) — {count} {noun}")
    lines.append("")
    return "\n".join(lines)


def update_module_counts(root, grouped):
    for module, records in grouped.items():
        slug = MODULES[module][0]
        path = root / "docs" / "modules" / f"{slug}.md"
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        text = re.sub(
            r"- \*\*Documented commands:\*\* \d+ commands? and subcommands?",
            f"- **Documented commands:** {len(records)} commands and subcommands",
            text,
        )
        path.write_text(text, encoding="utf-8")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("inventory", type=Path, help="JSON file returned by -docsreport")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    data = json.loads(args.inventory.read_text(encoding="utf-8"))
    if data.get("schema_version") != 1 or data.get("prefix") != "-":
        raise SystemExit("Unsupported inventory schema or SickGamingBot prefix")
    if data.get("command_count") != len(data.get("commands", [])):
        raise SystemExit("Inventory command_count does not match commands array")

    grouped = defaultdict(list)
    for record in data["commands"]:
        module = normalized_module(record)
        if module not in MODULES:
            raise SystemExit(f"Add module metadata for {module!r}")
        grouped[module].append(record)

    reference_dir = args.root / "docs" / "reference"
    for module, records in grouped.items():
        slug, title, _section = MODULES[module]
        packages = sorted({item["module"] for item in records})
        package = "` + `".join(packages)
        (reference_dir / f"{slug}.md").write_text(
            reference_page(title, package, records), encoding="utf-8"
        )
    (reference_dir / "index.md").write_text(
        build_reference_index(data, grouped), encoding="utf-8"
    )

    for key, (slug, title, _label) in AUDIENCES.items():
        records = [item for item in data["commands"] if item["audience"] == key]
        by_module = defaultdict(list)
        for record in records:
            by_module[normalized_module(record)].append(record)
        lines = [audience_intro(key, title, len(records)).rstrip()]
        for module in sorted(by_module, key=lambda value: MODULES[value][1]):
            module_slug, module_title, _section = MODULES[module]
            module_records = by_module[module]
            lines.extend(
                [
                    "",
                    f"### [{module_title}](../modules/{module_slug}.md) ({len(module_records)})",
                    "",
                    table_text(module_records, "Declared access"),
                ]
            )
        lines.append("")
        (args.root / "docs" / "commands" / f"{slug}.md").write_text(
            "\n".join(lines), encoding="utf-8"
        )

    update_module_counts(args.root, grouped)
    print(
        f"Generated {len(grouped)} references and 4 audience catalogs "
        f"for {data['command_count']} command paths."
    )


if __name__ == "__main__":
    main()
