# Staff commands

These command paths declare moderator, administrator, or specific Discord permission requirements. Delegated managers may receive narrower access.

Use live help for current syntax and checks:

```text
-help <command>
-help <command> <subcommand>
-help <command> <subcommand> <nested-subcommand>
```

The catalog is generated from the sanitized production command inventory. Server
rules, role hierarchy, disabled commands, channel permissions, and module configuration
can further restrict availability. [Learn how to use command help](../using-help.md).

## Catalog (505 command paths)

### [ARK](../modules/ark.md) (12)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-arkset` | — | Administrator or required Discord permission | Configure official ARK: Survival Ascended announcements. |
| `-arkset autopost` | — | Administrator or required Discord permission | Control automatic ARK announcement posting. |
| `-arkset autopost start` | — | Administrator or required Discord permission | Start automatic posting, optionally backfilling 2 to 10 matching posts. |
| `-arkset autopost stop` | — | Administrator or required Discord permission | Stop automatic ARK announcement posting. |
| `-arkset categories` | — | Administrator or required Discord permission | Set content filters; hotfixes means posts explicitly named as hotfixes, not Steam Regular Updates. |
| `-arkset channel` | — | Administrator or required Discord permission | Set the announcement channel; omit it to disable and clear the channel. |
| `-arkset check` | — | Administrator or required Discord permission | Check Steam now and publish any new matching announcements. |
| `-arkset interval` | — | Administrator or required Discord permission | Set how often Steam is checked, from 5 to 1440 minutes. |
| `-arkset mode` | — | Administrator or required Discord permission | Choose card embeds or article-style posts with trailer and image gallery. |
| `-arkset preview` | — | Administrator or required Discord permission | Preview the latest official announcement without changing delivery state. |
| `-arkset role` | — | Administrator or required Discord permission | Set the optional role mentioned for matching announcements; omit to clear. |
| `-arkset status` | — | Administrator or required Discord permission | No short description is declared. |

### [Administration](../modules/admin.md) (9)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-addrole` | — | Administrator or required Discord permission | Add a role to a user. |
| `-editrole` | — | Administrator or required Discord permission | Edit role settings. |
| `-editrole colour` | `color` | Administrator or required Discord permission | Edit a role's colour. |
| `-editrole name` | — | Administrator or required Discord permission | Edit a role's name. |
| `-removerole` | — | Administrator or required Discord permission | Remove a role from a user. |
| `-selfroleset` | — | Administrator or required Discord permission | Manage selfroles. |
| `-selfroleset add` | — | Administrator or required Discord permission | Add a role, or a selection of roles, to the list of available selfroles. |
| `-selfroleset clear` | — | Administrator or required Discord permission | Clear the list of available selfroles for this server. |
| `-selfroleset remove` | — | Administrator or required Discord permission | Remove a role, or a selection of roles, from the list of available selfroles. |

### [Age-Restricted](../modules/nsfw.md) (6)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-nsfwset` | — | Administrator or required Discord permission | Settings for the Nsfw cog. |
| `-nsfwset autopost` | — | Administrator or required Discord permission | Configure this server's one scheduled NSFW feed. |
| `-nsfwset autopost off` | `disable`, `remove` | Administrator or required Discord permission | Remove this server's scheduled NSFW feed. |
| `-nsfwset autopost preview` | `test` | Administrator or required Discord permission | Preview one post without changing or advancing the schedule. |
| `-nsfwset autopost status` | `show` | Administrator or required Discord permission | Show this server's scheduled NSFW feed. |
| `-nsfwset notifications` | `notify` | Administrator or required Discord permission | Choose silent or normal delivery for scheduled NSFW posts. |

### [Aliases](../modules/alias.md) (3)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-alias add` | — | Moderator or required Discord permission | Add an alias for a command. |
| `-alias delete` | `del`, `remove` | Moderator or required Discord permission | Delete an existing alias on this server. |
| `-alias edit` | — | Moderator or required Discord permission | Edit an existing alias in this server. |

### [Audio](../modules/audio.md) (32)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-audioset autodeafen` | — | Moderator or required Discord permission | Toggle whether the bot will be auto deafened upon joining the voice channel. |
| `-audioset autoplay` | — | Moderator or required Discord permission | Change auto-play setting. |
| `-audioset autoplay playlist` | — | Moderator or required Discord permission | Set a playlist to auto-play songs from. |
| `-audioset autoplay reset` | — | Moderator or required Discord permission | Resets auto-play to the default playlist. |
| `-audioset autoplay toggle` | — | Moderator or required Discord permission | Toggle auto-play when there no songs in queue. |
| `-audioset countrycode` | — | Moderator or required Discord permission | Set the country code for Spotify searches. |
| `-audioset dailyqueue` | — | Administrator | Toggle daily queues. |
| `-audioset dc` | — | Moderator or required Discord permission | Toggle the bot auto-disconnecting when done playing. |
| `-audioset dj` | — | Administrator or required Discord permission | Toggle DJ mode. |
| `-audioset emptydisconnect` | — | Moderator or required Discord permission | Auto-disconnect from channel when bot is alone in it for x seconds, 0 to disable. |
| `-audioset emptypause` | — | Moderator or required Discord permission | Auto-pause after x seconds when room is empty, 0 to disable. |
| `-audioset jukebox` | — | Moderator or required Discord permission | Set a price for queueing tracks for non-mods, 0 to disable. |
| `-audioset lyrics` | — | Moderator or required Discord permission | Prioritise tracks with lyrics. |
| `-audioset maxlength` | — | Moderator or required Discord permission | Max length of a track to queue in seconds, 0 to disable. |
| `-audioset maxvolume` | — | Administrator or required Discord permission | Set the maximum volume allowed in this server. |
| `-audioset notify` | — | Moderator or required Discord permission | Toggle track announcement and other bot messages. |
| `-audioset persistqueue` | — | Administrator | Toggle persistent queues. |
| `-audioset restrictions` | — | Moderator or required Discord permission | Manages the keyword whitelist and blacklist. |
| `-audioset restrictions blacklist` | — | Moderator or required Discord permission | Manages the keyword blacklist. |
| `-audioset restrictions blacklist add` | — | Moderator or required Discord permission | Adds a keyword to the blacklist. |
| `-audioset restrictions blacklist clear` | — | Moderator or required Discord permission | Clear all keywords added to the blacklist. |
| `-audioset restrictions blacklist delete` | `del`, `remove` | Moderator or required Discord permission | Removes a keyword from the blacklist. |
| `-audioset restrictions blacklist list` | — | Moderator or required Discord permission | List all keywords added to the blacklist. |
| `-audioset restrictions whitelist` | — | Moderator or required Discord permission | Manages the keyword whitelist. |
| `-audioset restrictions whitelist add` | — | Moderator or required Discord permission | Adds a keyword to the whitelist. |
| `-audioset restrictions whitelist clear` | — | Moderator or required Discord permission | Clear all keywords from the whitelist. |
| `-audioset restrictions whitelist delete` | `del`, `remove` | Moderator or required Discord permission | Removes a keyword from the whitelist. |
| `-audioset restrictions whitelist list` | — | Moderator or required Discord permission | List all keywords added to the whitelist. |
| `-audioset role` | — | Administrator or required Discord permission | Set the role to use for DJ mode. |
| `-audioset thumbnail` | — | Moderator or required Discord permission | Toggle displaying a thumbnail on audio messages. |
| `-audioset vote` | — | Moderator or required Discord permission | Percentage needed for non-mods to skip tracks, 0 to disable. |
| `-autoplay` | — | Moderator or required Discord permission | Starts auto play. |

