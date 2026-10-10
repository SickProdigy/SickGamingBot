# Movie Releases commands

Loaded package: `movies`

Use `-help <command>` for complete syntax and argument details. Access below is
derived from declared command checks; server-specific permission rules can change it.

| Command | Aliases | Access | Description |
| --- | --- | --- | --- |
| `-movies` | `movie`, `moviereleases` | Member | Search for a movie by title, or show movie suggestions. |
| `-movieset` | `moviereleaseset` | Moderator or required Discord permission | Configure new movie release announcements. |
| `-movieset channel` | — | Moderator or required Discord permission | Set the channel that receives movie release posts. Defaults to this channel. |
| `-movieset clearhistory` | — | Moderator or required Discord permission | Clear remembered movie IDs so releases can be posted again. |
| `-movieset disable` | `disabled` | Moderator or required Discord permission | Disable hourly automatic movie release posts. |
| `-movieset enable` | `enabled` | Moderator or required Discord permission | Enable hourly automatic movie release posts. |
| `-movieset force` | — | Moderator or required Discord permission | Check now and post the next unposted release even if scheduled posting is disabled. |
| `-movieset maxperday` | — | Moderator or required Discord permission | Set the maximum automatic release posts per day. |
| `-movieset minvotes` | — | Moderator or required Discord permission | Set the minimum TMDb vote count required before posting a movie. |
| `-movieset preview` | — | Moderator or required Discord permission | Preview matching TMDb releases without posting them. |
| `-movieset role` | — | Moderator or required Discord permission | Set the role mentioned by automatic movie release announcements. |
| `-movieset roleclear` | `clearrole` | Moderator or required Discord permission | Stop mentioning a notification role in automatic release posts. |
| `-movieset settings` | — | Moderator or required Discord permission | Show current movie release settings. |
| `-movieset window` | — | Moderator or required Discord permission | Set the release date window checked by the cog. |

Live `-help` output remains authoritative for enabled state, hidden commands,
arguments, cooldowns, and server-specific access.
