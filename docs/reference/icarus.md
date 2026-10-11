# Icarus commands

Loaded package: `Icarus`

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
| `-icarus` | — | Member | Browse official Icarus Steam announcements. |
| `-icarus latest` | — | Member | Show the latest official Steam announcement, optionally by category. |
| `-icarus updates` | — | Member | Show 2 to 10 recent announcements as a newest-to-oldest clickable list. |
| `-icarusset` | — | Administrator or required Discord permission | Configure official Icarus announcements. |
| `-icarusset autopost` | — | Administrator or required Discord permission | Control automatic Icarus announcement posting. |
| `-icarusset autopost start` | — | Administrator or required Discord permission | Start automatic posting, optionally backfilling 2 to 10 matching posts. |
| `-icarusset autopost stop` | — | Administrator or required Discord permission | Stop automatic Icarus announcement posting. |
| `-icarusset categories` | — | Administrator or required Discord permission | Set content filters; hotfixes means posts explicitly named as hotfixes, not Steam Regular Updates. |
| `-icarusset channel` | — | Administrator or required Discord permission | Set the announcement channel; omit it to disable and clear the channel. |
| `-icarusset check` | — | Administrator or required Discord permission | Check Steam now and publish any new matching announcements. |
| `-icarusset interval` | — | Administrator or required Discord permission | Set how often Steam is checked, from 5 to 1440 minutes. |
| `-icarusset mode` | — | Administrator or required Discord permission | Choose card embeds or article-style posts with trailer and image gallery. |
| `-icarusset preview` | — | Administrator or required Discord permission | Preview the latest official announcement without changing delivery state. |
| `-icarusset role` | — | Administrator or required Discord permission | Set the optional role mentioned for matching announcements; omit to clear. |
| `-icarusset status` | — | Administrator or required Discord permission | No short description is declared. |

Live `-help` output remains authoritative for syntax, enabled state, hidden commands,
arguments, cooldowns, and server-specific access.