### [Clash of Clans](../modules/coc.md) (1)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-cocset managerrole` | — | Administrator or required Discord permission | Show, set, or clear the role allowed to manage CoC settings. |

### [Cleanup](../modules/cleanup.md) (10)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-cleanup after` | — | Moderator or required Discord permission | Delete all messages after a specified message. |
| `-cleanup before` | — | Moderator or required Discord permission | Deletes X messages before the specified message. |
| `-cleanup between` | — | Moderator or required Discord permission | Delete the messages between Message One and Message Two, providing the messages IDs. |
| `-cleanup bot` | — | Moderator or required Discord permission | Clean up command messages and messages from the bot in the current channel. |
| `-cleanup duplicates` | `spam` | Moderator or required Discord permission | Deletes duplicate messages in the channel from the last X messages and keeps only one copy. |
| `-cleanup messages` | — | Moderator or required Discord permission | Delete the last X messages in the current channel. |
| `-cleanup text` | — | Moderator or required Discord permission | Delete the last X messages matching the specified text in the current channel. |
| `-cleanup user` | — | Moderator or required Discord permission | Delete the last X messages from a specified user in the current channel. |
| `-cleanupset` | — | Administrator or required Discord permission | Manage the settings for the cleanup command. |
| `-cleanupset notify` | — | Administrator or required Discord permission | Toggle clean up notification settings. |

### [Core](../modules/core.md) (15)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-ignore server` | `guild` | Administrator or required Discord permission | Ignore commands in this server. |
| `-localallowlist` | `localwhitelist` | Administrator or required Discord permission | Commands to manage the server specific allowlist. |
| `-localallowlist add` | — | Administrator or required Discord permission | Adds a user or role to the server allowlist. |
| `-localallowlist clear` | — | Administrator or required Discord permission | Clears the allowlist. |
| `-localallowlist list` | — | Administrator or required Discord permission | Lists users and roles on the server allowlist. |
| `-localallowlist remove` | — | Administrator or required Discord permission | Removes user or role from the allowlist. |
| `-localblocklist` | `localblacklist` | Administrator or required Discord permission | Commands to manage the server specific blocklist. |
| `-localblocklist add` | — | Administrator or required Discord permission | Adds a user or role to the local blocklist. |
| `-localblocklist clear` | — | Administrator or required Discord permission | Clears the server blocklist. |
| `-localblocklist list` | — | Administrator or required Discord permission | Lists users and roles on the server blocklist. |
| `-localblocklist remove` | — | Administrator or required Discord permission | Removes user or role from local blocklist. |
| `-set bot` | `metadata` | Administrator or required Discord permission | Commands for changing SickGamingBot's metadata. |
| `-set bot nickname` | — | Administrator or required Discord permission | Sets SickGamingBot's nickname for the current server. |
| `-set serverprefix` | `serverprefixes` | Administrator or required Discord permission | Sets SickGamingBot's server prefix(es). |
| `-unignore server` | `guild` | Administrator or required Discord permission | Remove this server from the ignore list. |

### [Custom Commands](../modules/customcom.md) (6)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-customcom cooldown` | — | Moderator or required Discord permission | Set, edit, or view the cooldown for a custom command. |
| `-customcom create` | `add` | Moderator or required Discord permission | Create custom commands. |
| `-customcom create random` | — | Moderator or required Discord permission | Create a CC where it will randomly choose a response! |
| `-customcom create simple` | — | Moderator or required Discord permission | Add a simple custom command. |
| `-customcom delete` | `del`, `remove` | Moderator or required Discord permission | Delete a custom command. |
| `-customcom edit` | — | Moderator or required Discord permission | Edit a custom command. |

### [DayZ](../modules/dayz.md) (12)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-dayzset` | — | Administrator or required Discord permission | Configure official DayZ announcements. |
| `-dayzset autopost` | — | Administrator or required Discord permission | Control automatic DayZ announcement posting. |
| `-dayzset autopost start` | — | Administrator or required Discord permission | Start automatic posting, optionally backfilling 2 to 10 matching posts. |
| `-dayzset autopost stop` | — | Administrator or required Discord permission | Stop automatic DayZ announcement posting. |
| `-dayzset categories` | — | Administrator or required Discord permission | Set content filters; hotfixes means posts explicitly named as hotfixes, not Steam Regular Updates. |
| `-dayzset channel` | — | Administrator or required Discord permission | Set the announcement channel; omit it to disable and clear the channel. |
| `-dayzset check` | — | Administrator or required Discord permission | Check Steam now and publish any new matching announcements. |
| `-dayzset interval` | — | Administrator or required Discord permission | Set how often Steam is checked, from 5 to 1440 minutes. |
| `-dayzset mode` | — | Administrator or required Discord permission | Choose card embeds or article-style posts with trailer and image gallery. |
| `-dayzset preview` | — | Administrator or required Discord permission | Preview the latest official announcement without changing delivery state. |
| `-dayzset role` | — | Administrator or required Discord permission | Set the optional role mentioned for matching announcements; omit to clear. |
| `-dayzset status` | — | Administrator or required Discord permission | No short description is declared. |

