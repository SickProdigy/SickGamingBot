# Moderation commands

Loaded package: `mod`

Use `-help <command>` for complete syntax and argument details. Access below is
derived from declared command checks; server-specific permission rules can change it.

| Command | Aliases | Access | Description |
| --- | --- | --- | --- |
| `-ban` | — | Administrator or required Discord permission | Ban a user from this server and optionally delete days of messages. |
| `-kick` | — | Administrator or required Discord permission | Kick a user. |
| `-massban` | `hackban` | Administrator or required Discord permission | Mass bans user(s) from the server. |
| `-modset` | — | Server owner or required Discord permission | Manage server administration settings. |
| `-modset defaultdays` | — | Server owner or required Discord permission | Set the default number of days worth of messages to be deleted when a user is banned. |
| `-modset defaultduration` | — | Server owner or required Discord permission | Set the default time to be used when a user is tempbanned. |
| `-modset deletenames` | — | Bot maintainer | Delete all stored usernames, global display names, and server nicknames. |
| `-modset deleterepeats` | — | Server owner or required Discord permission | Enable auto-deletion of repeated messages. |
| `-modset dm` | — | Server owner or required Discord permission | Settings for messaging the user when being kicked or banned. |
| `-modset dm banextrafieldcontents` | — | Server owner or required Discord permission | Set the contents for the optional extra embed on ban |
| `-modset dm banextrafieldtitle` | — | Server owner or required Discord permission | Set the title for the optional extra embed on ban. |
| `-modset dm banshowextrafield` | — | Server owner or required Discord permission | Toggle whether to show an extra customizable field when banning. |
| `-modset dm sendmessage` | — | Server owner or required Discord permission | Toggle whether a message should be sent to a user when they are kicked/banned. |
| `-modset hierarchy` | — | Server owner or required Discord permission | Toggle role hierarchy check for mods and admins. |
| `-modset mentionspam` | — | Server owner or required Discord permission | Manage the automoderation settings for mentionspam. |
| `-modset mentionspam ban` | — | Server owner or required Discord permission | Set the autoban conditions for mention spam. |
| `-modset mentionspam kick` | — | Server owner or required Discord permission | Sets the autokick conditions for mention spam. |
| `-modset mentionspam strict` | — | Server owner or required Discord permission | Setting to account for duplicate mentions. |
| `-modset mentionspam warn` | — | Server owner or required Discord permission | Sets the autowarn conditions for mention spam. |
| `-modset reinvite` | — | Server owner or required Discord permission | Toggle whether an invite will be sent to a user when unbanned. |
| `-modset requirereason` | — | Server owner or required Discord permission | Toggle whether a reason is required for mod actions. |
| `-modset showsettings` | — | Server owner or required Discord permission | Show the current server administration settings. |
| `-modset trackallnames` | — | Bot maintainer | Toggle whether all name changes should be tracked. |
| `-modset tracknicknames` | — | Server owner or required Discord permission | Toggle whether server nickname changes should be tracked. |
| `-movedeletedelay` | — | Bot maintainer | Move deletedelay settings to core |
| `-moveignoredchannels` | — | Bot maintainer | Move ignored channels and servers to core |
| `-names` | — | Member | Show previous usernames, global display names, and server nicknames of a member. |
| `-rename` | — | Administrator or required Discord permission | Change a member's server nickname. |
| `-slowmode` | — | Member | Changes thread's or text channel's slowmode setting. |
| `-softban` | — | Administrator or required Discord permission | Kick a user and delete 1 day's worth of their messages. |
| `-tempban` | — | Administrator or required Discord permission | Temporarily ban a user from this server. |
| `-unban` | — | Administrator or required Discord permission | Unban a user from this server. |
| `-userinfo` | — | Member | Show information about a member. |
| `-voiceban` | — | Administrator or required Discord permission | Ban a user from speaking and listening in the server's voice channels. |
| `-voicekick` | — | Moderator or required Discord permission | Kick a member from a voice channel. |
| `-voiceunban` | — | Administrator or required Discord permission | Unban a user from speaking and listening in the server's voice channels. |

Live `-help` output remains authoritative for enabled state, hidden commands,
arguments, cooldowns, and server-specific access.
