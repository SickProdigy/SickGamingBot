# Trivia commands

Loaded package: `Trivia`

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
| `-trivia` | — | Member | Start trivia session on the specified category. |
| `-trivia info` | — | Member | Get information about a trivia category. |
| `-trivia leaderboard` | `lboard` | Member | Leaderboard for trivia. |
| `-trivia leaderboard global` | — | Member | Global trivia leaderboard. |
| `-trivia leaderboard server` | — | Member | Leaderboard for this server. |
| `-trivia list` | — | Member | List available trivia categories. |
| `-trivia stop` | — | Member | Stop an ongoing trivia session. |
| `-triviaset` | — | Moderator or required Discord permission | Manage Trivia settings. |
| `-triviaset botplays` | — | Moderator or required Discord permission | Set whether or not the bot gains points. |
| `-triviaset custom` | — | Bot maintainer | Manage Custom Trivia lists. |
| `-triviaset custom delete` | `remove` | Bot maintainer | Delete a trivia file. |
| `-triviaset custom list` | — | Bot maintainer | List uploaded custom trivia. |
| `-triviaset custom upload` | `add` | Bot maintainer | Upload a trivia file. |
| `-triviaset maxscore` | — | Moderator or required Discord permission | Set the total points required to win. |
| `-triviaset override` | — | Moderator or required Discord permission | Allow/disallow trivia lists to override settings. |
| `-triviaset payout` | — | Administrator or required Discord permission | Set the payout multiplier. |
| `-triviaset revealanswer` | — | Moderator or required Discord permission | Set whether or not the answer is revealed. |
| `-triviaset showsettings` | — | Moderator or required Discord permission | Show the current trivia settings. |
| `-triviaset stopafter` | — | Moderator or required Discord permission | Set how long until trivia stops due to no response. |
| `-triviaset timelimit` | — | Moderator or required Discord permission | Set the maximum seconds permitted to answer a question. |
| `-triviaset usespoilers` | — | Moderator or required Discord permission | Set if bot will display the answers in spoilers. |

Live `-help` output remains authoritative for syntax, enabled state, hidden commands,
arguments, cooldowns, and server-specific access.