### [Economy](../modules/economy.md) (9)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-bank set` | — | Administrator or required Discord permission | Set the balance of a user's bank account. |
| `-economyset` | — | Administrator or required Discord permission | Base command to manage Economy settings. |
| `-economyset paydayamount` | — | Administrator or required Discord permission | Set the amount earned each payday. |
| `-economyset paydaytime` | — | Administrator or required Discord permission | Set the cooldown for the payday command. |
| `-economyset rolepaydayamount` | — | Administrator or required Discord permission | Set the amount earned each payday for a role. |
| `-economyset showsettings` | — | Administrator or required Discord permission | Shows the current economy settings |
| `-economyset slotmax` | — | Administrator or required Discord permission | Set the maximum slot machine bid. |
| `-economyset slotmin` | — | Administrator or required Discord permission | Set the minimum slot machine bid. |
| `-economyset slottime` | — | Administrator or required Discord permission | Set the cooldown for the slot machine. |

### [Filter](../modules/filter.md) (14)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-filter` | — | Moderator or required Discord permission | Base command to add or remove words from the server filter. |
| `-filter add` | — | Moderator or required Discord permission | Add words to the filter. |
| `-filter channel` | — | Moderator or required Discord permission | Base command to add or remove words from the channel filter. |
| `-filter channel add` | — | Moderator or required Discord permission | Add words to the filter. |
| `-filter channel clear` | — | Moderator or required Discord permission | Clears this channel's filter list. |
| `-filter channel delete` | `del`, `remove` | Moderator or required Discord permission | Remove words from the filter. |
| `-filter channel list` | — | Moderator or required Discord permission | Send a list of the channel's filtered words. |
| `-filter clear` | — | Moderator or required Discord permission | Clears this server's filter list. |
| `-filter delete` | `del`, `remove` | Moderator or required Discord permission | Remove words from the filter. |
| `-filter list` | — | Moderator or required Discord permission | Send a list of this server's filtered words. |
| `-filter names` | — | Moderator or required Discord permission | Toggle name and nickname filtering. |
| `-filterset` | — | Administrator or required Discord permission | Base command to manage filter settings. |
| `-filterset ban` | — | Administrator or required Discord permission | Set the filter's autoban conditions. |
| `-filterset defaultname` | — | Administrator or required Discord permission | Set the nickname for users with a filtered name. |

### [Game Roles](../modules/gameroles.md) (8)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-gameroleset` | — | Administrator or required Discord permission | Configure delegated game-role profiles. |
| `-gameroleset allow` | — | Administrator or required Discord permission | Configure roles that delegated managers may add or remove. |
| `-gameroleset allow add` | — | Administrator or required Discord permission | Approve a role for delegated management in one game profile. |
| `-gameroleset allow remove` | `delete` | Administrator or required Discord permission | Remove a role from one game's approved list. |
| `-gameroleset manager` | — | Administrator or required Discord permission | Configure roles allowed to manage one game's approved roles. |
| `-gameroleset manager add` | — | Administrator or required Discord permission | Allow a role to manage one game profile. |
| `-gameroleset manager remove` | `delete` | Administrator or required Discord permission | Remove a delegated manager role from one game profile. |
| `-gameroleset show` | `status` | Administrator or required Discord permission | Show the configured manager and member roles for a game. |

### [Garry's Mod](../modules/gmod.md) (16)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-gmodset` | — | Administrator or required Discord permission | Configure Garry's Mod status and Steam announcements. |
| `-gmodset add` | — | Administrator or required Discord permission | Add or replace a named GMod server after a successful safe query. |
| `-gmodset default` | — | Administrator or required Discord permission | Choose the default server used by public GMod commands. |
| `-gmodset info` | `status` | Administrator or required Discord permission | Show current GMod server-monitoring and Steam-update settings. |
| `-gmodset monitoring` | — | Administrator or required Discord permission | Start or stop server outage/recovery monitoring. |
| `-gmodset remove` | — | Administrator or required Discord permission | Remove a configured GMod server. |
| `-gmodset statuschannel` | — | Administrator or required Discord permission | Set the outage/recovery channel; omit it to stop monitoring and clear it. |
| `-gmodset statusinterval` | — | Administrator or required Discord permission | Set the server-status polling interval from 5 to 1,440 minutes. |
| `-gmodset statusrole` | — | Administrator or required Discord permission | Set the optional role mentioned for status changes; omit it to clear. |
| `-gmodset updates` | — | Administrator or required Discord permission | Show whether automatic official Steam-news posting is running. |
| `-gmodset updates start` | — | Administrator or required Discord permission | Start automatic posting, optionally backfilling 2 to 10 recent posts. |
| `-gmodset updates stop` | — | Administrator or required Discord permission | Stop automatic official Steam-news posting. |
| `-gmodset updateschannel` | — | Administrator or required Discord permission | Set the Steam-news channel; omit it to stop posting and clear it. |
| `-gmodset updatescheck` | — | Administrator or required Discord permission | Check Steam now and publish any unseen official announcements. |
| `-gmodset updatesinterval` | — | Administrator or required Discord permission | Set the Steam-news polling interval from 5 to 1,440 minutes. |
| `-gmodset updatesrole` | — | Administrator or required Discord permission | Set the optional role mentioned for new Steam posts; omit it to clear. |

### [Giveaways](../modules/giveaways.md) (11)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-giveaway` | `giveaways`, `gw` | Required Discord permission | Manage the giveaway system |
| `-giveaway advanced` | `adv` | Required Discord permission | Advanced creation of Giveaways. |
| `-giveaway cancel` | — | Required Discord permission | Cancel an active giveaway without drawing a winner. |
| `-giveaway edit` | — | Required Discord permission | Edit the supported settings of an active giveaway. |
| `-giveaway end` | — | Required Discord permission | End a giveaway. |
| `-giveaway entrants` | — | Required Discord permission | List all entrants for a giveaway. |
| `-giveaway explain` | — | Required Discord permission | Explanation of giveaway advanced and the arguements it supports. |
| `-giveaway info` | — | Required Discord permission | Information about a giveaway. |
| `-giveaway list` | — | Required Discord permission | List all giveaways in the server. |
| `-giveaway reroll` | — | Required Discord permission | Reroll a giveaway. |
| `-giveaway start` | — | Required Discord permission | Start a giveaway. |

