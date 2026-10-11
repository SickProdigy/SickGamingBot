# Cog Manager commands

Loaded package: `CogManagerUI`

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

| Command | Aliases | Access | Description |
| --- | --- | --- | --- |
| `-addpath` | — | Bot maintainer | Add a path to the list of available cog paths. |
| `-cogs` | — | Bot maintainer | Lists all loaded and available cogs. |
| `-installpath` | — | Bot maintainer | Returns the current install path or sets it if one is provided. |
| `-paths` | — | Bot maintainer | Lists current cog paths in order of priority. |
| `-removepath` | — | Bot maintainer | Removes one or more paths from the available cog paths given the `path_numbers` from `-paths`. |
| `-reorderpath` | — | Bot maintainer | Reorders paths internally to allow discovery of different cogs. |

Live `-help` output remains authoritative for syntax, enabled state, hidden commands,
arguments, cooldowns, and server-specific access.
