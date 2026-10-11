# Aliases commands

Loaded package: `Alias`

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
| `-alias` | — | Member | Manage command aliases. |
| `-alias add` | — | Moderator or required Discord permission | Add an alias for a command. |
| `-alias delete` | `del`, `remove` | Moderator or required Discord permission | Delete an existing alias on this server. |
| `-alias edit` | — | Moderator or required Discord permission | Edit an existing alias in this server. |
| `-alias global` | — | Member | Manage global aliases. |
| `-alias global add` | — | Bot maintainer | Add a global alias for a command. |
| `-alias global delete` | `del`, `remove` | Bot maintainer | Delete an existing global alias. |
| `-alias global edit` | — | Bot maintainer | Edit an existing global alias. |
| `-alias global list` | — | Member | List the available global aliases on this bot. |
| `-alias help` | — | Member | Try to execute help for the base command of the alias. |
| `-alias list` | — | Member | List the available aliases on this server. |
| `-alias show` | — | Member | Show what command the alias executes. |

Live `-help` output remains authoritative for syntax, enabled state, hidden commands,
arguments, cooldowns, and server-specific access.
