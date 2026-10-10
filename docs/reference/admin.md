# Administration commands

Loaded package: `admin`

## Reading this reference

Each command is shown as its complete path. To see detailed help, put that path after
`-help` without repeating the leading hyphen:

```text
-help <command>
-help <command> <subcommand>
-help <command> <subcommand> <nested-subcommand>
```

The access column is derived from declared command checks. Server-specific permission
rules can change it. See [Using SickGamingBot help](../using-help.md) for examples and
an explanation of required and optional arguments.

| Command | Aliases | Access | Description |
| --- | --- | --- | --- |
| `-addrole` | — | Administrator or required Discord permission | Add a role to a user. |
| `-announce` | — | Bot maintainer | Announce a message to all servers the bot is in. |
| `-announce cancel` | — | Bot maintainer | Cancel a running announce. |
| `-announceset` | — | Server owner or required Discord permission | Change how announcements are sent in this guild. |
| `-announceset channel` | — | Server owner or required Discord permission | Change the channel where the bot will send announcements. |
| `-announceset clearchannel` | — | Server owner or required Discord permission | Unsets the channel for announcements. |
| `-editrole` | — | Administrator or required Discord permission | Edit role settings. |
| `-editrole colour` | `color` | Administrator or required Discord permission | Edit a role's colour. |
| `-editrole name` | — | Administrator or required Discord permission | Edit a role's name. |
| `-removerole` | — | Administrator or required Discord permission | Remove a role from a user. |
| `-selfrole` | — | Member | Add or remove a selfrole from yourself. |
| `-selfrole add` | — | Member | Add a selfrole to yourself. |
| `-selfrole list` | — | Member | Lists all available selfroles. |
| `-selfrole remove` | — | Member | Remove a selfrole from yourself. |
| `-selfroleset` | — | Administrator or required Discord permission | Manage selfroles. |
| `-selfroleset add` | — | Administrator or required Discord permission | Add a role, or a selection of roles, to the list of available selfroles. |
| `-selfroleset clear` | — | Administrator or required Discord permission | Clear the list of available selfroles for this server. |
| `-selfroleset remove` | — | Administrator or required Discord permission | Remove a role, or a selection of roles, from the list of available selfroles. |
| `-serverlock` | — | Bot maintainer | Lock a bot to its current servers only. |

Live `-help` output remains authoritative for enabled state, hidden commands,
arguments, cooldowns, and server-specific access.
