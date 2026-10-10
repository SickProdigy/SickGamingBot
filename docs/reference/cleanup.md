# Cleanup commands

Loaded package: `cleanup`

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
| `-cleanup` | — | Member | Base command for deleting messages. |
| `-cleanup after` | — | Moderator or required Discord permission | Delete all messages after a specified message. |
| `-cleanup before` | — | Moderator or required Discord permission | Deletes X messages before the specified message. |
| `-cleanup between` | — | Moderator or required Discord permission | Delete the messages between Message One and Message Two, providing the messages IDs. |
| `-cleanup bot` | — | Moderator or required Discord permission | Clean up command messages and messages from the bot in the current channel. |
| `-cleanup duplicates` | `spam` | Moderator or required Discord permission | Deletes duplicate messages in the channel from the last X messages and keeps only one copy. |
| `-cleanup messages` | — | Moderator or required Discord permission | Delete the last X messages in the current channel. |
| `-cleanup self` | — | Member | Clean up messages owned by the bot in the current channel. |
| `-cleanup text` | — | Moderator or required Discord permission | Delete the last X messages matching the specified text in the current channel. |
| `-cleanup user` | — | Moderator or required Discord permission | Delete the last X messages from a specified user in the current channel. |
| `-cleanupset` | — | Administrator or required Discord permission | Manage the settings for the cleanup command. |
| `-cleanupset notify` | — | Administrator or required Discord permission | Toggle clean up notification settings. |

Live `-help` output remains authoritative for enabled state, hidden commands,
arguments, cooldowns, and server-specific access.
