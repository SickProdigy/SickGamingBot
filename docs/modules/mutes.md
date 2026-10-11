# Mutes

> Server, channel, and voice mute workflows with configurable behavior.

## At a glance

- **Category:** Moderation and safety
- **Intended audience:** Moderators apply mutes; administrators configure mute behavior.
- **Loaded package:** `mutes`
- **Documented commands:** 17 commands and subcommands

## Main command families

| Command | Default access | Purpose |
| --- | --- | --- |
| `-activemutes` | Moderator or required permission | Displays active mutes on this server. |
| `-forceunmute` | Moderator or required permission | Force Unmute users who have had channel overwrite mutes in every channel. |
| `-mute` | Moderator or required permission | Mute users. |
| `-mutechannel` | Moderator or required permission | Mute a user in the current text channel (or in the parent of the current thread). |
| `-muteset` | Member | Mute settings. |
| `-timeout` | Moderator or required permission | Timeout users. |
| `-unmute` | Moderator or required permission | Unmute users. |
| `-unmutechannel` | Moderator or required permission | Unmute a user in this channel (or in the parent of this thread). |
| `-voicemute` | Member | Mute a user in their current voice channel. |
| `-voiceunmute` | Member | Unmute a user in their current voice channel. |

## Using this module

Run help for a command family, then add subcommands to request more specific details:

```text
-help activemutes
-help activemutes <subcommand>
```

The bot only shows commands available to your account. Server-specific permission
rules, disabled commands, required integrations, and channel restrictions can change
what you can use.

## Learn more

- [Complete Mutes command reference](../reference/mutes.md)
- [Using SickGamingBot help](../using-help.md)
- [Permissions and access levels](../permissions.md)
