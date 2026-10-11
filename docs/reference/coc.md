# Clash of Clans commands

Loaded package: `Coc`

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
| `-coc` | `clashofclans` | Member | Show Clash of Clans clan information and war results. |
| `-coc attacks` | `attack`, `attackstatus`, `hits` | Member | Show the current war attack-status card. |
| `-coc clan` | — | Member | Look up a Clash of Clans clan by tag. |
| `-coc cwl` | — | Member | Show available rounds from a clan's currently active CWL group. |
| `-coc player` | — | Member | Look up a Clash of Clans player by tag. |
| `-coc war` | — | Member | Show a quick Clash of Clans war update. |
| `-coc warlog` | `warhistory` | Member | Show recent regular wars for a clan tag or the configured clan. |
| `-cocset` | — | Member | Configure this server's Clash of Clans integration. |
| `-cocset clan` | — | Member | Set this server's Clash of Clans clan tag. |
| `-cocset clanwarleague` | `cwl` | Member | Toggle all Clan War League notifications for this server. |
| `-cocset endwarning` | — | Member | Set how soon before war end the ending warning sends. |
| `-cocset event` | — | Member | Toggle one war notification event. |
| `-cocset managerrole` | — | Administrator or required Discord permission | Show, set, or clear the role allowed to manage CoC settings. |
| `-cocset mention` | — | Member | Toggle role mentions for one war notification event. |
| `-cocset notificationrole` | — | Member | Show, set, or clear the role used for war notification mentions. |
| `-cocset notifications` | — | Member | Toggle Clash of Clans war notifications for this server. |
| `-cocset notifications status` | — | Member | Show Clash of Clans war notification settings. |
| `-cocset prepwarning` | — | Member | Set how soon before battle day the preparation warning sends. |
| `-cocset raidweekend` | `capitalraid`, `raids` | Member | Toggle Clan Capital Raid Weekend start and end notifications. |
| `-cocset timezone` | — | Member | Set the timezone used for this server's war schedules. |
| `-cocset warattacks` | — | Member | Set war attack-log notifications to card or compact format. |
| `-cocset warchannel` | — | Member | Set this server's Clash of Clans war update channel. |

Live `-help` output remains authoritative for syntax, enabled state, hidden commands,
arguments, cooldowns, and server-specific access.
