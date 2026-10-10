# DayZ commands

Loaded package: `dayz`

Use `-help <command>` for complete syntax and argument details. Access below is
derived from declared command checks; server-specific permission rules can change it.

| Command | Aliases | Access | Description |
| --- | --- | --- | --- |
| `-dayz` | — | Member | Browse official DayZ Steam announcements. |
| `-dayz latest` | — | Member | Show the latest official Steam announcement, optionally by category. |
| `-dayz updates` | — | Member | Show 2 to 10 recent announcements as a newest-to-oldest clickable list. |
| `-dayzset` | — | Administrator or required Discord permission | Configure official DayZ announcements. |
| `-dayzset autopost` | — | Administrator or required Discord permission | Control automatic DayZ announcement posting. |
| `-dayzset autopost start` | — | Administrator or required Discord permission | Start automatic posting, optionally backfilling 2 to 10 matching posts. |
| `-dayzset autopost stop` | — | Administrator or required Discord permission | Stop automatic DayZ announcement posting. |
| `-dayzset categories` | — | Administrator or required Discord permission | Set content filters; hotfixes means posts explicitly named as hotfixes, not Steam Regular Updates. |
| `-dayzset channel` | — | Administrator or required Discord permission | Set the announcement channel; omit it to disable and clear the channel. |
| `-dayzset check` | — | Administrator or required Discord permission | Check Steam now and publish any new matching announcements. |
| `-dayzset interval` | — | Administrator or required Discord permission | Set how often Steam is checked, from 5 to 1440 minutes. |
| `-dayzset mode` | — | Administrator or required Discord permission | Choose card embeds or article-style posts with trailer and image gallery. |
| `-dayzset preview` | — | Administrator or required Discord permission | Preview the latest official announcement without changing delivery state. |
| `-dayzset role` | — | Administrator or required Discord permission | Set the optional role mentioned for matching announcements; omit to clear. |
| `-dayzset status` | — | Administrator or required Discord permission | See live help. |

Live `-help` output remains authoritative for enabled state, hidden commands,
arguments, cooldowns, and server-specific access.
