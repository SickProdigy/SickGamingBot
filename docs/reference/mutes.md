# Mutes commands

Loaded package: `Mutes`

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
| `-activemutes` | — | Moderator or required Discord permission | Displays active mutes on this server. |
| `-forceunmute` | — | Moderator or required Discord permission | Force Unmute users who have had channel overwrite mutes in every channel. |
| `-mute` | — | Moderator or required Discord permission | Mute users. |
| `-mutechannel` | `channelmute` | Moderator or required Discord permission | Mute a user in the current text channel (or in the parent of the current thread). |
| `-muteset` | — | Member | Mute settings. |
| `-muteset defaulttime` | `time` | Moderator or required Discord permission | Set the default mute time for the mute command. |
| `-muteset makerole` | — | Administrator or required Discord permission | Create a Muted role. |
| `-muteset notification` | — | Administrator or required Discord permission | Set the notification channel for automatic unmute issues. |
| `-muteset role` | — | Administrator or required Discord permission | Sets the role to be applied when muting a user. |
| `-muteset senddm` | — | Moderator or required Discord permission | Set whether mute notifications should be sent to users in DMs. |
| `-muteset settings` | `showsettings` | Moderator or required Discord permission | Shows the current mute settings for this guild. |
| `-muteset showmoderator` | — | Moderator or required Discord permission | Decide whether the name of the moderator muting a user should be included in the DM to that user. |
| `-timeout` | — | Moderator or required Discord permission | Timeout users. |
| `-unmute` | — | Moderator or required Discord permission | Unmute users. |
| `-unmutechannel` | `channelunmute` | Moderator or required Discord permission | Unmute a user in this channel (or in the parent of this thread). |
| `-voicemute` | — | Member | Mute a user in their current voice channel. |
| `-voiceunmute` | — | Member | Unmute a user in their current voice channel. |

Live `-help` output remains authoritative for syntax, enabled state, hidden commands,
arguments, cooldowns, and server-specific access.
