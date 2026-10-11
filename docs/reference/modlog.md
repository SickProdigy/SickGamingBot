# Moderation Log commands

Loaded package: `ModLog`

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
| `-case` | — | Member | Show the specified case. |
| `-casesfor` | — | Member | Display cases for the specified member. |
| `-listcases` | — | Member | List cases for the specified member. |
| `-reason` | — | Member | Specify a reason for a modlog case. |

Live `-help` output remains authoritative for syntax, enabled state, hidden commands,
arguments, cooldowns, and server-specific access.
