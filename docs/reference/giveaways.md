# Giveaways commands

Loaded package: `giveaways`

## Reading this reference

Each command is shown as its complete path. To see detailed help, put that path after
`-help` without repeating the leading hyphen:

```text
-help <command>
-help <command> <subcommand>
-help <command> <subcommand> <nested-subcommand>
```

The access column is derived from declared command checks. Server-specific permission
rules can change it. See [Using SickGamingBot help](../using-help.md) for examples and
an explanation of required and optional arguments.

| Command | Aliases | Access | Description |
| --- | --- | --- | --- |
| `-giveaway` | `gw`, `giveaways` | Required Discord permission | Manage the giveaway system |
| `-giveaway advanced` | `adv` | Required Discord permission | Advanced creation of Giveaways. |
| `-giveaway cancel` | — | Required Discord permission | Cancel an active giveaway without drawing a winner. |
| `-giveaway edit` | — | Required Discord permission | Edit the supported settings of an active giveaway. |
| `-giveaway end` | — | Required Discord permission | End a giveaway. |
| `-giveaway entrants` | — | Required Discord permission | List all entrants for a giveaway. |
| `-giveaway explain` | — | Required Discord permission | Explanation of giveaway advanced and the arguements it supports. |
| `-giveaway info` | — | Required Discord permission | Information about a giveaway. |
| `-giveaway list` | — | Required Discord permission | List all giveaways in the server. |
| `-giveaway reroll` | — | Required Discord permission | Reroll a giveaway. |
| `-giveaway start` | — | Required Discord permission | Start a giveaway. |

Live `-help` output remains authoritative for enabled state, hidden commands,
arguments, cooldowns, and server-specific access.
