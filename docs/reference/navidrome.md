# Navidrome commands

Loaded package: `Navidrome`

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
| `-navidrome` | — | Member | Show this server's Navidrome library information. |
| `-navidrome account` | — | Member | Show your Discord-linked Navidrome account. |
| `-navidrome info` | `stats` | Member | Show non-sensitive Navidrome server and library information. |
| `-navidrome recent` | — | Member | Show recently added albums (1-10). |
| `-navidromeowner` | — | Bot maintainer | Manage bot-owner-approved Navidrome connections. |
| `-navidromeowner connection` | — | Bot maintainer | Manage approved connection profiles. |
| `-navidromeowner connection add` | — | Bot maintainer | Approve a URL after setting navidrome_NAME username/password API tokens. |
| `-navidromeowner connection list` | `show` | Bot maintainer | List approved connection names and redacted endpoints. |
| `-navidromeowner connection remove` | `delete` | Bot maintainer | Remove an approved connection profile. Credentials are not deleted. |
| `-navidromeowner connection test` | — | Bot maintainer | Test an approved connection without exposing credentials. |
| `-navidromeset` | — | Administrator or required Discord permission | Configure this server's Navidrome connection and announcements. |
| `-navidromeset channel` | `announcechannel` | Administrator or required Discord permission | Set the recently-added album channel. Defaults to this channel. |
| `-navidromeset connection` | — | Administrator or required Discord permission | Select a bot-owner-approved connection for this server. |
| `-navidromeset disable` | — | Administrator or required Discord permission | Disable scheduled album announcements. |
| `-navidromeset disconnect` | — | Administrator or required Discord permission | Disconnect this Discord server without deleting owner credentials. |
| `-navidromeset enable` | — | Administrator or required Discord permission | Enable album announcements and establish a no-flood baseline. |
| `-navidromeset interval` | — | Administrator or required Discord permission | Set album polling interval in minutes (15-1440). |
| `-navidromeset notificationrole` | `alertrole` | Administrator or required Discord permission | Set or clear the opt-in album alert role. |
| `-navidromeset notifications` | `notify` | Administrator or required Discord permission | Choose silent, normal, or opt-in-role album notifications. |
| `-navidromeset preview` | `test` | Administrator or required Discord permission | Preview the newest album without changing announcement history. |
| `-navidromeset quiethours` | — | Administrator or required Discord permission | Set local quiet hours or disable them with `off`. |
| `-navidromeset setup` | `interactive` | Administrator or required Discord permission | Open the guided Navidrome setup panel. |
| `-navidromeset status` | `settings` | Administrator or required Discord permission | Show this server's Navidrome settings. |
| `-navidromeset user` | — | Administrator or required Discord permission | Manage Discord-linked Navidrome accounts for this server. |
| `-navidromeset user create` | — | Administrator or required Discord permission | Create a non-admin Navidrome user and privately send its temporary password. |
| `-navidromeset user delete` | — | Administrator or required Discord permission | Permanently delete a linked Navidrome account; append `confirm`. |
| `-navidromeset user email` | — | Administrator or required Discord permission | Change a linked user's Navidrome email address. |
| `-navidromeset user info` | — | Administrator or required Discord permission | Show the current remote record for a linked member. |
| `-navidromeset user list` | — | Administrator or required Discord permission | List accounts provisioned through this Discord server. |
| `-navidromeset user name` | — | Administrator or required Discord permission | Change a linked user's Navidrome display name. |
| `-navidromeset user password` | `resetpassword` | Administrator or required Discord permission | Reset a linked user's password and send it privately. |
| `-navidromeset user unlink` | — | Administrator or required Discord permission | Remove only the Discord mapping; keep the Navidrome account. |

Live `-help` output remains authoritative for syntax, enabled state, hidden commands,
arguments, cooldowns, and server-specific access.
