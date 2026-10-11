# Contributing to SickGamingBot public documentation

Thanks for helping improve the public SickGamingBot documentation. This repository
explains the bot for members, Discord staff, server owners, and SickGamingBot
maintainers. Cog implementation belongs in the
[Sick-Cogs repository](/sickprodigy/Sick-Cogs).

## Before opening a change

- Search existing issues and documentation first.
- Confirm behavior with live `-help`, `-help <command>`, or
  `-help <command> <subcommand>` when possible.
- Use the official SickGamingBot runtime as the availability baseline. A cog present in
  source is not publicly available until it is loaded on the official bot.
- Report implementation bugs and new cog development in Sick-Cogs. Use this repository
  for inaccurate, missing, unclear, or poorly organized public documentation.

## How to contribute

1. Fork the repository and clone your fork.
2. Create a focused branch:

   ```bash
   git checkout -b docs/your-change
   ```

3. Make the smallest complete documentation change.
4. Update every affected navigation, audience, module, feature, and reference page.
5. Check relative links and Markdown formatting.
6. Commit with a clear message and reference the related issue.
7. Push the branch and open a pull request.

## Documentation rules

- SickGamingBot uses `-` as its documented prefix. Do not use a variable prefix
  placeholder in user-facing pages.
- Keep Member, Staff/Administrator, Server Owner, and Bot Maintainer capabilities
  clearly separated.
- A Discord server owner is not the Red bot owner.
- Live Discord permissions, Red checks, disabled commands, role hierarchy, and server
  rules remain authoritative.
- Use complete command paths when documenting subcommands.
- Explain workflows and decisions instead of publishing unexplained command dumps.
- Keep archived command lists historical; do not treat them as current sources.

## Privacy and public-repository safety

Never commit or include in an issue:

- API keys, passwords, tokens, private keys, or recovery codes;
- private server addresses, SSH details, filesystem paths, or internal endpoints;
- Discord user, guild, channel, message, or role IDs unless they are intentionally
  public and essential;
- private-channel content, moderation evidence, or unnecessary personal information;
- live bot configuration or credential files.

Sanitize screenshots, logs, and error messages before attaching them.

## Command and module changes

When an officially loaded command or cog changes, review all affected areas:

- `docs/features/`
- `docs/modules/`
- `docs/reference/`
- `docs/commands/`
- member, staff, and server-owner guides
- `docs/command-status.md`

Aliases, descriptions, complete subcommand paths, access classification, and catalog
counts should remain consistent. Maintainers can regenerate these catalogs from a sanitized
production export with:

```text
python3 tools/update_command_docs.py path/to/sickgamingbot-command-inventory.json
```

Review the resulting diff and update the narrative feature and setup pages whenever the
loaded module set or user-facing behavior changes.

## Pull requests

- Keep each pull request focused on one documentation problem or related feature set.
- Describe how the information was verified.
- List the pages changed and any manual checks performed.
- Call out assumptions or behavior that still requires live-bot verification.
- Do not combine unrelated cog implementation with public documentation changes.

## License

By contributing, you agree that your contributions will be licensed under the
[GNU General Public License version 3](LICENSE).
