# Rocket League commands

Loaded package: `RocketLeague`

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
| `-rlcs` | — | Member | Show the next RLCS event (short form of rocketleague rlcs). |
| `-rlcs event` | — | Member | Show a cached official event or an explicit start.gg tournament. |
| `-rlcs events` | `list` | Member | List discoverable official event IDs and slugs from the local cache. |
| `-rlcs recent` | — | Member | Show recently completed official events from retained weekly snapshots. |
| `-rlcs results` | — | Member | Show detailed cached results for a completed Rocket League event. |
| `-rlcs upcoming` | — | Member | Show later RLCS events (short form of rocketleague rlcs upcoming). |
| `-rlcsset` | — | Administrator or required Discord permission | Admin: configure automatic RLCS schedule announcements. |
| `-rlcsset channel` | — | Administrator or required Discord permission | Enable schedule updates in a channel. |
| `-rlcsset disable` | — | Administrator or required Discord permission | Disable automatic schedule updates for this server. |
| `-rlcsset postnow` | — | Administrator or required Discord permission | Post the current cached schedule without scraping BLAST. |
| `-rlcsset refresh` | — | Bot maintainer | Refresh BLAST when the seven-day request window permits. |
| `-rlcsset status` | — | Administrator or required Discord permission | Show announcement and weekly cache status. |
| `-rocketleague` | `rl` | Member | Browse Rocket League commands and announcement administration. |
| `-rocketleague clips` | — | Member | Show this server's automatic community clip feed. |
| `-rocketleague rlcs` | — | Member | Show the next RLCS event. |
| `-rocketleague rlcs event` | — | Member | Show a cached official event or an explicit start.gg tournament. |
| `-rocketleague rlcs events` | `list` | Member | List discoverable official event IDs and slugs from the local cache. |
| `-rocketleague rlcs recent` | — | Member | Show recently completed official events from retained weekly snapshots. |
| `-rocketleague rlcs results` | — | Member | Show detailed cached results for a completed Rocket League event. |
| `-rocketleague rlcs upcoming` | — | Member | Show RLCS tournaments scheduled after the next event. |
| `-rocketleague tournaments` | `tourney`, `tourneys` | Member | Show upcoming tournaments configured for this Discord server. |
| `-rocketleague tournaments recent` | — | Member | Show recently completed configured Rocket League tournaments. |
| `-rocketleague tournaments upcoming` | — | Member | Show upcoming configured Rocket League tournaments. |
| `-rocketleagueset` | `rlset` | Administrator or required Discord permission | Admin: configure server-specific tournaments and automatic clips. |
| `-rocketleagueset clips` | `clip` | Administrator or required Discord permission | Admin: configure automatic short Rocket League clips. |
| `-rocketleagueset clips channel` | — | Administrator or required Discord permission | Choose the channel for automatic clip posts. |
| `-rocketleagueset clips disable` | — | Administrator or required Discord permission | Disable automatic clip posts without removing settings. |
| `-rocketleagueset clips enable` | — | Administrator or required Discord permission | Enable automatic random clip posts. |
| `-rocketleagueset clips interval` | — | Administrator or required Discord permission | Set the approximate posting interval in hours (1-168). |
| `-rocketleagueset clips maxlength` | — | Administrator or required Discord permission | Set the longest eligible clip in seconds (15-600). |
| `-rocketleagueset clips notifications` | `notify` | Administrator or required Discord permission | Choose silent or normal delivery for automatic clip posts. |
| `-rocketleagueset clips postnow` | — | Administrator or required Discord permission | Post one unseen eligible clip in the configured channel now. |
| `-rocketleagueset clips refresh` | — | Administrator or required Discord permission | Refresh all configured clip-source caches now. |
| `-rocketleagueset clips sourceadd` | — | Administrator or required Discord permission | Add a Medal, Twitch, or YouTube source by URL or provider and name. |
| `-rocketleagueset clips sourceremove` | — | Administrator or required Discord permission | Remove a configured clip source by its server ID. |
| `-rocketleagueset clips sources` | — | Administrator or required Discord permission | List configured clip sources and their removal IDs. |
| `-rocketleagueset clips status` | — | Administrator or required Discord permission | Show this server's automatic clip settings. |
| `-rocketleagueset leagueadd` | — | Administrator or required Discord permission | Subscribe this server to a complete start.gg league URL. |
| `-rocketleagueset leaguedisable` | — | Administrator or required Discord permission | Disable automatic refresh and display for a league subscription. |
| `-rocketleagueset leaguerefresh` | — | Administrator or required Discord permission | Refresh one league subscription by ID, or every subscription. |
| `-rocketleagueset leagueremove` | — | Administrator or required Discord permission | Remove a start.gg league subscription and its cached tournaments. |
| `-rocketleagueset leagues` | — | Administrator or required Discord permission | List this server's start.gg league subscriptions. |
| `-rocketleagueset tournamentadd` | — | Administrator or required Discord permission | Validate, cache, and add a start.gg or Challonge tournament URL. |
| `-rocketleagueset tournamentrefresh` | — | Administrator or required Discord permission | Refresh one cached tournament by ID, or every configured tournament. |
| `-rocketleagueset tournamentremove` | — | Administrator or required Discord permission | Remove a configured tournament by its short ID or original URL. |
| `-rocketleagueset tournaments` | — | Administrator or required Discord permission | List cached tournaments, IDs, and removal instructions. |

Live `-help` output remains authoritative for syntax, enabled state, hidden commands,
arguments, cooldowns, and server-specific access.
