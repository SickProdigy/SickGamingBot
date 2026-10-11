# Member commands

These are ordinary member and self-service command paths. Staff and server owners also retain commands available to them through the live permission system.

Use live help for current syntax and checks:

```text
-help <command>
-help <command> <subcommand>
-help <command> <subcommand> <nested-subcommand>
```

The catalog is generated from the sanitized production command inventory. Server
rules, role hierarchy, disabled commands, channel permissions, and module configuration
can further restrict availability. [Learn how to use command help](../using-help.md).

## Catalog (318 command paths)

### [ARK](../modules/ark.md) (3)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-ark` | — | Member | View the latest official ARK: Survival Ascended announcement. |
| `-ark latest` | — | Member | Show the latest official Steam announcement, optionally by category. |
| `-ark updates` | — | Member | Show 2 to 10 recent announcements as a newest-to-oldest clickable list. |

### [Administration](../modules/admin.md) (4)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-selfrole` | — | Member | Add or remove a selfrole from yourself. |
| `-selfrole add` | — | Member | Add a selfrole to yourself. |
| `-selfrole list` | — | Member | Lists all available selfroles. |
| `-selfrole remove` | — | Member | Remove a selfrole from yourself. |

### [Age-Restricted](../modules/nsfw.md) (42)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-4k` | `4K`, `fourk` | Member | Sends some 4k images from random subreddits. |
| `-ahegao` | `oface`, `ofaces` | Member | Sends some ahegao images from random subreddits. |
| `-anal` | `sodomy` | Member | Sends some anal images/gifs from random subreddits. |
| `-asianporn` | `asian` | Member | Sends some asian porn images. |
| `-ass` | `booty`, `butt` | Member | Sends some ass images from random subreddits. |
| `-bbw` | — | Member | Sends some bbw images. |
| `-bdsm` | `shibari` | Member | Sends some bdsm from random subreddits. |
| `-blackcock` | `bcock`, `bdick`, `blackcocks`, `blackdick`, `blackdicks` | Member | Sends some blackcock images from random subreddits. |
| `-blowjob` | `bjob`, `blowj`, `blowjobs`, `fellatio`, `fellation` | Member | Sends some blowjob images/gifs from random subreddits. |
| `-boobs` | `boob`, `boobies`, `breast`, `breasts`, `tits`, `titties` | Member | Sends some boobs images from random subreddits. |
| `-bottomless` | `boless` | Member | Sends some bottomless images from random subreddits. |
| `-cleandm` | — | Member | Delete a number specified of DM's from the bot. |
| `-cosplay` | — | Member | Sends some nsfw cosplay images from random subreddits. |
| `-cumshot` | `cum`, `cums`, `cumshots` | Member | Sends some cumshot images/gifs from random subreddits. |
| `-cunnilingus` | `cunni`, `pussyeating` | Member | Sends some cunnilingus images from random subreddits. |
| `-deepthroat` | `deept`, `deepthroating` | Member | Sends some deepthroat images from random subreddits. |
| `-dick` | `cock` | Member | Sends some dicks images from random subreddits. |
| `-doublepenetration` | `doublep` | Member | Sends some double penetration images/gifs from random subreddits. |
| `-ebony` | — | Member | Sends some ebony images. |
| `-facials` | `facial` | Member | Sends some facials images from random subreddits. |
| `-feet` | `feetish`, `feets` | Member | Sends some feet images from random subreddits. |
| `-femdom` | — | Member | Sends some femdom images from random subreddits. |
| `-futa` | `futanari` | Member | Sends some futa images from random subreddits. |
| `-gay` | `gayporn` | Member | Sends some gay porn from random subreddits. |
| `-gonewild` | `gwild`, `wild` | Member | Sends some gonewild images from random subreddits. |
| `-group` | `groups`, `nudegroup`, `nudegroups` | Member | Sends some groups nudes from random subreddits. |
| `-hentai` | — | Member | Sends some hentai images/gifs from Nekobot API. |
| `-lesbian` | `lesbians` | Member | Sends some lesbian gifs or images from random subreddits. |
| `-milf` | `milfs` | Member | Sends some milf images from random subreddits. |
| `-nsfwversion` | — | Member | Get the version of the installed Nsfw cog. |
| `-oral` | `oralsex` | Member | Sends some oral gifs or images from random subreddits. |
| `-porngif` | `pgif`, `prongif` | Member | Sends some porn gifs from Nekobot API. |
| `-public` | — | Member | Sends some public nude images from random subreddits. |
| `-pussy` | `puss`, `vagina` | Member | Sends some pussy nude images from random subreddits. |
| `-realgirls` | — | Member | Sends some real girls images from random subreddits. |
| `-redhead` | `ginger`, `gingers`, `redheads` | Member | Sends some red heads images from random subreddits. |
| `-rule34` | `r34` | Member | Sends some rule34 images from random subreddits. |
| `-squirt` | `squirts` | Member | Sends some squirts images from random subreddits. |
| `-thigh` | `legs`, `thighs` | Member | Sends some thighs images from random subreddits. |
| `-threesome` | `groupsex` | Member | Sends some threesome images. |
| `-trans` | `shemale`, `shemales`, `trap` | Member | Sends some trans from random subreddits. |
| `-yiff` | `yiffs` | Member | Sends some yiff images from random subreddits. |

