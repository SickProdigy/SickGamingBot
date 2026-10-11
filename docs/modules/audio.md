# Audio

> Voice-channel music playback, queues, playlists, equalizer controls, and audio configuration.

## At a glance

- **Category:** Music, media, and feeds
- **Intended audience:** Members, DJs, moderators, administrators, and maintainers depending on the action.
- **Loaded package:** `audio`
- **Documented commands:** 137 commands and subcommands

## Main command families

| Command | Default access | Purpose |
| --- | --- | --- |
| `-audioset` | Member | Music configuration options. |
| `-audiostats` | Bot maintainer | Audio stats. |
| `-autoplay` | Moderator or required permission | Starts auto play. |
| `-bump` | Member | Bump a track number to the top of the queue. |
| `-bumpplay` | Member | Force play a URL or search for a track. |
| `-command_audioset_restart` | Member | See live help. |
| `-disconnect` | Member | Disconnect from the voice channel. |
| `-eq` | Member | Equalizer management. |
| `-genre` | Member | Pick a Spotify playlist from a list of categories to start playing. |
| `-llset` | Bot maintainer | `Dangerous commands` Manage Lavalink node configuration settings. |
| `-local` | Member | Local playback commands. |
| `-now` | Member | Now playing. |
| `-pause` | Member | Pause or resume a playing track. |
| `-percent` | Member | Queue percentage. |
| `-play` | Member | Play the specified track or search for a close match. |
| `-playlist` | Member | Playlist configuration options. |
| `-prev` | Member | Skip to the start of the previously played track. |
| `-queue` | Member | List the songs in the queue. |
| `-remove` | Member | Remove a specific track number from the queue. |
| `-repeat` | Member | Toggle repeat. |
| `-search` | Member | Pick a track with a search. |
| `-seek` | Member | Seek ahead or behind on a track by seconds or to a specific time. |
| `-shuffle` | Member | Toggle shuffle. |
| `-sing` | Member | Make Red sing one of her songs. |
| `-skip` | Member | Skip to the next track, or to a given track number. |
| `-stop` | Member | Stop playback and clear the queue. |
| `-summon` | Member | Summon the bot to a voice channel. |
| `-volume` | Member | Set the volume, 1% - 150%. |

## Using this module

Run help for a command family, then add subcommands to request more specific details:

```text
-help audioset
-help audioset <subcommand>
```

The bot only shows commands available to your account. Server-specific permission
rules, disabled commands, required integrations, and channel restrictions can change
what you can use.

## Learn more

- [Complete Audio command reference](../reference/audio.md)
- [Using SickGamingBot help](../using-help.md)
- [Permissions and access levels](../permissions.md)
