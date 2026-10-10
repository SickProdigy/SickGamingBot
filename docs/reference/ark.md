# ARK commands

Loaded package: `ark`

Use `-help <command>` for complete syntax and argument details. Access below is
derived from declared command checks; server-specific permission rules can change it.

| Command | Aliases | Access | Description |
| --- | --- | --- | --- |
| `-ark` | — | Member | View the latest official ARK: Survival Ascended announcement. |
| `-ark latest` | — | Member | Show the latest official Steam announcement, optionally by category. |
| `-ark updates` | — | Member | Show 2 to 10 recent announcements as a newest-to-oldest clickable list. |
| `-arkset` | — | Administrator or required Discord permission | Configure official ARK: Survival Ascended announcements. |
| `-arkset autopost` | — | Administrator or required Discord permission | Control automatic ARK announcement posting. |
| `-arkset autopost start` | — | Administrator or required Discord permission | Start automatic posting, optionally backfilling 2 to 10 matching posts. |
| `-arkset autopost stop` | — | Administrator or required Discord permission | Stop automatic ARK announcement posting. |
| `-arkset categories` | — | Administrator or required Discord permission | Set content filters; hotfixes means posts explicitly named as hotfixes, not Steam Regular Updates. |
| `-arkset channel` | — | Administrator or required Discord permission | Set the announcement channel; omit it to disable and clear the channel. |
| `-arkset check` | — | Administrator or required Discord permission | Check Steam now and publish any new matching announcements. |
| `-arkset interval` | — | Administrator or required Discord permission | Set how often Steam is checked, from 5 to 1440 minutes. |
| `-arkset mode` | — | Administrator or required Discord permission | Choose card embeds or article-style posts with trailer and image gallery. |
| `-arkset preview` | — | Administrator or required Discord permission | Preview the latest official announcement without changing delivery state. |
| `-arkset role` | — | Administrator or required Discord permission | Set the optional role mentioned for matching announcements; omit to clear. |
| `-arkset status` | — | Administrator or required Discord permission | See live help. |

Live `-help` output remains authoritative for enabled state, hidden commands,
arguments, cooldowns, and server-specific access.