### [Icarus](../modules/icarus.md) (12)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-icarusset` | — | Administrator or required Discord permission | Configure official Icarus announcements. |
| `-icarusset autopost` | — | Administrator or required Discord permission | Control automatic Icarus announcement posting. |
| `-icarusset autopost start` | — | Administrator or required Discord permission | Start automatic posting, optionally backfilling 2 to 10 matching posts. |
| `-icarusset autopost stop` | — | Administrator or required Discord permission | Stop automatic Icarus announcement posting. |
| `-icarusset categories` | — | Administrator or required Discord permission | Set content filters; hotfixes means posts explicitly named as hotfixes, not Steam Regular Updates. |
| `-icarusset channel` | — | Administrator or required Discord permission | Set the announcement channel; omit it to disable and clear the channel. |
| `-icarusset check` | — | Administrator or required Discord permission | Check Steam now and publish any new matching announcements. |
| `-icarusset interval` | — | Administrator or required Discord permission | Set how often Steam is checked, from 5 to 1440 minutes. |
| `-icarusset mode` | — | Administrator or required Discord permission | Choose card embeds or article-style posts with trailer and image gallery. |
| `-icarusset preview` | — | Administrator or required Discord permission | Preview the latest official announcement without changing delivery state. |
| `-icarusset role` | — | Administrator or required Discord permission | Set the optional role mentioned for matching announcements; omit to clear. |
| `-icarusset status` | — | Administrator or required Discord permission | No short description is declared. |

### [Meme](../modules/meme.md) (10)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-memeset` | — | Administrator or required Discord permission | Configure automatic meme feeds. |
| `-memeset autopost` | — | Administrator or required Discord permission | Set or toggle a Meme API subreddit feed. |
| `-memeset autopost off` | `disable`, `remove` | Administrator or required Discord permission | Remove a Meme API feed by destination and subreddit source. |
| `-memeset autopost status` | `list` | Administrator or required Discord permission | Show Meme API feed IDs, sources, destinations, intervals, and state. |
| `-memeset feed` | — | Administrator or required Discord permission | Manage automatic meme feeds. |
| `-memeset feed add` | — | Administrator or required Discord permission | Add an advanced scheduled feed. |
| `-memeset feed list` | — | Administrator or required Discord permission | List configured feeds. |
| `-memeset feed remove` | `delete` | Administrator or required Discord permission | Remove a feed by ID. |
| `-memeset gifpost` | — | Administrator or required Discord permission | Automatically post animated Imgur results to a channel. |
| `-memeset notifications` | `notify` | Administrator or required Discord permission | Choose silent or normal delivery for automatic meme feeds. |

### [Moderation](../modules/mod.md) (10)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-ban` | — | Administrator or required Discord permission | Ban a user from this server and optionally delete days of messages. |
| `-kick` | — | Administrator or required Discord permission | Kick a user. |
| `-massban` | `hackban` | Administrator or required Discord permission | Mass bans user(s) from the server. |
| `-rename` | — | Administrator or required Discord permission | Change a member's server nickname. |
| `-softban` | — | Administrator or required Discord permission | Kick a user and delete 1 day's worth of their messages. |
| `-tempban` | — | Administrator or required Discord permission | Temporarily ban a user from this server. |
| `-unban` | — | Administrator or required Discord permission | Unban a user from this server. |
| `-voiceban` | — | Administrator or required Discord permission | Ban a user from speaking and listening in the server's voice channels. |
| `-voicekick` | — | Moderator or required Discord permission | Kick a member from a voice channel. |
| `-voiceunban` | — | Administrator or required Discord permission | Unban a user from speaking and listening in the server's voice channels. |

### [Movie Releases](../modules/movies.md) (14)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-movieset` | `moviereleaseset` | Moderator or required Discord permission | Configure new movie release announcements. |
| `-movieset channel` | — | Moderator or required Discord permission | Set the channel that receives movie release posts. Defaults to this channel. |
| `-movieset clearhistory` | — | Moderator or required Discord permission | Clear remembered movie IDs so releases can be posted again. |
| `-movieset disable` | `disabled` | Moderator or required Discord permission | Disable hourly automatic movie release posts. |
| `-movieset enable` | `enabled` | Moderator or required Discord permission | Enable hourly automatic movie release posts. |
| `-movieset force` | — | Moderator or required Discord permission | Check now and post the next unposted release even if scheduled posting is disabled. |
| `-movieset maxperday` | — | Moderator or required Discord permission | Set the maximum automatic release posts per day. |
| `-movieset minvotes` | — | Moderator or required Discord permission | Set the minimum TMDb vote count required before posting a movie. |
| `-movieset notifications` | `notify` | Moderator or required Discord permission | Choose silent or normal delivery for automatic movie posts. |
| `-movieset preview` | — | Moderator or required Discord permission | Preview matching TMDb releases without posting them. |
| `-movieset role` | — | Moderator or required Discord permission | Set the role mentioned by automatic movie release announcements. |
| `-movieset roleclear` | `clearrole` | Moderator or required Discord permission | Stop mentioning a notification role in automatic release posts. |
| `-movieset settings` | — | Moderator or required Discord permission | Show current movie release settings. |
| `-movieset window` | — | Moderator or required Discord permission | Set the release date window checked by the cog. |

### [Mutes](../modules/mutes.md) (14)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-activemutes` | — | Moderator or required Discord permission | Displays active mutes on this server. |
| `-forceunmute` | — | Moderator or required Discord permission | Force Unmute users who have had channel overwrite mutes in every channel. |
| `-mute` | — | Moderator or required Discord permission | Mute users. |
| `-mutechannel` | `channelmute` | Moderator or required Discord permission | Mute a user in the current text channel (or in the parent of the current thread). |
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

### [Navidrome](../modules/navidrome.md) (22)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
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

