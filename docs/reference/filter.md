# Filter commands

Loaded package: `Filter`

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
| `-filter` | — | Moderator or required Discord permission | Base command to add or remove words from the server filter. |
| `-filter add` | — | Moderator or required Discord permission | Add words to the filter. |
| `-filter channel` | — | Moderator or required Discord permission | Base command to add or remove words from the channel filter. |
| `-filter channel add` | — | Moderator or required Discord permission | Add words to the filter. |
| `-filter channel clear` | — | Moderator or required Discord permission | Clears this channel's filter list. |
| `-filter channel delete` | `del`, `remove` | Moderator or required Discord permission | Remove words from the filter. |
| `-filter channel list` | — | Moderator or required Discord permission | Send a list of the channel's filtered words. |
| `-filter clear` | — | Moderator or required Discord permission | Clears this server's filter list. |
| `-filter delete` | `del`, `remove` | Moderator or required Discord permission | Remove words from the filter. |
| `-filter list` | — | Moderator or required Discord permission | Send a list of this server's filtered words. |
| `-filter names` | — | Moderator or required Discord permission | Toggle name and nickname filtering. |
| `-filterset` | — | Administrator or required Discord permission | Base command to manage filter settings. |
| `-filterset ban` | — | Administrator or required Discord permission | Set the filter's autoban conditions. |
| `-filterset defaultname` | — | Administrator or required Discord permission | Set the nickname for users with a filtered name. |

Live `-help` output remains authoritative for syntax, enabled state, hidden commands,
arguments, cooldowns, and server-specific access.
