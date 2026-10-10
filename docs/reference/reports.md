# Reports commands

Loaded package: `reports`

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
| `-report` | — | Member | Send a report. |
| `-report interact` | — | Moderator or required Discord permission | Open a message tunnel. |
| `-reportset` | — | Administrator or required Discord permission | Manage Reports. |
| `-reportset output` | — | Administrator or required Discord permission | Set the channel where reports will be sent. |
| `-reportset toggle` | `toggleactive` | Administrator or required Discord permission | Enable or disable reporting for this server. |

Live `-help` output remains authoritative for enabled state, hidden commands,
arguments, cooldowns, and server-specific access.
