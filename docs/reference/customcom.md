# Custom Commands commands

Loaded package: `customcom`

Use `-help <command>` for complete syntax and argument details. Access below is
derived from declared command checks; server-specific permission rules can change it.

| Command | Aliases | Access | Description |
| --- | --- | --- | --- |
| `-customcom` | `cc` | Member | Base command for Custom Commands management. |
| `-customcom cooldown` | — | Moderator or required Discord permission | Set, edit, or view the cooldown for a custom command. |
| `-customcom create` | `add` | Moderator or required Discord permission | Create custom commands. |
| `-customcom create random` | — | Moderator or required Discord permission | Create a CC where it will randomly choose a response! |
| `-customcom create simple` | — | Moderator or required Discord permission | Add a simple custom command. |
| `-customcom delete` | `del`, `remove` | Moderator or required Discord permission | Delete a custom command. |
| `-customcom edit` | — | Moderator or required Discord permission | Edit a custom command. |
| `-customcom list` | — | Member | List all available custom commands. |
| `-customcom raw` | — | Member | Get the raw response of a custom command, to get the proper markdown. |
| `-customcom search` | — | Member | Searches through custom commands, according to the query. |
| `-customcom show` | — | Member | Shows a custom command's responses and its settings. |

Live `-help` output remains authoritative for enabled state, hidden commands,
arguments, cooldowns, and server-specific access.
