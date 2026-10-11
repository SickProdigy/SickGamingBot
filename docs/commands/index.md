# Command guides

Start with the guide that matches what you are trying to do:

- [Member commands](members.md) cover everyday utilities, games, media, profiles, and self-service actions.
- [Staff commands](staff.md) cover moderation and delegated feature management.
- [Server-owner commands](server-owners.md) cover guild-wide policy and configuration.
- [Bot-maintainer commands](maintainers.md) cover host-wide and global bot operations.
- [Complete command reference](../reference/index.md) lists all commands and subcommands by loaded module.
- [Using SickGamingBot help](../using-help.md) explains command and subcommand help paths.

Each audience catalog lists every command path assigned to that primary access tier.
The tiers are cumulative in practice: staff retain member commands, and server owners
retain member and staff commands. Bot-maintainer access is separate from Discord
server ownership.

SickGamingBot uses the `-` prefix. Use `-help <command>` or
`-help <command> <subcommand>` for current syntax, aliases, and access checks.

The old generated lists remain available as [legacy snapshots](../legacy-command-lists.md),
but they are not the current permission model.

## Baseline

The official runtime baseline was reviewed on 2026-10-10. SickGamingBot was running
Red 3.5.24 with 38 loaded packages and the `-` prefix. The custom cog reference uses
the installed Sick-Cogs source at commit
`42693ae13d35c0662abfd886ed6c2eb5332dc172`.

Loaded packages define the documented baseline. Individual commands or modules can
still be disabled, hidden, or restricted for a particular server, so live help remains
authoritative.

Age-restricted commands are included in the appropriate audience catalog for
completeness, but remain subject to channel, server, and Discord age restrictions.
