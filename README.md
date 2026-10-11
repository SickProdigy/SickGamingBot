# SickGamingBot

SickGamingBot is a community Discord bot that brings moderation, member tools,
games, media, roles, alerts, and server integrations together in one place. Each
Discord server can enable different features and decide who may use or manage them.

## Add SickGamingBot to your server

[Invite SickGamingBot](https://discord.com/oauth2/authorize?client_id=691452746632658954&scope=bot&permissions=0)
using the same authorization link returned by the `-invite` command.

## New to the bot?

Start by asking the bot for help. SickGamingBot commands use the `-` prefix:

```text
-help
-help <command>
-help <command> <subcommand>
```

The first command shows what is available to your account. The second explains a
command group, while the third focuses on a specific subcommand. See
[Using SickGamingBot help](docs/using-help.md) or [Getting started](docs/getting-started.md)
for the full introduction.

## What can SickGamingBot do?

Depending on what a server enables, SickGamingBot can provide:

- Moderation tools for warnings, mutes, bans, message cleanup, reports, and case history.
- Self-service roles, game-role profiles, welcome messages, and giveaways.
- Music playback, memes, movie discovery, stream status, and stream alerts.
- Profiles, activity levels, economy features, trivia, and general utilities.
- Game and community integrations for ARK, Clash of Clans, DayZ, Garry's Mod,
  Icarus, Rocket League, RuneScape, and more.
- Wolfram, Navidrome, RSS, and other connected services.

Browse the [features overview](docs/features/index.md), open the full
[module catalog](docs/modules/index.md), or go directly to the
[command guides](docs/commands/index.md). Live help is always the authority for what
is currently loaded, enabled, and available in a particular server.

## Choose your guide

| I am a… | Start here | What you will find |
| --- | --- | --- |
| Member | [Member guide](docs/members/index.md) | Everyday commands, self-service features, and account connections |
| Moderator or administrator | [Moderator and administrator guide](docs/staff/index.md) | Moderation workflows and server configuration |
| Discord server owner | [Server-owner guide](docs/server-owners/index.md) | Initial setup, integrations, and guild policy |
| SickGamingBot maintainer | [Bot-maintainer commands](docs/commands/maintainers.md) | Global configuration, code, and host-wide operations |

## How access levels work

- **Member** — uses everyday commands and manages their own account connections.
- **Moderator** — handles day-to-day community moderation when granted access by the server.
- **Administrator** — configures sensitive, server-wide settings and optional features.
- **Server Owner** — makes guild-level decisions about setup, access, integrations, and policy.
- **SickGaming Maintainer** — hosts the bot and manages its code, process, and global services.

These levels describe responsibility; they do not override Discord permissions or the
bot's checks. A server may also delegate one feature to a manager role without making
that person a full administrator.

A Discord server owner is not the bot host. Loading cogs, changing global credentials,
restarting the bot, and other host operations are maintainer-only. Read
[Permissions](docs/permissions.md) for the complete distinction.

## Help and reference

- [Command and documentation status](docs/command-status.md)
- [Using SickGamingBot help](docs/using-help.md)
- [Audience command catalogs](docs/commands/index.md)
- [Complete command reference](docs/reference/index.md)
- [Module catalog](docs/modules/index.md)
- [Privacy and data](docs/privacy-and-data.md)
- [Troubleshooting](docs/troubleshooting.md)
- [Legacy command snapshots](docs/legacy-command-lists.md)

This repository documents the public bot experience. Cog source and development
information live in the [Sick-Cogs repository](/SickProdigy/Sick-Cogs).