### [Aliases](../modules/alias.md) (6)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-alias` | — | Member | Manage command aliases. |
| `-alias global` | — | Member | Manage global aliases. |
| `-alias global list` | — | Member | List the available global aliases on this bot. |
| `-alias help` | — | Member | Try to execute help for the base command of the alias. |
| `-alias list` | — | Member | List the available aliases on this server. |
| `-alias show` | — | Member | Show what command the alias executes. |

### [Audio](../modules/audio.md) (54)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-audioset` | — | Member | Music configuration options. |
| `-audioset mycountrycode` | — | Member | Set the country code for Spotify searches. |
| `-audioset settings` | `info` | Member | Show the current settings. |
| `-bump` | — | Member | Bump a track number to the top of the queue. |
| `-bumpplay` | — | Member | Force play a URL or search for a track. |
| `-disconnect` | — | Member | Disconnect from the voice channel. |
| `-eq` | — | Member | Equalizer management. |
| `-eq delete` | `del`, `remove` | Member | Delete a saved eq preset. |
| `-eq list` | — | Member | List saved eq presets. |
| `-eq load` | — | Member | Load a saved eq preset. |
| `-eq reset` | — | Member | Reset the eq to 0 across all bands. |
| `-eq save` | — | Member | Save the current eq settings to a preset. |
| `-eq set` | — | Member | Set an eq band with a band number or name and value. |
| `-genre` | — | Member | Pick a Spotify playlist from a list of categories to start playing. |
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
| `-playlist info` | — | Member | Retrieve information from a saved playlist. |
| `-playlist list` | — | Member | List saved playlists. |
| `-playlist queue` | — | Member | Save the queue to a playlist. |
| `-playlist remove` | — | Member | Remove a track from a playlist by url. |
| `-playlist rename` | — | Member | Rename an existing playlist. |
| `-playlist save` | — | Member | Save a playlist from a url. |
| `-playlist start` | `play` | Member | Load a playlist into the queue. |
| `-playlist update` | — | Member | Updates all tracks in a playlist. |
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

### [Avatar](../modules/avatar.md) (1)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-avatar` | — | Member | Return a user's avatar URL. |

### [Clash of Clans](../modules/coc.md) (21)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-coc` | `clashofclans` | Member | Show Clash of Clans clan information and war results. |
| `-coc attacks` | `attack`, `attackstatus`, `hits` | Member | Show the current war attack-status card. |
| `-coc clan` | — | Member | Look up a Clash of Clans clan by tag. |
| `-coc cwl` | — | Member | Show available rounds from a clan's currently active CWL group. |
| `-coc player` | — | Member | Look up a Clash of Clans player by tag. |
| `-coc war` | — | Member | Show a quick Clash of Clans war update. |
| `-coc warlog` | `warhistory` | Member | Show recent regular wars for a clan tag or the configured clan. |
| `-cocset` | — | Member | Configure this server's Clash of Clans integration. |
| `-cocset clan` | — | Member | Set this server's Clash of Clans clan tag. |
| `-cocset clanwarleague` | `cwl` | Member | Toggle all Clan War League notifications for this server. |
| `-cocset endwarning` | — | Member | Set how soon before war end the ending warning sends. |
| `-cocset event` | — | Member | Toggle one war notification event. |
| `-cocset mention` | — | Member | Toggle role mentions for one war notification event. |
| `-cocset notificationrole` | — | Member | Show, set, or clear the role used for war notification mentions. |
| `-cocset notifications` | — | Member | Toggle Clash of Clans war notifications for this server. |
| `-cocset notifications status` | — | Member | Show Clash of Clans war notification settings. |
| `-cocset prepwarning` | — | Member | Set how soon before battle day the preparation warning sends. |
| `-cocset raidweekend` | `capitalraid`, `raids` | Member | Toggle Clan Capital Raid Weekend start and end notifications. |
| `-cocset timezone` | — | Member | Set the timezone used for this server's war schedules. |
| `-cocset warattacks` | — | Member | Set war attack-log notifications to card or compact format. |
| `-cocset warchannel` | — | Member | Set this server's Clash of Clans war update channel. |

