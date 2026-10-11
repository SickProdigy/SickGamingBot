# Advanced Help commands

Loaded package: `AdvancedHelp`

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
| `-advancedhelpset` | `advhelpset` | Bot maintainer | Configure the AdvancedHelp formatter. |
| `-advancedhelpset audience` | — | Bot maintainer | List command audience overrides. |
| `-advancedhelpset audience appearance` | — | Bot maintainer | Set audience emoji and name\|description. |
| `-advancedhelpset audience order` | — | Bot maintainer | Set all four audience keys in display order. |
| `-advancedhelpset audience remove` | — | Bot maintainer | No short description is declared. |
| `-advancedhelpset audience set` | — | Bot maintainer | Assign a command to member, staff, server_owner, or bot_owner. |
| `-advancedhelpset category` | — | Bot maintainer | List command category overrides. |
| `-advancedhelpset category appearance` | — | Bot maintainer | Set category order, emoji, and name\|description. |
| `-advancedhelpset category remove` | — | Bot maintainer | No short description is declared. |
| `-advancedhelpset category set` | — | Bot maintainer | Assign an available command to a presentation category. |
| `-advancedhelpset deleteontimeout` | — | Bot maintainer | Delete interactive help when it expires instead of disabling it. |
| `-advancedhelpset destination` | — | Bot maintainer | Choose channel or DM delivery for bare prefix help. |
| `-advancedhelpset rolegroup` | — | Bot maintainer | List role-backed presentation groups. |
| `-advancedhelpset rolegroup add` | — | Bot maintainer | Add a Discord role to a named presentation group. |
| `-advancedhelpset rolegroup appearance` | — | Bot maintainer | Set a role group order, emoji, and name\|description. |
| `-advancedhelpset rolegroup category` | — | Bot maintainer | Add a presentation category to a named role group. |
| `-advancedhelpset rolegroup remove` | — | Bot maintainer | No short description is declared. |
| `-advancedhelpset timeout` | — | Bot maintainer | Set the interactive timeout from 30 through 900 seconds. |
| `-docsreport` | `commandinventory` | Bot maintainer | Export sanitized metadata for every registered command. |

Live `-help` output remains authoritative for syntax, enabled state, hidden commands,
arguments, cooldowns, and server-specific access.
