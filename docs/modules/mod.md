# Moderation

> Bans, kicks, nickname management, slow mode, voice moderation, and member information.

## At a glance

- **Category:** Moderation and safety
- **Intended audience:** Moderators and administrators.
- **Loaded package:** `mod`
- **Documented commands:** 36 commands and subcommands

## Main command families

| Command | Default access | Purpose |
| --- | --- | --- |
| `-ban` | Administrator or required permission | Ban a user from this server and optionally delete days of messages. |
| `-kick` | Administrator or required permission | Kick a user. |
| `-massban` | Administrator or required permission | Mass bans user(s) from the server. |
| `-modset` | Server owner or required permission | Manage server administration settings. |
| `-movedeletedelay` | Bot maintainer | Move deletedelay settings to core |
| `-moveignoredchannels` | Bot maintainer | Move ignored channels and servers to core |
| `-names` | Member | Show previous usernames, global display names, and server nicknames of a member. |
| `-rename` | Administrator or required permission | Change a member's server nickname. |
| `-slowmode` | Member | Changes thread's or text channel's slowmode setting. |
| `-softban` | Administrator or required permission | Kick a user and delete 1 day's worth of their messages. |
| `-tempban` | Administrator or required permission | Temporarily ban a user from this server. |
| `-unban` | Administrator or required permission | Unban a user from this server. |
| `-userinfo` | Member | Show information about a member. |
| `-voiceban` | Administrator or required permission | Ban a user from speaking and listening in the server's voice channels. |
| `-voicekick` | Moderator or required permission | Kick a member from a voice channel. |
| `-voiceunban` | Administrator or required permission | Unban a user from speaking and listening in the server's voice channels. |

## Using this module

Run help for a command family, then add subcommands to request more specific details:

```text
-help ban
-help ban <subcommand>
```

The bot only shows commands available to your account. Server-specific permission
rules, disabled commands, required integrations, and channel restrictions can change
what you can use.

## Learn more

- [Complete Moderation command reference](../reference/mod.md)
- [Using SickGamingBot help](../using-help.md)
- [Permissions and access levels](../permissions.md)