### [Cleanup](../modules/cleanup.md) (2)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-cleanup` | — | Member | Base command for deleting messages. |
| `-cleanup self` | — | Member | Clean up messages owned by the bot in the current channel. |

### [Core](../modules/core.md) (22)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-contact` | — | Member | Sends a message to the owner. |
| `-embedset` | — | Member | Commands for toggling embeds on or off. |
| `-embedset showsettings` | — | Member | Show the current embed settings. |
| `-embedset user` | — | Member | Sets personal embed setting for DMs. |
| `-help` | — | Member | I need somebody |
| `-ignore` | — | Member | Commands to add servers or channels to the ignore list. |
| `-ignore channel` | — | Member | Ignore commands in the channel, thread, or category. |
| `-ignore list` | — | Member | List the currently ignored servers and channels. |
| `-info` | — | Member | Shows info about SickGamingBot. |
| `-invite` | — | Member | Shows SickGamingBot's invite url. |
| `-licenseinfo` | `licenceinfo` | Member | Get info about Red's licenses. |
| `-mydata` | — | Member | Commands which interact with the data SickGamingBot has about you. |
| `-mydata 3rdparty` | — | Member | View the End User Data statements of each 3rd-party module. |
| `-mydata forgetme` | — | Member | Have SickGamingBot forget what it knows about you. |
| `-mydata getmydata` | — | Member | [Coming Soon] Get what data SickGamingBot has about you. |
| `-mydata whatdata` | — | Member | Find out what type of data SickGamingBot stores and why. |
| `-ping` | — | Member | Pong. |
| `-set` | — | Member | Commands for changing SickGamingBot's settings. |
| `-set showsettings` | — | Member | Show the current settings for SickGamingBot. |
| `-unignore` | — | Member | Commands to remove servers or channels from the ignore list. |
| `-unignore channel` | — | Member | Remove a channel, thread, or category from the ignore list. |
| `-uptime` | — | Member | Shows SickGamingBot's uptime. |

### [Custom Commands](../modules/customcom.md) (5)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-customcom` | `cc` | Member | Base command for Custom Commands management. |
| `-customcom list` | — | Member | List all available custom commands. |
| `-customcom raw` | — | Member | Get the raw response of a custom command, to get the proper markdown. |
| `-customcom search` | — | Member | Searches through custom commands, according to the query. |
| `-customcom show` | — | Member | Shows a custom command's responses and its settings. |

### [DayZ](../modules/dayz.md) (3)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-dayz` | — | Member | Browse official DayZ Steam announcements. |
| `-dayz latest` | — | Member | Show the latest official Steam announcement, optionally by category. |
| `-dayz updates` | — | Member | Show 2 to 10 recent announcements as a newest-to-oldest clickable list. |

### [Dictionary](../modules/dictionary.md) (3)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-antonym` | `ant`, `antonyms` | Member | Show antonyms for an English word. |
| `-dictionary` | `define`, `dict` | Member | Look up an English word or phrase. |
| `-synonym` | `syn`, `synonyms` | Member | Show synonyms for an English word. |

### [Downloader](../modules/downloader.md) (1)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-findcog` | — | Member | Find which cog a command comes from. |

### [Economy](../modules/economy.md) (7)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-bank` | — | Member | Base command to manage the bank. |
| `-bank balance` | — | Member | Show the user's account balance. |
| `-bank transfer` | — | Member | Transfer currency to other users. |
| `-leaderboard` | — | Member | Print the leaderboard. |
| `-payday` | — | Member | Get some free currency. |
| `-payouts` | — | Member | Show the payouts for the slot machine. |
| `-slot` | — | Member | Use the slot machine. |

