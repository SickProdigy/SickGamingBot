# Garry's Mod commands

Loaded package: `GMod`

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
| `-gmod` | — | Member | Show Garry's Mod server status and browse official updates. |
| `-gmod connect` | — | Member | No short description is declared. |
| `-gmod servers` | — | Member | No short description is declared. |
| `-gmod status` | — | Member | No short description is declared. |
| `-gmod updates` | — | Member | Show 1 to 10 recent official Steam announcements. |
| `-gmodowner` | — | Bot maintainer | Manage bot-owner-only GMod network policy. |
| `-gmodowner privatehost` | — | Bot maintainer | No short description is declared. |
| `-gmodowner privatehost add` | — | Bot maintainer | No short description is declared. |
| `-gmodowner privatehost remove` | — | Bot maintainer | No short description is declared. |
| `-gmodset` | — | Administrator or required Discord permission | Configure Garry's Mod status and Steam announcements. |
| `-gmodset add` | — | Administrator or required Discord permission | Add or replace a named GMod server after a successful safe query. |
| `-gmodset default` | — | Administrator or required Discord permission | Choose the default server used by public GMod commands. |
| `-gmodset info` | `status` | Administrator or required Discord permission | Show current GMod server-monitoring and Steam-update settings. |
| `-gmodset monitoring` | — | Administrator or required Discord permission | Start or stop server outage/recovery monitoring. |
| `-gmodset remove` | — | Administrator or required Discord permission | Remove a configured GMod server. |
| `-gmodset statuschannel` | — | Administrator or required Discord permission | Set the outage/recovery channel; omit it to stop monitoring and clear it. |
| `-gmodset statusinterval` | — | Administrator or required Discord permission | Set the server-status polling interval from 5 to 1,440 minutes. |
| `-gmodset statusrole` | — | Administrator or required Discord permission | Set the optional role mentioned for status changes; omit it to clear. |
| `-gmodset updates` | — | Administrator or required Discord permission | Show whether automatic official Steam-news posting is running. |
| `-gmodset updates start` | — | Administrator or required Discord permission | Start automatic posting, optionally backfilling 2 to 10 recent posts. |
| `-gmodset updates stop` | — | Administrator or required Discord permission | Stop automatic official Steam-news posting. |
| `-gmodset updateschannel` | — | Administrator or required Discord permission | Set the Steam-news channel; omit it to stop posting and clear it. |
| `-gmodset updatescheck` | — | Administrator or required Discord permission | Check Steam now and publish any unseen official announcements. |
| `-gmodset updatesinterval` | — | Administrator or required Discord permission | Set the Steam-news polling interval from 5 to 1,440 minutes. |
| `-gmodset updatesrole` | — | Administrator or required Discord permission | Set the optional role mentioned for new Steam posts; omit it to clear. |

Live `-help` output remains authoritative for syntax, enabled state, hidden commands,
arguments, cooldowns, and server-specific access.