### [Pokémon](../modules/pokemon.md) (23)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-pokemonset` | `pkmnset`, `pokeset` | Administrator or required Discord permission | Configure Pokémon without cluttering player commands. |
| `-pokemonset battleexpiry` | — | Administrator or required Discord permission | Set the server battle time limit. |
| `-pokemonset center` | — | Administrator or required Discord permission | Designate the server Pokémon Center. |
| `-pokemonset channel` | — | Administrator or required Discord permission | Enable wild encounters in a channel. |
| `-pokemonset clear` | — | Administrator or required Discord permission | End the encounter in this channel, or the server’s only encounter. |
| `-pokemonset concurrency` | `slots` | Administrator or required Discord permission | Set this server’s simultaneous encounters within the bot limit. |
| `-pokemonset cooldown` | — | Administrator or required Discord permission | Set a slower custom spawn cooldown. |
| `-pokemonset disable` | — | Administrator or required Discord permission | Disable wild encounters in this server. |
| `-pokemonset encountertime` | — | Administrator or required Discord permission | Set or inherit this server's wild encounter lifetime. |
| `-pokemonset expiredcards` | `missedcards` | Administrator or required Discord permission | Delete expired wild cards or keep their dimmed result. |
| `-pokemonset generations` | — | Administrator or required Discord permission | Choose from bot-enabled generations. |
| `-pokemonset mode` | — | Administrator or required Discord permission | Choose timed spawning or the optional activity system. |
| `-pokemonset notificationrole` | `alertrole` | Administrator or required Discord permission | Set or clear the opt-in encounter alert role. |
| `-pokemonset notifications` | `notify` | Administrator or required Discord permission | Choose silent, normal, or opt-in-role encounter alerts. |
| `-pokemonset pace` | — | Administrator or required Discord permission | Choose a preset encounter pace. |
| `-pokemonset profile` | — | Administrator or required Discord permission | Apply an Active, Balanced, or Relaxed server profile. |
| `-pokemonset quiethours` | — | Administrator or required Discord permission | Set local quiet hours or disable them with `off`. |
| `-pokemonset removecenter` | — | Administrator or required Discord permission | Remove the server Pokémon Center. |
| `-pokemonset removechannel` | — | Administrator or required Discord permission | Stop wild encounters in a channel. |
| `-pokemonset spawn` | — | Administrator or required Discord permission | Trigger a test encounter; bot owners may use `shiny`. |
| `-pokemonset status` | `settings` | Administrator or required Discord permission | Show channels, schedule, and effective server settings. |
| `-pokemonset threshold` | — | Administrator or required Discord permission | Set a slower custom activity threshold. |
| `-pokemonset timer` | — | Administrator or required Discord permission | Set this server’s jittered timer within the bot-owner floor. |

### [RSS Publisher](../modules/rsspublisher.md) (35)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-rsspublisher` | `rss` | Moderator or required Discord permission | Manage this server's RSS and Atom feeds. |
| `-rsspublisher add` | — | Moderator or required Discord permission | Add a feed. |
| `-rsspublisher announce` | `announcement` | Moderator or required Discord permission | Set announcement text. |
| `-rsspublisher embed` | — | Moderator or required Discord permission | Configure feed embeds. |
| `-rsspublisher embed color` | `colour` | Moderator or required Discord permission | Set an embed color for a feed. |
| `-rsspublisher embed image` | — | Moderator or required Discord permission | Set a tag to be a large embed image. |
| `-rsspublisher embed thumbnail` | — | Moderator or required Discord permission | Set a tag to be a thumbnail image. |
| `-rsspublisher embed toggle` | — | Moderator or required Discord permission | Toggle whether a feed is sent in an embed or not. |
| `-rsspublisher filter` | — | Moderator or required Discord permission | Filter entries by title or author. |
| `-rsspublisher filter author` | — | Moderator or required Discord permission | Manage the exact author allowlist. |
| `-rsspublisher filter author allow` | `add` | Moderator or required Discord permission | Allow an exact author name after plaintext normalization. |
| `-rsspublisher filter author list` | — | Moderator or required Discord permission | List exact allowed authors for a feed. |
| `-rsspublisher filter author remove` | `delete` | Moderator or required Discord permission | Remove an exact author from the allowlist. |
| `-rsspublisher filter show` | — | Moderator or required Discord permission | Show active title, author, and tag filters for a feed. |
| `-rsspublisher filter titleprefix` | `title` | Moderator or required Discord permission | Set a case-insensitive title prefix; use `clear` to remove it. |
| `-rsspublisher find` | — | Moderator or required Discord permission | Find feeds on a website. |
| `-rsspublisher force` | `preview`, `test` | Moderator or required Discord permission | Preview the newest entry. |
| `-rsspublisher limit` | — | Moderator or required Discord permission | Set the post length limit. |
| `-rsspublisher list` | — | Moderator or required Discord permission | List feeds in one channel. |
| `-rsspublisher listall` | — | Moderator or required Discord permission | List every server feed. |
| `-rsspublisher listtags` | — | Moderator or required Discord permission | List available feed tags. |
| `-rsspublisher mode` | — | Moderator or required Discord permission | Set latest or catch-up mode. |
| `-rsspublisher pause` | — | Moderator or required Discord permission | Pause a feed. |
| `-rsspublisher remove` | `del`, `delete` | Moderator or required Discord permission | Remove a feed. |
| `-rsspublisher resume` | — | Moderator or required Discord permission | Resume a feed. |
| `-rsspublisher showtemplate` | — | Moderator or required Discord permission | Show a feed template. |
| `-rsspublisher status` | — | Moderator or required Discord permission | Show feed health. |
| `-rsspublisher tag` | — | Moderator or required Discord permission | Manage tag filters. |
| `-rsspublisher tag allow` | — | Moderator or required Discord permission | Set an allowed tag for a feed to be posted. The tag must match exactly (without regard to title casing). |
| `-rsspublisher tag allowlist` | — | Moderator or required Discord permission | List allowed tags for feed post qualification. |
| `-rsspublisher tag remove` | `delete` | Moderator or required Discord permission | Remove a tag from the allow list. The tag must match exactly (without regard to title casing). |
| `-rsspublisher template` | — | Moderator or required Discord permission | Set a feed template. |
| `-rsspublisher version` | — | Moderator or required Discord permission | Show the RSS version. |
| `-rsspublisher view` | `info`, `settings` | Moderator or required Discord permission | View one feed's settings. |
| `-rsspublisher viewtags` | — | Moderator or required Discord permission | Preview rendered tag values. |

### [Reports](../modules/reports.md) (4)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-report interact` | — | Moderator or required Discord permission | Open a message tunnel. |
| `-reportset` | — | Administrator or required Discord permission | Manage Reports. |
| `-reportset output` | — | Administrator or required Discord permission | Set the channel where reports will be sent. |
| `-reportset toggle` | `toggleactive` | Administrator or required Discord permission | Enable or disable reporting for this server. |