### [Game Roles](../modules/gameroles.md) (3)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-gameroles` | `clanrole`, `clanroles`, `gamerole` | Member | Assign approved game roles through a dashboard or fallback commands. |
| `-gameroles add` | `assign` | Member | Add an approved game role; the optional game keeps legacy syntax working. |
| `-gameroles remove` | `rem`, `unassign` | Member | Remove an approved game role; the optional game keeps legacy syntax working. |

### [Garry's Mod](../modules/gmod.md) (5)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-gmod` | — | Member | Show Garry's Mod server status and browse official updates. |
| `-gmod connect` | — | Member | No short description is declared. |
| `-gmod servers` | — | Member | No short description is declared. |
| `-gmod status` | — | Member | No short description is declared. |
| `-gmod updates` | — | Member | Show 1 to 10 recent official Steam announcements. |

### [General](../modules/general.md) (10)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-8` | `8ball` | Member | Ask 8 ball a question. |
| `-choose` | — | Member | Choose between multiple options. |
| `-flip` | — | Member | Flip a coin... or a user. |
| `-hug` | — | Member | Because everyone likes hugs! |
| `-lmgtfy` | — | Member | Create a lmgtfy link. |
| `-roll` | — | Member | Roll a random number. |
| `-rps` | — | Member | Play Rock Paper Scissors. |
| `-serverinfo` | — | Member | Show server information. |
| `-stopwatch` | `sw` | Member | Start or stop the stopwatch. |
| `-urban` | — | Member | Search the Urban Dictionary. |

### [Icarus](../modules/icarus.md) (3)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-icarus` | — | Member | Browse official Icarus Steam announcements. |
| `-icarus latest` | — | Member | Show the latest official Steam announcement, optionally by category. |
| `-icarus updates` | — | Member | Show 2 to 10 recent announcements as a newest-to-oldest clickable list. |

### [Image](../modules/image.md) (5)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-gif` | — | Member | Retrieve the first search result from Giphy. |
| `-gifr` | — | Member | Retrieve a random GIF from a Giphy search. |
| `-imgur` | — | Member | Retrieve pictures from Imgur. |
| `-imgur search` | — | Member | Search Imgur for the specified term. |
| `-imgur subreddit` | — | Member | Get images from a subreddit. |

### [Meme](../modules/meme.md) (11)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-meme` | `memes` | Member | Post or search for online memes and GIFs. |
| `-meme community` | `reddit` | Member | Get a random Meme API result from a subreddit. |
| `-meme gif` | `imgurgif` | Member | Post an animated Imgur result, optionally searching by query. |
| `-meme imgur` | — | Member | Post a random public Imgur result, optionally searching by query. |
| `-meme search` | — | Member | Search public Imgur posts by title and tags. |
| `-meme sources` | — | Member | Show online providers and configuration status. |
| `-memeify` | `imgflip` | Member | Create a meme: `memeify <template> <top> \| <bottom>`. |
| `-memeify avatar` | — | Member | Create a meme using a member's displayed avatar. |
| `-memeify image` | `attachment`, `photo` | Member | Caption an attached image: `memeify image <top> \| <bottom>`. |
| `-memeify list` | `templates` | Member | List bundled meme templates. |
| `-memeversion` | — | Member | Show the installed Meme cog version. |

### [Moderation](../modules/mod.md) (3)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-names` | — | Member | Show previous usernames, global display names, and server nicknames of a member. |
| `-slowmode` | — | Member | Changes thread's or text channel's slowmode setting. |
| `-userinfo` | — | Member | Show information about a member. |

### [Moderation Log](../modules/modlog.md) (4)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-case` | — | Member | Show the specified case. |
| `-casesfor` | — | Member | Display cases for the specified member. |
| `-listcases` | — | Member | List cases for the specified member. |
| `-reason` | — | Member | Specify a reason for a modlog case. |

### [Movie Releases](../modules/movies.md) (1)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-movies` | `movie`, `moviereleases` | Member | Search for a movie by title, or show movie suggestions. |

### [Mutes](../modules/mutes.md) (3)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-muteset` | — | Member | Mute settings. |
| `-voicemute` | — | Member | Mute a user in their current voice channel. |
| `-voiceunmute` | — | Member | Unmute a user in their current voice channel. |

### [Navidrome](../modules/navidrome.md) (4)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-navidrome` | — | Member | Show this server's Navidrome library information. |
| `-navidrome account` | — | Member | Show your Discord-linked Navidrome account. |
| `-navidrome info` | `stats` | Member | Show non-sensitive Navidrome server and library information. |
| `-navidrome recent` | — | Member | Show recently added albums (1-10). |

