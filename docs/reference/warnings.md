# Warnings commands

Loaded package: `warnings`

Use `-help <command>` for complete syntax and argument details. Access below is
derived from declared command checks; server-specific permission rules can change it.

| Command | Aliases | Access | Description |
| --- | --- | --- | --- |
| `-actionlist` | — | Administrator or required Discord permission | List all configured automated actions for Warnings. |
| `-mywarnings` | — | Member | List warnings for yourself. |
| `-reasonlist` | — | Administrator or required Discord permission | List all configured reasons for Warnings. |
| `-unwarn` | — | Administrator or required Discord permission | Remove a warning from a user. |
| `-warn` | — | Administrator or required Discord permission | Warn the user for the specified reason. |
| `-warnaction` | — | Server owner or required Discord permission | Manage automated actions for Warnings. |
| `-warnaction add` | — | Server owner or required Discord permission | Create an automated action. |
| `-warnaction delete` | `del`, `remove` | Server owner or required Discord permission | Delete the action with the specified name. |
| `-warnings` | — | Administrator | List the warnings for the specified user. |
| `-warningset` | — | Server owner or required Discord permission | Manage settings for Warnings. |
| `-warningset allowcustomreasons` | — | Server owner or required Discord permission | Enable or disable custom reasons for a warning. |
| `-warningset mywarnings` | — | Server owner or required Discord permission | Manage the settings for `-mywarnings`. |
| `-warningset mywarnings sendtodms` | — | Server owner or required Discord permission | Whether a member self requesting their warnings with `-mywarnings` should get them sent to DMs or in the current channel. |
| `-warningset senddm` | — | Server owner or required Discord permission | Set whether warnings should be sent to users in DMs. |
| `-warningset showmoderator` | — | Server owner or required Discord permission | Decide whether the name of the moderator warning a user should be included in the DM to that user when being |
| `-warningset usewarnchannel` | — | Server owner or required Discord permission | Set if warnings should be sent to a channel set with `-warningset warnchannel`. |
| `-warningset warnchannel` | — | Server owner or required Discord permission | Set the channel where warnings should be sent to. |
| `-warnreason` | — | Server owner or required Discord permission | Manage warning reasons. |
| `-warnreason create` | `add` | Server owner or required Discord permission | Create a warning reason. |
| `-warnreason delete` | `remove`, `del` | Server owner or required Discord permission | Delete a warning reason. |

Live `-help` output remains authoritative for enabled state, hidden commands,
arguments, cooldowns, and server-specific access.