### [Rocket League](../modules/rocketleague.md) (28)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-rlcsset` | — | Administrator or required Discord permission | Admin: configure automatic RLCS schedule announcements. |
| `-rlcsset channel` | — | Administrator or required Discord permission | Enable schedule updates in a channel. |
| `-rlcsset disable` | — | Administrator or required Discord permission | Disable automatic schedule updates for this server. |
| `-rlcsset postnow` | — | Administrator or required Discord permission | Post the current cached schedule without scraping BLAST. |
| `-rlcsset status` | — | Administrator or required Discord permission | Show announcement and weekly cache status. |
| `-rocketleagueset` | `rlset` | Administrator or required Discord permission | Admin: configure server-specific tournaments and automatic clips. |
| `-rocketleagueset clips` | `clip` | Administrator or required Discord permission | Admin: configure automatic short Rocket League clips. |
| `-rocketleagueset clips channel` | — | Administrator or required Discord permission | Choose the channel for automatic clip posts. |
| `-rocketleagueset clips disable` | — | Administrator or required Discord permission | Disable automatic clip posts without removing settings. |
| `-rocketleagueset clips enable` | — | Administrator or required Discord permission | Enable automatic random clip posts. |
| `-rocketleagueset clips interval` | — | Administrator or required Discord permission | Set the approximate posting interval in hours (1-168). |
| `-rocketleagueset clips maxlength` | — | Administrator or required Discord permission | Set the longest eligible clip in seconds (15-600). |
| `-rocketleagueset clips notifications` | `notify` | Administrator or required Discord permission | Choose silent or normal delivery for automatic clip posts. |
| `-rocketleagueset clips postnow` | — | Administrator or required Discord permission | Post one unseen eligible clip in the configured channel now. |
| `-rocketleagueset clips refresh` | — | Administrator or required Discord permission | Refresh all configured clip-source caches now. |
| `-rocketleagueset clips sourceadd` | — | Administrator or required Discord permission | Add a Medal, Twitch, or YouTube source by URL or provider and name. |
| `-rocketleagueset clips sourceremove` | — | Administrator or required Discord permission | Remove a configured clip source by its server ID. |
| `-rocketleagueset clips sources` | — | Administrator or required Discord permission | List configured clip sources and their removal IDs. |
| `-rocketleagueset clips status` | — | Administrator or required Discord permission | Show this server's automatic clip settings. |
| `-rocketleagueset leagueadd` | — | Administrator or required Discord permission | Subscribe this server to a complete start.gg league URL. |
| `-rocketleagueset leaguedisable` | — | Administrator or required Discord permission | Disable automatic refresh and display for a league subscription. |
| `-rocketleagueset leaguerefresh` | — | Administrator or required Discord permission | Refresh one league subscription by ID, or every subscription. |
| `-rocketleagueset leagueremove` | — | Administrator or required Discord permission | Remove a start.gg league subscription and its cached tournaments. |
| `-rocketleagueset leagues` | — | Administrator or required Discord permission | List this server's start.gg league subscriptions. |
| `-rocketleagueset tournamentadd` | — | Administrator or required Discord permission | Validate, cache, and add a start.gg or Challonge tournament URL. |
| `-rocketleagueset tournamentrefresh` | — | Administrator or required Discord permission | Refresh one cached tournament by ID, or every configured tournament. |
| `-rocketleagueset tournamentremove` | — | Administrator or required Discord permission | Remove a configured tournament by its short ID or original URL. |
| `-rocketleagueset tournaments` | — | Administrator or required Discord permission | List cached tournaments, IDs, and removal instructions. |

