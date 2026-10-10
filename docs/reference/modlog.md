# Moderation Log commands

Loaded package: `modlog`

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
| `-case` | — | Member | Show the specified case. |
| `-casesfor` | — | Member | Display cases for the specified member. |
| `-listcases` | — | Member | List cases for the specified member. |
| `-reason` | — | Member | Specify a reason for a modlog case. |

Live `-help` output remains authoritative for enabled state, hidden commands,
arguments, cooldowns, and server-specific access.