### [Permissions](../modules/permissions.md) (3)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-permissions` | — | Member | Command permission management tools. |
| `-permissions canrun` | — | Member | Check if a user can run a command. |
| `-permissions explain` | — | Member | Explain how permissions works. |

### [Pokémon](../modules/pokemon.md) (29)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-pokemon` | `pkmn`, `poke` | Member | Play the global Pokémon catching and battle game. |
| `-pokemon achievements` | `goals` | Member | View accomplishment progress and upcoming supply rewards. |
| `-pokemon bag` | — | Member | View your available medicine and items. |
| `-pokemon buy` | — | Member | Buy Poké Mart supplies with Red bank credits. |
| `-pokemon center` | — | Member | Heal your party at this server’s Pokémon Center. |
| `-pokemon collection` | `box` | Member | Browse and manage Pokémon in your global collection. |
| `-pokemon collection release` | — | Member | Permanently release one boxed Pokémon after confirmation. |
| `-pokemon gym` | — | Member | View your ordered Kanto Gym progress. |
| `-pokemon gym challenge` | — | Member | Challenge the next Kanto Gym Leader's team. |
| `-pokemon mart` | — | Member | View supplies sold for Red bank credits. |
| `-pokemon menustyle` | — | Member | Choose the Retro or Modern Pokémon main-menu style. |
| `-pokemon moves` | — | Member | Resume an unfinished move-learning choice. |
| `-pokemon party` | — | Member | View the Pokémon in your active party. |
| `-pokemon party add` | — | Member | Add a caught Pokémon to your active party. |
| `-pokemon party remove` | — | Member | Remove a Pokémon from your active party. |
| `-pokemon pokedex` | `dex` | Member | Browse the Pokémon you have seen and caught. |
| `-pokemon pokedexstyle` | `dexstyle` | Member | Choose your Pokédex display style, or follow the bot default. |
| `-pokemon profile` | — | Member | View your or another member’s trainer card and badge case. |
| `-pokemon profilestyle` | `cardstyle` | Member | Choose the Retro or Gold style for your trainer card. |
| `-pokemon research` | `daily` | Member | View today’s Professor research tasks and supply rewards. |
| `-pokemon starter` | — | Member | Choose or view your first partner Pokémon. |
| `-pokemon trade` | — | Member | Offer an exact Pokémon-for-Pokémon trade. |
| `-pokemon trade cancel` | — | Member | Cancel one of your pending trade offers. |
| `-pokemon trade collection` | — | Member | View another trainer’s numbered Pokémon for a trade. |
| `-pokemon trade give` | `gift` | Member | Offer one to three Pokémon as a confirmed gift. |
| `-pokemon use` | — | Member | Use an item on one of your Pokémon. |
| `-pokemon use potion` | — | Member | Use a Potion to restore a Pokémon’s HP. |
| `-pokemon use revive` | — | Member | Use a Revive on a fainted Pokémon. |
| `-pokemon use stone` | — | Member | Use a Kanto evolution stone on an eligible Pokémon. |

### [Reports](../modules/reports.md) (1)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-report` | — | Member | Send a report. |

### [Rocket League](../modules/rocketleague.md) (17)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-rlcs` | — | Member | Show the next RLCS event (short form of rocketleague rlcs). |
| `-rlcs event` | — | Member | Show a cached official event or an explicit start.gg tournament. |
| `-rlcs events` | `list` | Member | List discoverable official event IDs and slugs from the local cache. |
| `-rlcs recent` | — | Member | Show recently completed official events from retained weekly snapshots. |
| `-rlcs results` | — | Member | Show detailed cached results for a completed Rocket League event. |
| `-rlcs upcoming` | — | Member | Show later RLCS events (short form of rocketleague rlcs upcoming). |
| `-rocketleague` | `rl` | Member | Browse Rocket League commands and announcement administration. |
| `-rocketleague clips` | — | Member | Show this server's automatic community clip feed. |
| `-rocketleague rlcs` | — | Member | Show the next RLCS event. |
| `-rocketleague rlcs event` | — | Member | Show a cached official event or an explicit start.gg tournament. |
| `-rocketleague rlcs events` | `list` | Member | List discoverable official event IDs and slugs from the local cache. |
| `-rocketleague rlcs recent` | — | Member | Show recently completed official events from retained weekly snapshots. |
| `-rocketleague rlcs results` | — | Member | Show detailed cached results for a completed Rocket League event. |
| `-rocketleague rlcs upcoming` | — | Member | Show RLCS tournaments scheduled after the next event. |
| `-rocketleague tournaments` | `tourney`, `tourneys` | Member | Show upcoming tournaments configured for this Discord server. |
| `-rocketleague tournaments recent` | — | Member | Show recently completed configured Rocket League tournaments. |
| `-rocketleague tournaments upcoming` | — | Member | Show upcoming configured Rocket League tournaments. |

