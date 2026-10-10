# Streams commands

Loaded package: `streams`

Use `-help <command>` for complete syntax and argument details. Access below is
derived from declared command checks; server-specific permission rules can change it.

| Command | Aliases | Access | Description |
| --- | --- | --- | --- |
| `-picarto` | — | Member | Check if a Picarto channel is live. |
| `-streamalert` | — | Moderator or required Discord permission | Manage automated stream alerts. |
| `-streamalert list` | — | Moderator or required Discord permission | List all active stream alerts in this server. |
| `-streamalert picarto` | — | Moderator or required Discord permission | Toggle alerts in this channel for a Picarto stream. |
| `-streamalert stop` | — | Moderator or required Discord permission | Disable all stream alerts in this channel or server. |
| `-streamalert twitch` | — | Moderator or required Discord permission | Manage Twitch stream notifications. |
| `-streamalert twitch channel` | — | Moderator or required Discord permission | Toggle alerts in this or the given channel for a Twitch stream. |
| `-streamalert youtube` | — | Moderator or required Discord permission | Toggle alerts in this channel for a YouTube stream. |
| `-streamset` | — | Moderator or required Discord permission | Manage stream alert settings. |
| `-streamset autodelete` | — | Moderator or required Discord permission | Toggle alert deletion for when streams go offline. |
| `-streamset ignorereruns` | — | Moderator or required Discord permission | Toggle excluding rerun streams from alerts. |
| `-streamset ignoreschedule` | — | Moderator or required Discord permission | Toggle excluding YouTube streams schedules from alerts. |
| `-streamset mention` | — | Moderator or required Discord permission | Manage mention settings for stream alerts. |
| `-streamset mention all` | `everyone` | Moderator or required Discord permission | Toggle the `@​everyone` mention. |
| `-streamset mention online` | `here` | Moderator or required Discord permission | Toggle the `@​here` mention. |
| `-streamset mention role` | — | Moderator or required Discord permission | Toggle a role mention. |
| `-streamset message` | — | Moderator or required Discord permission | Manage custom messages for stream alerts. |
| `-streamset message clear` | — | Moderator or required Discord permission | Reset the stream alert messages in this server. |
| `-streamset message mention` | — | Moderator or required Discord permission | Set stream alert message when mentions are enabled. |
| `-streamset message nomention` | — | Moderator or required Discord permission | Set stream alert message when mentions are disabled. |
| `-streamset timer` | — | Bot maintainer | Set stream check refresh time. |
| `-streamset twitchtoken` | — | Bot maintainer | Explain how to set the twitch token. |
| `-streamset usebuttons` | — | Moderator or required Discord permission | Toggle whether to use buttons for stream alerts. |
| `-streamset youtubekey` | — | Bot maintainer | Explain how to set the YouTube token. |
| `-twitchstream` | — | Member | Check if a Twitch channel is live. |
| `-youtubestream` | — | Member | Check if a YouTube channel is live. |

Live `-help` output remains authoritative for enabled state, hidden commands,
arguments, cooldowns, and server-specific access.
