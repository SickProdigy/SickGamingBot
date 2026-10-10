# Audio commands

Loaded package: `audio`

Use `-help <command>` for complete syntax and argument details. Access below is
derived from declared command checks; server-specific permission rules can change it.

| Command | Aliases | Access | Description |
| --- | --- | --- | --- |
| `-audioset` | — | Member | Music configuration options. |
| `-audioset autodeafen` | — | Moderator or required Discord permission | Toggle whether the bot will be auto deafened upon joining the voice channel. |
| `-audioset autoplay` | — | Moderator or required Discord permission | Change auto-play setting. |
| `-audioset autoplay playlist` | — | Moderator or required Discord permission | Set a playlist to auto-play songs from. |
| `-audioset autoplay reset` | — | Moderator or required Discord permission | Resets auto-play to the default playlist. |
| `-audioset autoplay toggle` | — | Moderator or required Discord permission | Toggle auto-play when there no songs in queue. |
| `-audioset cache` | — | Bot maintainer | Sets the caching level. |
| `-audioset cacheage` | — | Bot maintainer | Sets the cache max age. |
| `-audioset countrycode` | — | Moderator or required Discord permission | Set the country code for Spotify searches. |
| `-audioset dailyqueue` | — | Administrator | Toggle daily queues. |
| `-audioset dc` | — | Moderator or required Discord permission | Toggle the bot auto-disconnecting when done playing. |
| `-audioset dj` | — | Administrator or required Discord permission | Toggle DJ mode. |
| `-audioset emptydisconnect` | — | Moderator or required Discord permission | Auto-disconnect from channel when bot is alone in it for x seconds, 0 to disable. |
| `-audioset emptypause` | — | Moderator or required Discord permission | Auto-pause after x seconds when room is empty, 0 to disable. |
| `-audioset globaldailyqueue` | — | Bot maintainer | Toggle global daily queues. |
| `-audioset jukebox` | — | Moderator or required Discord permission | Set a price for queueing tracks for non-mods, 0 to disable. |
| `-audioset localpath` | — | Bot maintainer | Set the localtracks path if the Lavalink.jar is not run from the Audio data folder. |
| `-audioset logs` | — | Bot maintainer | Sends the managed Lavalink node logs to your DMs. |
| `-audioset lyrics` | — | Moderator or required Discord permission | Prioritise tracks with lyrics. |
| `-audioset maxlength` | — | Moderator or required Discord permission | Max length of a track to queue in seconds, 0 to disable. |
| `-audioset maxvolume` | — | Administrator or required Discord permission | Set the maximum volume allowed in this server. |
| `-audioset mycountrycode` | — | Member | Set the country code for Spotify searches. |
| `-audioset notify` | — | Moderator or required Discord permission | Toggle track announcement and other bot messages. |
| `-audioset persistqueue` | — | Administrator | Toggle persistent queues. |
| `-audioset restart` | — | Bot maintainer | Restarts the lavalink connection. |
| `-audioset restrict` | — | Bot maintainer | Toggle the domain restriction on Audio. |
| `-audioset restrictions` | — | Moderator or required Discord permission | Manages the keyword whitelist and blacklist. |
| `-audioset restrictions blacklist` | — | Moderator or required Discord permission | Manages the keyword blacklist. |
| `-audioset restrictions blacklist add` | — | Moderator or required Discord permission | Adds a keyword to the blacklist. |
| `-audioset restrictions blacklist clear` | — | Moderator or required Discord permission | Clear all keywords added to the blacklist. |
| `-audioset restrictions blacklist delete` | `del`, `remove` | Moderator or required Discord permission | Removes a keyword from the blacklist. |
| `-audioset restrictions blacklist list` | — | Moderator or required Discord permission | List all keywords added to the blacklist. |
| `-audioset restrictions global` | — | Bot maintainer | Manages the global keyword whitelist/blacklist. |
| `-audioset restrictions global blacklist` | — | Bot maintainer | Manages the global keyword blacklist. |
| `-audioset restrictions global blacklist add` | — | Bot maintainer | Adds a keyword to the blacklist. |
| `-audioset restrictions global blacklist clear` | — | Bot maintainer | Clear all keywords added to the blacklist. |
| `-audioset restrictions global blacklist delete` | `del`, `remove` | Bot maintainer | Removes a keyword from the blacklist. |
| `-audioset restrictions global blacklist list` | — | Bot maintainer | List all keywords added to the blacklist. |
| `-audioset restrictions global whitelist` | — | Bot maintainer | Manages the global keyword whitelist. |
| `-audioset restrictions global whitelist add` | — | Bot maintainer | Adds a keyword to the whitelist. |
| `-audioset restrictions global whitelist clear` | — | Bot maintainer | Clear all keywords from the whitelist. |
| `-audioset restrictions global whitelist delete` | `del`, `remove` | Bot maintainer | Removes a keyword from the whitelist. |
| `-audioset restrictions global whitelist list` | — | Bot maintainer | List all keywords added to the whitelist. |
| `-audioset restrictions whitelist` | — | Moderator or required Discord permission | Manages the keyword whitelist. |
| `-audioset restrictions whitelist add` | — | Moderator or required Discord permission | Adds a keyword to the whitelist. |
| `-audioset restrictions whitelist clear` | — | Moderator or required Discord permission | Clear all keywords from the whitelist. |
| `-audioset restrictions whitelist delete` | `del`, `remove` | Moderator or required Discord permission | Removes a keyword from the whitelist. |
| `-audioset restrictions whitelist list` | — | Moderator or required Discord permission | List all keywords added to the whitelist. |
| `-audioset role` | — | Administrator or required Discord permission | Set the role to use for DJ mode. |
| `-audioset settings` | `info` | Member | Show the current settings. |
| `-audioset spotifyapi` | — | Bot maintainer | Instructions to set the Spotify API tokens. |
| `-audioset status` | — | Bot maintainer | Enable/disable tracks' titles as status. |
| `-audioset thumbnail` | — | Moderator or required Discord permission | Toggle displaying a thumbnail on audio messages. |
| `-audioset vote` | — | Moderator or required Discord permission | Percentage needed for non-mods to skip tracks, 0 to disable. |
| `-audioset youtubeapi` | — | Bot maintainer | Instructions to set the YouTube API key. |
| `-audiostats` | — | Bot maintainer | Audio stats. |
| `-autoplay` | — | Moderator or required Discord permission | Starts auto play. |
| `-bump` | — | Member | Bump a track number to the top of the queue. |
| `-bumpplay` | — | Member | Force play a URL or search for a track. |
| `-command_audioset_restart` | — | Member | See live help. |
| `-disconnect` | — | Member | Disconnect from the voice channel. |
| `-eq` | — | Member | Equalizer management. |
| `-eq delete` | `del`, `remove` | Member | Delete a saved eq preset. |
| `-eq list` | — | Member | List saved eq presets. |
| `-eq load` | — | Member | Load a saved eq preset. |
| `-eq reset` | — | Member | Reset the eq to 0 across all bands. |
| `-eq save` | — | Member | Save the current eq settings to a preset. |
| `-eq set` | — | Member | Set an eq band with a band number or name and value. |
| `-genre` | — | Member | Pick a Spotify playlist from a list of categories to start playing. |
| `-llset` | — | Bot maintainer | `Dangerous commands` Manage Lavalink node configuration settings. |
| `-llset config` | `conf` | Bot maintainer | Configure the managed Lavalink node runtime options. |
| `-llset config bind` | `host`, `address` | Bot maintainer | `Dangerous command` Set the managed Lavalink node's binding IP address. |
| `-llset config port` | — | Bot maintainer | `Dangerous command` Set the managed Lavalink node's connection port. |
| `-llset config server` | — | Bot maintainer | Configure the managed node authorization and connection settings. |
| `-llset config server buffer` | `b` | Bot maintainer | `Dangerous command`  Set the managed Lavalink node JDA-NAS buffer size. |
| `-llset config server framebuffer` | `fb`, `frame` | Bot maintainer | `Dangerous command` Set the managed Lavalink node framebuffer size. |
| `-llset config source` | — | Bot maintainer | `Dangerous command` Toggle audio sources on/off. |
| `-llset config source bandcamp` | `bc` | Bot maintainer | Toggle Bandcamp source on or off. |
| `-llset config source http` | — | Bot maintainer | Toggle HTTP direct URL usage on or off. |
| `-llset config source local` | — | Bot maintainer | Toggle local file usage on or off. |
| `-llset config source soundcloud` | `sc` | Bot maintainer | Toggle Soundcloud source on or off. |
| `-llset config source twitch` | — | Bot maintainer | Toggle Twitch source on or off. |
| `-llset config source vimeo` | — | Bot maintainer | Toggle Vimeo source on or off. |
| `-llset config source youtube` | `yt` | Bot maintainer | `Dangerous command` Toggle YouTube source on or off (this includes Spotify). |
| `-llset config token` | `password`, `pass` | Bot maintainer | Set the managed Lavalink node's connection password. |
| `-llset heapsize` | `hs`, `ram`, `memory` | Bot maintainer | Set the managed Lavalink node maximum heap-size. |
| `-llset host` | — | Bot maintainer | Set the Lavalink node host. |
| `-llset info` | `settings` | Bot maintainer | Display Lavalink connection settings. |
| `-llset java` | — | Bot maintainer | Change your Java executable path. |
| `-llset password` | `pass`, `token` | Bot maintainer | Set the Lavalink node password. |
| `-llset port` | — | Bot maintainer | Set the Lavalink node port. |
| `-llset reset` | — | Bot maintainer | Reset all `llset` changes back to their default values. |
| `-llset secured` | `wss` | Bot maintainer | Set the Lavalink node connection to secured. |
| `-llset unmanaged` | `external` | Bot maintainer | Toggle using external (unmanaged) Lavalink nodes - requires an existing Lavalink node for Audio to work, if enabled. |
| `-llset yaml` | `yml` | Bot maintainer | Uploads a copy of the application.yml file used by the managed Lavalink node. |
| `-local` | — | Member | Local playback commands. |
| `-local folder` | `start` | Member | Play all songs in a localtracks folder. |
| `-local play` | — | Member | Play a local track. |
| `-local search` | — | Member | Search for songs across all localtracks folders. |
| `-now` | — | Member | Now playing. |
| `-pause` | — | Member | Pause or resume a playing track. |
| `-percent` | — | Member | Queue percentage. |
| `-play` | — | Member | Play the specified track or search for a close match. |
| `-playlist` | — | Member | Playlist configuration options. |
| `-playlist append` | — | Member | Add a track URL, playlist link, or quick search to a playlist. |
| `-playlist copy` | — | Member | Copy a playlist from one scope to another. |
| `-playlist create` | — | Member | Create an empty playlist. |
| `-playlist dedupe` | — | Member | Remove duplicate tracks from a saved playlist. |
| `-playlist delete` | `del` | Member | Delete a saved playlist. |
| `-playlist download` | — | Bot maintainer | Download a copy of a playlist. |
| `-playlist info` | — | Member | Retrieve information from a saved playlist. |
| `-playlist list` | — | Member | List saved playlists. |
| `-playlist queue` | — | Member | Save the queue to a playlist. |
| `-playlist remove` | — | Member | Remove a track from a playlist by url. |
| `-playlist rename` | — | Member | Rename an existing playlist. |
| `-playlist save` | — | Member | Save a playlist from a url. |
| `-playlist start` | `play` | Member | Load a playlist into the queue. |
| `-playlist update` | — | Member | Updates all tracks in a playlist. |
| `-playlist upload` | — | Bot maintainer | Uploads a playlist file as a playlist for the bot. |
| `-prev` | — | Member | Skip to the start of the previously played track. |
| `-queue` | — | Member | List the songs in the queue. |
| `-queue clean` | — | Member | Removes songs from the queue if the requester is not in the voice channel. |
| `-queue cleanself` | — | Member | Removes all tracks you requested from the queue. |
| `-queue clear` | — | Member | Clears the queue. |
| `-queue search` | — | Member | Search the queue. |
| `-queue shuffle` | — | Member | Shuffles the queue. |
| `-remove` | — | Member | Remove a specific track number from the queue. |
| `-repeat` | — | Member | Toggle repeat. |
| `-search` | — | Member | Pick a track with a search. |
| `-seek` | — | Member | Seek ahead or behind on a track by seconds or to a specific time. |
| `-shuffle` | — | Member | Toggle shuffle. |
| `-shuffle bumped` | — | Member | Toggle bumped track shuffle. |
| `-sing` | — | Member | Make Red sing one of her songs. |
| `-skip` | — | Member | Skip to the next track, or to a given track number. |
| `-stop` | — | Member | Stop playback and clear the queue. |
| `-summon` | — | Member | Summon the bot to a voice channel. |
| `-volume` | — | Member | Set the volume, 1% - 150%. |

Live `-help` output remains authoritative for enabled state, hidden commands,
arguments, cooldowns, and server-specific access.