### [Role Tools](../modules/roletools.md) (21)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-roletools` | — | Member | Member role help and server role-management commands. |
| `-roletools exclude` | `exclusive` | Member | Manage conflicting roles. |
| `-roletools group` | `groups`, `privategroups` | Member | View or manage private access groups. |
| `-roletools group join` | — | Member | Join a private group after its prerequisites and access cost are checked. |
| `-roletools group leave` | — | Member | Leave a private group and remove its gateway/selectable roles. |
| `-roletools group view` | — | Member | Show a private group's access rules and roles. |
| `-roletools include` | `inclusive` | Member | Manage linked roles. |
| `-roletools message` | — | Member | Manage RoleTools messages. |
| `-roletools message edit` | — | Member | Edit a bots message to include Role Buttons |
| `-roletools message editbutton` | — | Member | Edit a bots message to include Role Buttons |
| `-roletools message editselect` | — | Member | Edit a bots message to include Select Menus |
| `-roletools message send` | — | Member | Send a select menu to a specified channel for role assignment |
| `-roletools message sendbutton` | — | Member | Send buttons to a specified channel with optional message. |
| `-roletools message sendselect` | — | Member | Send a select menu to a specified channel for role assignment |
| `-roletools reaction` | `react`, `reactions` | Member | Manage reaction roles. |
| `-roletools required` | `req`, `require`, `requires` | Member | Manage role requirements. |
| `-roletools selfrole` | — | Member | Toggle a self-role. |
| `-roletools temporary` | `temp` | Member | Manage temporary roles. |
| `-roletools temporary list` | — | Member | List the currently pending temporary roles and when they expire. |
| `-roletools viewroles` | `viewrole` | Member | View available or configured roles. |
| `-selfroles` | — | Member | List available self-roles. |

### [RuneScape](../modules/runescape.md) (6)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-runescape` | `rs` | Member | Look up RuneScape players and wiki articles. |
| `-runescape item` | — | Member | Find an item on the Old School RuneScape Wiki. |
| `-runescape quest` | — | Member | Find a quest on the Old School RuneScape Wiki. |
| `-runescape rs3wiki` | — | Member | Search the RuneScape (RS3) Wiki. |
| `-runescape user` | `player`, `stats` | Member | Show stats. Prefix a name with `rs3` to use RuneScape 3. |
| `-runescape wiki` | `search` | Member | Search the Old School RuneScape Wiki. |

### [Streams](../modules/streams.md) (3)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-picarto` | — | Member | Check if a Picarto channel is live. |
| `-twitchstream` | — | Member | Check if a Twitch channel is live. |
| `-youtubestream` | — | Member | Check if a YouTube channel is live. |

### [Trivia](../modules/trivia.md) (7)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-trivia` | — | Member | Start trivia session on the specified category. |
| `-trivia info` | — | Member | Get information about a trivia category. |
| `-trivia leaderboard` | `lboard` | Member | Leaderboard for trivia. |
| `-trivia leaderboard global` | — | Member | Global trivia leaderboard. |
| `-trivia leaderboard server` | — | Member | Leaderboard for this server. |
| `-trivia list` | — | Member | List available trivia categories. |
| `-trivia stop` | — | Member | Stop an ongoing trivia session. |

### [Warnings](../modules/warnings.md) (1)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-mywarnings` | — | Member | List warnings for yourself. |

### [Wolfram](../modules/wolfram.md) (4)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-wolfram` | — | Member | Ask Wolfram\|Alpha a factual, mathematical, or scientific question. |
| `-wolframexample` | `wolframrandom` | Member | Show a curated Wolfram example. |
| `-wolframimage` | — | Member | Ask Wolfram\|Alpha a question and return an image. |
| `-wolframsolve` | — | Member | Ask Wolfram\|Alpha a math question and return step-by-step answers. |