### [Role Tools](../modules/roletools.md) (89)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-roletools adminhelp` | `setuphelp` | Administrator or required Discord permission | Manager command guide. |
| `-roletools atomic` | — | Administrator or required Discord permission | Configure safe role changes. |
| `-roletools autorole` | `auto` | Administrator or required Discord permission | Configure join roles. |
| `-roletools buttons` | `button` | Administrator or required Discord permission | Manage button roles. |
| `-roletools buttons cleanup` | — | Administrator or required Discord permission | Check each button that has registered a message still exists and remove buttons with |
| `-roletools buttons create` | — | Administrator or required Discord permission | Create a role button |
| `-roletools buttons delete` | `del`, `remove` | Administrator or required Discord permission | Delete a saved button. |
| `-roletools buttons view` | — | Administrator or required Discord permission | View current buttons setup for role assign in this server. |
| `-roletools cost` | — | Administrator or required Discord permission | Set a role Bank cost. |
| `-roletools exclude add` | — | Administrator or required Discord permission | Add role exclusion (This will remove if the designated role is acquired |
| `-roletools exclude mutual` | — | Administrator or required Discord permission | Allow setting roles mutually exclusive to eachother |
| `-roletools exclude remove` | — | Administrator or required Discord permission | Remove role exclusion |
| `-roletools forcerole` | — | Administrator or required Discord permission | Force a sticky role. |
| `-roletools forceroleremove` | — | Administrator or required Discord permission | Remove a forced sticky role. |
| `-roletools giverole` | — | Administrator or required Discord permission | Give a role in bulk. |
| `-roletools group accessrole` | `gateway` | Administrator or required Discord permission | Set the group's member access role; omit the role to clear it. |
| `-roletools group archive` | — | Administrator or required Discord permission | Archive an unpublished private group. |
| `-roletools group conflicts` | — | Administrator or required Discord permission | No short description is declared. |
| `-roletools group conflicts add` | — | Administrator or required Discord permission | No short description is declared. |
| `-roletools group conflicts remove` | — | Administrator or required Discord permission | No short description is declared. |
| `-roletools group cost` | — | Administrator or required Discord permission | Set the one-time access cost; use 0 for free. |
| `-roletools group create` | — | Administrator or required Discord permission | Create a private group and its unpublished named menu. |
| `-roletools group delete` | — | Administrator or required Discord permission | Delete an unpublished private group; append `confirm`. |
| `-roletools group description` | `describe` | Administrator or required Discord permission | Set the manager/member description for a private group. |
| `-roletools group duration` | — | Administrator or required Discord permission | Set gateway access in minutes; use 0 for permanent. |
| `-roletools group publish` | — | Administrator or required Discord permission | Publish a group through private, dropdown, reactions, or role_channel layout. |
| `-roletools group required` | — | Administrator or required Discord permission | No short description is declared. |
| `-roletools group required add` | — | Administrator or required Discord permission | No short description is declared. |
| `-roletools group required mode` | — | Administrator or required Discord permission | No short description is declared. |
| `-roletools group required remove` | — | Administrator or required Discord permission | No short description is declared. |
| `-roletools group restore` | — | Administrator or required Discord permission | Restore an archived private group. |
| `-roletools group roles` | — | Administrator or required Discord permission | Add or remove private-group selectable roles. |
| `-roletools group roles add` | — | Administrator or required Discord permission | No short description is declared. |
| `-roletools group roles remove` | — | Administrator or required Discord permission | No short description is declared. |
| `-roletools include add` | — | Administrator or required Discord permission | Add role inclusion (This will add roles if the designated role is acquired |
| `-roletools include mutual` | — | Administrator or required Discord permission | Allow setting roles mutually inclusive to eachother |
| `-roletools include remove` | — | Administrator or required Discord permission | Remove role inclusion |
| `-roletools menu` | — | Administrator or required Discord permission | Manage published role menus. |
| `-roletools menu add` | — | Administrator or required Discord permission | Add shared-catalog roles to a saved menu. |
| `-roletools menu archive` | — | Administrator or required Discord permission | Archive an unpublished menu while keeping its configuration. |
| `-roletools menu create` | — | Administrator or required Discord permission | Create an unpublished named menu using roles from the shared library. |
| `-roletools menu delete` | — | Administrator or required Discord permission | Permanently delete an unpublished menu; append `confirm`. |
| `-roletools menu diagnose` | `diagnostics` | Administrator or required Discord permission | Check a menu for missing roles, messages, emoji, and permissions. |
| `-roletools menu duplicate` | — | Administrator or required Discord permission | Copy a saved menu into a new unpublished draft. |
| `-roletools menu layout` | — | Administrator or required Discord permission | Set private, dropdown, reactions, or role_channel layout. |
| `-roletools menu presentation` | — | Administrator or required Discord permission | Set `label \| description \| emoji \| group`; omit values to reset. |
| `-roletools menu preview` | — | Administrator or required Discord permission | Preview a saved menu without changing its published messages. |
| `-roletools menu publish` | — | Administrator or required Discord permission | Publish or move a saved menu using its selected layout. |
| `-roletools menu remove` | — | Administrator or required Discord permission | Remove roles from a saved menu without deleting the Discord roles. |
| `-roletools menu restore` | — | Administrator or required Discord permission | Restore an archived menu to active management. |
| `-roletools menu sync` | — | Administrator or required Discord permission | Synchronize a saved menu's published Discord messages. |
| `-roletools menu unpublish` | — | Administrator or required Discord permission | Remove published messages but keep the saved menu. |
| `-roletools menu view` | — | Administrator or required Discord permission | Show one saved menu's roles, layout, and destination. |
| `-roletools notify` | `notifications` | Administrator or required Discord permission | Configure role notices. |
| `-roletools notify channel` | — | Administrator or required Discord permission | Send successful member role-change notices to this channel. |
| `-roletools notify disable` | `clear`, `off` | Administrator or required Discord permission | Disable public RoleTools role-change notices for this server. |
| `-roletools picker` | — | Administrator or required Discord permission | Create and maintain scalable self-role picker cards. |
| `-roletools picker add` | — | Administrator or required Discord permission | Add one or more roles to a picker without rebuilding it. |
| `-roletools picker create` | — | Administrator or required Discord permission | Create and publish a managed role picker card. |
| `-roletools picker delete` | — | Administrator or required Discord permission | Delete a picker configuration and remove its published card. |
| `-roletools picker move` | — | Administrator or required Discord permission | Move a picker role to a one-based position and switch to manual ordering. |
| `-roletools picker remove` | — | Administrator or required Discord permission | Remove one or more roles from a picker without deleting the Discord roles. |
| `-roletools picker replace` | — | Administrator or required Discord permission | Replace a picker role in place while retaining its position. |
| `-roletools picker sort` | — | Administrator or required Discord permission | Sort a picker alphabetically or retain manual order. |
| `-roletools picker sync` | — | Administrator or required Discord permission | Refresh a published picker card from its saved configuration. |
| `-roletools picker view` | — | Administrator or required Discord permission | Show a picker's saved roles and published message. |
| `-roletools reaction bulk` | `bulkcreate`, `bulkmake` | Administrator or required Discord permission | Create multiple roles reactions for a single message |
| `-roletools reaction cleanup` | — | Administrator or required Discord permission | Cleanup old/missing reaction roles and settings. |
| `-roletools reaction clearreact` | `clearreacts` | Administrator or required Discord permission | Clear the reactions for reaction roles. This will remove |
| `-roletools reaction create` | `make`, `setup` | Administrator or required Discord permission | Create a reaction role |
| `-roletools reaction reactroles` | `reactionroles`, `reactrole` | Administrator or required Discord permission | View current bound roles in the server |
| `-roletools reaction remove` | `rem` | Administrator or required Discord permission | Remove a reaction role |
| `-roletools removerole` | — | Administrator or required Discord permission | Remove a role in bulk. |
| `-roletools required add` | — | Administrator or required Discord permission | Add role requirements |
| `-roletools required any` | — | Administrator or required Discord permission | Set the required roles to require any of the roles instead of all of them |
| `-roletools required remove` | — | Administrator or required Discord permission | Remove role requirements |
| `-roletools select` | `selects` | Administrator or required Discord permission | Manage dropdown roles. |
| `-roletools select cleanup` | — | Administrator or required Discord permission | Check each select menu that has registered a message still exists and remove buttons with |
| `-roletools select create` | — | Administrator or required Discord permission | Create a select menu |
| `-roletools select createoption` | `addoption` | Administrator or required Discord permission | Create a select menu option |
| `-roletools select delete` | `del`, `remove` | Administrator or required Discord permission | Delete a saved select menu. |
| `-roletools select deleteoption` | `deloption`, `remoption`, `removeoption` | Administrator or required Discord permission | Delete a saved option. |
| `-roletools select view` | `list` | Administrator or required Discord permission | View current select menus setup for role assign in this server. |
| `-roletools select viewoptions` | `listoption`, `listoptions`, `viewoption` | Administrator or required Discord permission | View current select menus setup for role assign in this server. |
| `-roletools selfassignable` | `selfadd`, `selfassign` | Administrator or required Discord permission | Allow self-assignment. |
| `-roletools selfremovable` | `selfrem` | Administrator or required Discord permission | Allow self-removal. |
| `-roletools setup` | — | Administrator or required Discord permission | Open interactive setup. |
| `-roletools sticky` | — | Administrator or required Discord permission | Configure sticky roles. |
| `-roletools temporary set` | — | Administrator or required Discord permission | Set the duration the role will last before being removed. |

### [Streams](../modules/streams.md) (20)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
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
| `-streamset usebuttons` | — | Moderator or required Discord permission | Toggle whether to use buttons for stream alerts. |

### [Trivia](../modules/trivia.md) (10)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-triviaset` | — | Moderator or required Discord permission | Manage Trivia settings. |
| `-triviaset botplays` | — | Moderator or required Discord permission | Set whether or not the bot gains points. |
| `-triviaset maxscore` | — | Moderator or required Discord permission | Set the total points required to win. |
| `-triviaset override` | — | Moderator or required Discord permission | Allow/disallow trivia lists to override settings. |
| `-triviaset payout` | — | Administrator or required Discord permission | Set the payout multiplier. |
| `-triviaset revealanswer` | — | Moderator or required Discord permission | Set whether or not the answer is revealed. |
| `-triviaset showsettings` | — | Moderator or required Discord permission | Show the current trivia settings. |
| `-triviaset stopafter` | — | Moderator or required Discord permission | Set how long until trivia stops due to no response. |
| `-triviaset timelimit` | — | Moderator or required Discord permission | Set the maximum seconds permitted to answer a question. |
| `-triviaset usespoilers` | — | Moderator or required Discord permission | Set if bot will display the answers in spoilers. |

### [Warnings](../modules/warnings.md) (5)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-actionlist` | — | Administrator or required Discord permission | List all configured automated actions for Warnings. |
| `-reasonlist` | — | Administrator or required Discord permission | List all configured reasons for Warnings. |
| `-unwarn` | — | Administrator or required Discord permission | Remove a warning from a user. |
| `-warn` | — | Administrator or required Discord permission | Warn the user for the specified reason. |
| `-warnings` | — | Administrator | List the warnings for the specified user. |

### [Welcome](../modules/welcome.md) (45)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-welcomeset` | — | Administrator or required Discord permission | Sets welcome module settings |
| `-welcomeset bot` | — | Administrator or required Discord permission | Special greeting for bots. |
| `-welcomeset bot goodbyemsg` | `goodbyemessage` | Administrator or required Discord permission | Set the goodbye msg for bots. |
| `-welcomeset bot msg` | — | Administrator or required Discord permission | Set the greeting msg for bots. |
| `-welcomeset bot role` | — | Administrator or required Discord permission | Set the role to put bots in when they join. |
| `-welcomeset bot test` | — | Administrator or required Discord permission | Test the bot joining message |
| `-welcomeset embed` | — | Administrator or required Discord permission | Set various embed options. |
| `-welcomeset embed author` | — | Administrator or required Discord permission | Toggle the author field being filled in the embed. |
| `-welcomeset embed colour` | `color` | Administrator or required Discord permission | Set the embed colour. |
| `-welcomeset embed footer` | — | Administrator or required Discord permission | Set the embed footer. |
| `-welcomeset embed goodbyecolour` | `gcolor`, `gcolour`, `goodbyecolor` | Administrator or required Discord permission | Set the embed colour. |
| `-welcomeset embed icon` | — | Administrator or required Discord permission | Set the embed icon image. |
| `-welcomeset embed image` | — | Administrator or required Discord permission | Set embed image options. |
| `-welcomeset embed image goodbye` | — | Administrator or required Discord permission | Set the embed image link for goodbyes. |
| `-welcomeset embed image greeting` | — | Administrator or required Discord permission | Set the embed image link for greetings. |
| `-welcomeset embed mention` | — | Administrator or required Discord permission | Toggle mentioning the user when they join. |
| `-welcomeset embed thumbnail` | — | Administrator or required Discord permission | Set the embed thumbnail image. |
| `-welcomeset embed timestamp` | — | Administrator or required Discord permission | Toggle the timestamp in embeds. |
| `-welcomeset embed title` | — | Administrator or required Discord permission | Set the embed title. |
| `-welcomeset embed toggle` | — | Administrator or required Discord permission | Toggle embed messages. |
| `-welcomeset goodbye` | `leave` | Administrator or required Discord permission | Manage goodbye messages. |
| `-welcomeset goodbye add` | — | Administrator or required Discord permission | Adds a goodbye message format for the guild to be chosen at random |
| `-welcomeset goodbye allowedmentions` | — | Administrator or required Discord permission | Determine the bots allowed mentions for greetings |
| `-welcomeset goodbye channel` | — | Administrator or required Discord permission | Sets the channel to send the goodbye message. |
| `-welcomeset goodbye deleteafter` | — | Administrator or required Discord permission | Set the time after which a greeting message is deleted in seconds. |
| `-welcomeset goodbye deleteprevious` | — | Administrator or required Discord permission | Turns on/off deleting the previous greeting message when a user joins. |
| `-welcomeset goodbye list` | `del`, `delete`, `edit` | Administrator or required Discord permission | Lists the goodbye messages of this guild and allows editing the settings. |
| `-welcomeset goodbye test` | — | Administrator or required Discord permission | Test the goodbye message deleted after 60 seconds |
| `-welcomeset goodbye toggle` | — | Administrator or required Discord permission | Turns on/off sending goodbye messages to users who leave to the guild. |
| `-welcomeset greeting` | `welcome` | Administrator or required Discord permission | Manage welcome messages |
| `-welcomeset greeting add` | — | Administrator or required Discord permission | Adds a greeting message format for the guild to be chosen at random |
| `-welcomeset greeting allowedmentions` | — | Administrator or required Discord permission | Determine the bots allowed mentions for greetings |
| `-welcomeset greeting channel` | — | Administrator or required Discord permission | Sets the channel to send the greeting message. |
| `-welcomeset greeting count` | — | Administrator or required Discord permission | Turns on/off showing how many users join each day. |
| `-welcomeset greeting deleteafter` | — | Administrator or required Discord permission | Set the time after which a greeting message is deleted in seconds. |
| `-welcomeset greeting deleteprevious` | — | Administrator or required Discord permission | Turns on/off deleting the previous greeting message when a user joins. |
| `-welcomeset greeting filter` | — | Administrator or required Discord permission | Set what to do when a username matches the bots filter. |
| `-welcomeset greeting grouped` | — | Administrator or required Discord permission | Set whether to group greeting messages |
| `-welcomeset greeting list` | `del`, `delete`, `edit` | Administrator or required Discord permission | Lists the greeting messages of this guild and allows editing the settings. |
| `-welcomeset greeting minimumage` | `age` | Administrator or required Discord permission | Set the minimum number of days a user account must be to show up in the greeting message. |
| `-welcomeset greeting pending` | — | Administrator or required Discord permission | Set whether to wait for the user to pass verification to send the welcome |
| `-welcomeset greeting test` | — | Administrator or required Discord permission | Test the greeting message deleted after 60 seconds. |
| `-welcomeset greeting toggle` | — | Administrator or required Discord permission | Turns on/off welcoming new users to the guild. |
| `-welcomeset settings` | — | Administrator or required Discord permission | Show the servers welcome settings |
| `-welcomeset whisper` | — | Administrator or required Discord permission | Sets whether or not a DM is sent to the new user |
