# Bot-maintainer commands

These command paths control the hosted bot, global configuration, installed code, or cross-server behavior. Discord server ownership does not grant this tier.

Use live help for current syntax and checks:

```text
-help <command>
-help <command> <subcommand>
-help <command> <subcommand> <nested-subcommand>
```

The catalog is generated from the sanitized production command inventory. Server
rules, role hierarchy, disabled commands, channel permissions, and module configuration
can further restrict availability. [Learn how to use command help](../using-help.md).

## Catalog (267 command paths)

### [Administration](../modules/admin.md) (3)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-announce` | — | Bot maintainer | Announce a message to all servers the bot is in. |
| `-announce cancel` | — | Bot maintainer | Cancel a running announce. |
| `-serverlock` | — | Bot maintainer | Lock a bot to its current servers only. |

### [Advanced Help](../modules/advancedhelp.md) (19)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-advancedhelpset` | `advhelpset` | Bot maintainer | Configure the AdvancedHelp formatter. |
| `-advancedhelpset audience` | — | Bot maintainer | List command audience overrides. |
| `-advancedhelpset audience appearance` | — | Bot maintainer | Set audience emoji and name\|description. |
| `-advancedhelpset audience order` | — | Bot maintainer | Set all four audience keys in display order. |
| `-advancedhelpset audience remove` | — | Bot maintainer | No short description is declared. |
| `-advancedhelpset audience set` | — | Bot maintainer | Assign a command to member, staff, server_owner, or bot_owner. |
| `-advancedhelpset category` | — | Bot maintainer | List command category overrides. |
| `-advancedhelpset category appearance` | — | Bot maintainer | Set category order, emoji, and name\|description. |
| `-advancedhelpset category remove` | — | Bot maintainer | No short description is declared. |
| `-advancedhelpset category set` | — | Bot maintainer | Assign an available command to a presentation category. |
| `-advancedhelpset deleteontimeout` | — | Bot maintainer | Delete interactive help when it expires instead of disabling it. |
| `-advancedhelpset destination` | — | Bot maintainer | Choose channel or DM delivery for bare prefix help. |
| `-advancedhelpset rolegroup` | — | Bot maintainer | List role-backed presentation groups. |
| `-advancedhelpset rolegroup add` | — | Bot maintainer | Add a Discord role to a named presentation group. |
| `-advancedhelpset rolegroup appearance` | — | Bot maintainer | Set a role group order, emoji, and name\|description. |
| `-advancedhelpset rolegroup category` | — | Bot maintainer | Add a presentation category to a named role group. |
| `-advancedhelpset rolegroup remove` | — | Bot maintainer | No short description is declared. |
| `-advancedhelpset timeout` | — | Bot maintainer | Set the interactive timeout from 30 through 900 seconds. |
| `-docsreport` | `commandinventory` | Bot maintainer | Export sanitized metadata for every registered command. |

### [Aliases](../modules/alias.md) (3)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-alias global add` | — | Bot maintainer | Add a global alias for a command. |
| `-alias global delete` | `del`, `remove` | Bot maintainer | Delete an existing global alias. |
| `-alias global edit` | — | Bot maintainer | Edit an existing global alias. |

### [Audio](../modules/audio.md) (50)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-audioset cache` | — | Bot maintainer | Sets the caching level. |
| `-audioset cacheage` | — | Bot maintainer | Sets the cache max age. |
| `-audioset globaldailyqueue` | — | Bot maintainer | Toggle global daily queues. |
| `-audioset localpath` | — | Bot maintainer | Set the localtracks path if the Lavalink.jar is not run from the Audio data folder. |
| `-audioset logs` | — | Bot maintainer | Sends the managed Lavalink node logs to your DMs. |
| `-audioset restart` | — | Bot maintainer | Restarts the lavalink connection. |
| `-audioset restrict` | — | Bot maintainer | Toggle the domain restriction on Audio. |
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
| `-audioset spotifyapi` | — | Bot maintainer | Instructions to set the Spotify API tokens. |
| `-audioset status` | — | Bot maintainer | Enable/disable tracks' titles as status. |
| `-audioset youtubeapi` | — | Bot maintainer | Instructions to set the YouTube API key. |
| `-audiostats` | — | Bot maintainer | Audio stats. |
| `-llset` | — | Bot maintainer | `Dangerous commands` Manage Lavalink node configuration settings. |
| `-llset config` | `conf` | Bot maintainer | Configure the managed Lavalink node runtime options. |
| `-llset config bind` | `address`, `host` | Bot maintainer | `Dangerous command` Set the managed Lavalink node's binding IP address. |
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
| `-llset config token` | `pass`, `password` | Bot maintainer | Set the managed Lavalink node's connection password. |
| `-llset heapsize` | `hs`, `memory`, `ram` | Bot maintainer | Set the managed Lavalink node maximum heap-size. |
| `-llset host` | — | Bot maintainer | Set the Lavalink node host. |
| `-llset info` | `settings` | Bot maintainer | Display Lavalink connection settings. |
| `-llset java` | — | Bot maintainer | Change your Java executable path. |
| `-llset password` | `pass`, `token` | Bot maintainer | Set the Lavalink node password. |
| `-llset port` | — | Bot maintainer | Set the Lavalink node port. |
| `-llset reset` | — | Bot maintainer | Reset all `llset` changes back to their default values. |
| `-llset secured` | `wss` | Bot maintainer | Set the Lavalink node connection to secured. |
| `-llset unmanaged` | `external` | Bot maintainer | Toggle using external (unmanaged) Lavalink nodes - requires an existing Lavalink node for Audio to work, if enabled. |
| `-llset yaml` | `yml` | Bot maintainer | Uploads a copy of the application.yml file used by the managed Lavalink node. |
| `-playlist download` | — | Bot maintainer | Download a copy of a playlist. |
| `-playlist upload` | — | Bot maintainer | Uploads a playlist file as a playlist for the bot. |

### [Cog Manager](../modules/cogmanagerui.md) (6)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-addpath` | — | Bot maintainer | Add a path to the list of available cog paths. |
| `-cogs` | — | Bot maintainer | Lists all loaded and available cogs. |
| `-installpath` | — | Bot maintainer | Returns the current install path or sets it if one is provided. |
| `-paths` | — | Bot maintainer | Lists current cog paths in order of priority. |
| `-removepath` | — | Bot maintainer | Removes one or more paths from the available cog paths given the `path_numbers` from `-paths`. |
| `-reorderpath` | — | Bot maintainer | Reorders paths internally to allow discovery of different cogs. |

### [Core](../modules/core.md) (99)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-allowlist` | `whitelist` | Bot maintainer | Commands to manage the allowlist. |
| `-allowlist add` | — | Bot maintainer | Adds users to the allowlist. |
| `-allowlist clear` | — | Bot maintainer | Clears the allowlist. |
| `-allowlist list` | — | Bot maintainer | Lists users on the allowlist. |
| `-allowlist remove` | — | Bot maintainer | Removes users from the allowlist. |
| `-bankset prune global` | — | Bot maintainer | Prune bank accounts for users who no longer share a server with the bot. |
| `-bankset toggleglobal` | — | Bot maintainer | Toggle whether the bank is global or not. |
| `-blocklist` | `blacklist`, `denylist` | Bot maintainer | Commands to manage the blocklist. |
| `-blocklist add` | — | Bot maintainer | Adds users to the blocklist. |
| `-blocklist clear` | — | Bot maintainer | Clears the blocklist. |
| `-blocklist list` | — | Bot maintainer | Lists users on the blocklist. |
| `-blocklist remove` | — | Bot maintainer | Removes users from the blocklist. |
| `-command defaultdisablecog` | — | Bot maintainer | Set the default state for a cog as disabled. |
| `-command defaultenablecog` | — | Bot maintainer | Set the default state for a cog as enabled. |
| `-command disable global` | — | Bot maintainer | Disable a command globally. |
| `-command disabledmsg` | — | Bot maintainer | Set the bot's response to disabled commands. |
| `-command enable global` | — | Bot maintainer | Enable a command globally. |
| `-datapath` | — | Bot maintainer | Prints the bot's data path. |
| `-debuginfo` | — | Bot maintainer | Shows debug information useful for debugging. |
| `-diagnoseissues` | — | Bot maintainer | Diagnose issues with the command checks with ease! |
| `-dm` | — | Bot maintainer | Sends a DM to a user. |
| `-embedset command global` | — | Bot maintainer | Sets a command's embed setting globally. |
| `-embedset global` | — | Bot maintainer | Toggle the global embed setting. |
| `-helpset` | — | Bot maintainer | Commands to manage settings for the help command. |
| `-helpset deletedelay` | — | Bot maintainer | Set the delay after which help pages will be deleted. |
| `-helpset maxpages` | — | Bot maintainer | Set the maximum number of help pages sent in a server channel. |
| `-helpset pagecharlimit` | — | Bot maintainer | Set the character limit for each page in the help message. |
| `-helpset reacttimeout` | — | Bot maintainer | Set the timeout for reactions, if menus are enabled. |
| `-helpset resetformatter` | — | Bot maintainer | This resets SickGamingBot's help formatter to the default formatter. |
| `-helpset resetsettings` | — | Bot maintainer | This resets SickGamingBot's help settings to their defaults. |
| `-helpset showaliases` | — | Bot maintainer | This allows the help command to show existing commands aliases if there is any. |
| `-helpset showhidden` | — | Bot maintainer | This allows the help command to show hidden commands. |
| `-helpset showsettings` | — | Bot maintainer | Show the current help settings. |
| `-helpset tagline` | — | Bot maintainer | Set the tagline to be used. |
| `-helpset usemenus` | — | Bot maintainer | Allows the help command to be sent as a paginated menu instead of separate |
| `-helpset usetick` | — | Bot maintainer | This allows the help command message to be ticked if help is sent to a DM. |
| `-helpset verifychecks` | — | Bot maintainer | Sets if commands which can't be run in the current context should be filtered from help. |
| `-helpset verifyexists` | — | Bot maintainer | Sets whether the bot should respond to help commands for nonexistent topics. |
| `-inviteset` | — | Bot maintainer | Commands to setup SickGamingBot's invite settings. |
| `-inviteset commandscope` | — | Bot maintainer | Add the `applications.commands` scope to your invite URL. |
| `-inviteset perms` | — | Bot maintainer | Make the bot create its own role with permissions on join. |
| `-inviteset public` | — | Bot maintainer | Toggles if `-invite` should be accessible for the average user. |
| `-leave` | — | Bot maintainer | Leaves servers. |
| `-load` | — | Bot maintainer | Loads cog packages from the local paths and installed cogs. |
| `-modlogset fixcasetypes` | — | Bot maintainer | Command to fix misbehaving casetypes. |
| `-mydata ownermanagement` | — | Bot maintainer | Commands for more complete data handling. |
| `-mydata ownermanagement allowuserdeletions` | — | Bot maintainer | Set the bot to allow users to request a data deletion. |
| `-mydata ownermanagement deleteforuser` | — | Bot maintainer | Delete data SickGamingBot has about a user for a user. |
| `-mydata ownermanagement deleteuserasowner` | — | Bot maintainer | Delete data SickGamingBot has about a user. |
| `-mydata ownermanagement disallowuserdeletions` | — | Bot maintainer | Set the bot to not allow users to request a data deletion. |
| `-mydata ownermanagement processdiscordrequest` | — | Bot maintainer | Handle a deletion request from Discord. |
| `-mydata ownermanagement setuserdeletionlevel` | — | Bot maintainer | Sets how user deletions are treated. |
| `-reload` | — | Bot maintainer | Reloads cog packages. |
| `-restart` | — | Bot maintainer | Attempts to restart SickGamingBot. |
| `-servers` | — | Bot maintainer | Lists the servers SickGamingBot is currently in. |
| `-set api` | — | Bot maintainer | Commands to set, list or remove various external API tokens. |
| `-set api list` | — | Bot maintainer | Show all external API services along with their keys that have been set. |
| `-set api remove` | — | Bot maintainer | Remove the given services with all their keys and tokens. |
| `-set bot avatar` | — | Bot maintainer | Sets SickGamingBot's avatar |
| `-set bot avatar remove` | `clear` | Bot maintainer | Removes SickGamingBot's avatar. |
| `-set bot banner` | — | Bot maintainer | Sets SickGamingBot's banner |
| `-set bot banner remove` | `clear` | Bot maintainer | Removes SickGamingBot's banner. |
| `-set bot custominfo` | — | Bot maintainer | Customizes a section of `-info`. |
| `-set bot description` | — | Bot maintainer | Sets the bot's description. |
| `-set bot username` | `name` | Bot maintainer | Sets SickGamingBot's username. |
| `-set colour` | `color` | Bot maintainer | Sets a default colour to be used for the bot's embeds. |
| `-set errormsg` | — | Bot maintainer | Set the message that will be sent on uncaught bot errors. |
| `-set fuzzy` | — | Bot maintainer | Toggle whether to enable fuzzy command search in DMs. |
| `-set locale global` | — | Bot maintainer | Changes SickGamingBot's default locale. |
| `-set ownernotifications` | — | Bot maintainer | Commands for configuring owner notifications. |
| `-set ownernotifications adddestination` | — | Bot maintainer | Adds a destination text channel to receive owner notifications. |
| `-set ownernotifications listdestinations` | — | Bot maintainer | Lists the configured extra destinations for owner notifications. |
| `-set ownernotifications optin` | — | Bot maintainer | Opt-in on receiving owner notifications. |
| `-set ownernotifications optout` | — | Bot maintainer | Opt-out of receiving owner notifications. |
| `-set ownernotifications removedestination` | `deldestination`, `deletedestination`, `remdestination` | Bot maintainer | Removes a destination text channel from receiving owner notifications. |
| `-set prefix` | `globalprefix`, `globalprefixes`, `prefixes` | Bot maintainer | Sets SickGamingBot's global prefix(es). |
| `-set regionalformat global` | — | Bot maintainer | Changes the bot's regional format. This is used for formatting date, time and numbers. |
| `-set status` | — | Bot maintainer | Commands for setting SickGamingBot's status. |
| `-set status competing` | — | Bot maintainer | Sets SickGamingBot's competing status. |
| `-set status custom` | — | Bot maintainer | Sets SickGamingBot's custom status. |
| `-set status dnd` | `busy`, `donotdisturb` | Bot maintainer | Set SickGamingBot's status to do not disturb. |
| `-set status idle` | `afk`, `away` | Bot maintainer | Set SickGamingBot's status to idle. |
| `-set status invisible` | `offline` | Bot maintainer | Set SickGamingBot's status to invisible. |
| `-set status listening` | — | Bot maintainer | Sets SickGamingBot's listening status. |
| `-set status online` | — | Bot maintainer | Set SickGamingBot's status to online. |
| `-set status playing` | `game` | Bot maintainer | Sets SickGamingBot's playing status. |
| `-set status streaming` | `stream`, `twitch` | Bot maintainer | Sets SickGamingBot's streaming status to a twitch stream. |
| `-set status watching` | — | Bot maintainer | Sets SickGamingBot's watching status. |
| `-set usebuttons` | — | Bot maintainer | Set a global bot variable for using buttons in menus. |
| `-shutdown` | — | Bot maintainer | Shuts down the bot. |
| `-slash` | — | Bot maintainer | Base command for managing what application commands are able to be used on SickGamingBot. |
| `-slash disable` | — | Bot maintainer | Marks an application command as being disabled, preventing it from being added to the bot. |
| `-slash disablecog` | — | Bot maintainer | Marks all application commands in a cog as being disabled, preventing them from being added to the bot. |
| `-slash enable` | — | Bot maintainer | Marks an application command as being enabled, allowing it to be added to the bot. |
| `-slash enablecog` | — | Bot maintainer | Marks all application commands in a cog as being enabled, allowing them to be added to the bot. |
| `-slash list` | — | Bot maintainer | List the slash commands the bot can see, and whether or not they are enabled. |
| `-slash sync` | — | Bot maintainer | Syncs the slash settings to discord. |
| `-traceback` | — | Bot maintainer | Sends to the owner the last command exception that has occurred. |
| `-unload` | — | Bot maintainer | Unloads previously loaded cog packages. |

### [Downloader](../modules/downloader.md) (21)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-cog` | — | Bot maintainer | Base command for cog installation management commands. |
| `-cog checkforupdates` | — | Bot maintainer | Check for available cog updates (including pinned cogs). |
| `-cog info` | — | Bot maintainer | List information about a single cog. |
| `-cog install` | — | Bot maintainer | Install a cog from the given repo. |
| `-cog installversion` | — | Bot maintainer | Install a cog from the specified revision of given repo. |
| `-cog list` | — | Bot maintainer | List all available cogs from a single repo. |
| `-cog listpinned` | — | Bot maintainer | List currently pinned cogs. |
| `-cog pin` | — | Bot maintainer | Pin cogs - this will lock cogs on their current version. |
| `-cog reinstallreqs` | — | Bot maintainer | This command should not be used unless Red specifically asks for it. |
| `-cog uninstall` | — | Bot maintainer | Uninstall cogs. |
| `-cog unpin` | — | Bot maintainer | Unpin cogs - this will remove the update lock from those cogs. |
| `-cog update` | — | Bot maintainer | Update all cogs, or ones of your choosing. |
| `-cog updateallfromrepos` | — | Bot maintainer | Update all cogs from repos of your choosing. |
| `-cog updatetoversion` | — | Bot maintainer | Update all cogs, or ones of your choosing to chosen revision of one repo. |
| `-pipinstall` | — | Bot maintainer | Install a group of dependencies using pip. |
| `-repo` | — | Bot maintainer | Base command for repository management. |
| `-repo add` | — | Bot maintainer | Add a new repo. |
| `-repo delete` | `del`, `remove` | Bot maintainer | Remove repos and their files. |
| `-repo info` | — | Bot maintainer | Show information about a repo. |
| `-repo list` | — | Bot maintainer | List all installed repos. |
| `-repo update` | — | Bot maintainer | Update all repos, or ones of your choosing. |

### [Garry's Mod](../modules/gmod.md) (4)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-gmodowner` | — | Bot maintainer | Manage bot-owner-only GMod network policy. |
| `-gmodowner privatehost` | — | Bot maintainer | No short description is declared. |
| `-gmodowner privatehost add` | — | Bot maintainer | No short description is declared. |
| `-gmodowner privatehost remove` | — | Bot maintainer | No short description is declared. |

### [Image](../modules/image.md) (2)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-giphycreds` | — | Bot maintainer | Explains how to set GIPHY API tokens. |
| `-imgurcreds` | — | Bot maintainer | Explain how to set imgur API tokens. |

### [Moderation](../modules/mod.md) (4)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-modset deletenames` | — | Bot maintainer | Delete all stored usernames, global display names, and server nicknames. |
| `-modset trackallnames` | — | Bot maintainer | Toggle whether all name changes should be tracked. |
| `-movedeletedelay` | — | Bot maintainer | Move deletedelay settings to core |
| `-moveignoredchannels` | — | Bot maintainer | Move ignored channels and servers to core |

### [NSFW](../modules/nsfw.md) (1)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-nsfwset switchredditapi` | — | Bot maintainer | Toggle to use Reddit API directly with the cost of getting ratelimited fast, or use Martine API with faster results and no ratelimits problems. |

### [Navidrome](../modules/navidrome.md) (6)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-navidromeowner` | — | Bot maintainer | Manage bot-owner-approved Navidrome connections. |
| `-navidromeowner connection` | — | Bot maintainer | Manage approved connection profiles. |
| `-navidromeowner connection add` | — | Bot maintainer | Approve a URL after setting navidrome_NAME username/password API tokens. |
| `-navidromeowner connection list` | `show` | Bot maintainer | List approved connection names and redacted endpoints. |
| `-navidromeowner connection remove` | `delete` | Bot maintainer | Remove an approved connection profile. Credentials are not deleted. |
| `-navidromeowner connection test` | — | Bot maintainer | Test an approved connection without exposing credentials. |

### [Permissions](../modules/permissions.md) (7)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-permissions acl getglobal` | — | Bot maintainer | Get a YAML file detailing all global rules. |
| `-permissions acl setglobal` | — | Bot maintainer | Set global rules with a YAML file. |
| `-permissions acl updateglobal` | — | Bot maintainer | Update global rules with a YAML file. |
| `-permissions addglobalrule` | — | Bot maintainer | Add a global rule to a command. |
| `-permissions clearglobalrules` | — | Bot maintainer | Reset all global rules. |
| `-permissions removeglobalrule` | — | Bot maintainer | Remove a global rule from a command. |
| `-permissions setdefaultglobalrule` | — | Bot maintainer | Set the default global rule for a command. |

### [Pokémon](../modules/pokemon.md) (21)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-pokemonownerset` | `pkmnownerset`, `pokeownerset` | Bot maintainer | Configure bot-wide Pokémon policy and owner overrides. |
| `-pokemonownerset catalogsync` | — | Bot maintainer | Cache catalog data for a generation. |
| `-pokemonownerset centercooldown` | — | Bot maintainer | Set the bot-wide free Pokémon Center cooldown. |
| `-pokemonownerset concurrency` | `slots` | Bot maintainer | Override this server’s simultaneous encounter limit. |
| `-pokemonownerset encounterlimits` | — | Bot maintainer | Set server wild-encounter lifetime boundaries. |
| `-pokemonownerset encountertime` | — | Bot maintainer | Set the inherited bot-wide wild encounter lifetime. |
| `-pokemonownerset globalconcurrency` | — | Bot maintainer | Set the concurrency ceiling for ordinary server administrators. |
| `-pokemonownerset globalgenerations` | — | Bot maintainer | Set bot-wide available generations. |
| `-pokemonownerset globallimits` | — | Bot maintainer | Set global spawn-rate floors. |
| `-pokemonownerset globalstatus` | `settings`, `status` | Bot maintainer | Show all bot-wide Pokémon policies and owner limits. |
| `-pokemonownerset martprice` | — | Bot maintainer | Set a bot-wide Poké Mart item price. |
| `-pokemonownerset pokedexstyle` | — | Bot maintainer | Choose the default Pokédex style for users following the default. |
| `-pokemonownerset profile` | — | Bot maintainer | Apply a server profile with per-server owner overrides. |
| `-pokemonownerset rarity` | — | Bot maintainer | Choose the global rarity profile. |
| `-pokemonownerset resetplayer` | — | Bot maintainer | Reset one complete Pokémon profile. |
| `-pokemonownerset specials` | — | Bot maintainer | Allow or gate special species. |
| `-pokemonownerset timer` | — | Bot maintainer | Override this server’s jittered timer from 1 minute to one week. |
| `-pokemonownerset timermin` | `minimumtimer` | Bot maintainer | Set the fastest timer ordinary server administrators may choose. |
| `-pokemonownerset vipclear` | — | Bot maintainer | Disable the trusted VIP role without removing prior rewards or Pokémon. |
| `-pokemonownerset vippack` | — | Bot maintainer | Set the monthly VIP supply pack. |
| `-pokemonownerset viprole` | — | Bot maintainer | Set or show the trusted guild and role for global VIP benefits. |

### [RSS Publisher](../modules/rsspublisher.md) (9)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-rsspublisher migrationstatus` | — | Bot maintainer | Show migration status. |
| `-rsspublisher parse` | — | Bot maintainer | Manage domain parsing. |
| `-rsspublisher parse add` | — | Bot maintainer | Add a website to the list for a time parsing override. |
| `-rsspublisher parse list` | — | Bot maintainer | Show the list for time parsing overrides. |
| `-rsspublisher parse remove` | `del`, `delete` | Bot maintainer | Remove a website from the list for a time parsing override. |
| `-rsspublisher privatehost` | — | Bot maintainer | Manage trusted private hosts. |
| `-rsspublisher privatehost add` | — | Bot maintainer | Allow one private hostname or IP address for RSS requests. |
| `-rsspublisher privatehost list` | — | Bot maintainer | List private RSS hosts explicitly trusted by the bot owner. |
| `-rsspublisher privatehost remove` | `delete` | Bot maintainer | Remove a private hostname or IP address from the RSS allowlist. |

### [Rocket League](../modules/rocketleague.md) (1)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-rlcsset refresh` | — | Bot maintainer | Refresh BLAST when the seven-day request window permits. |

### [Role Tools](../modules/roletools.md) (3)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-roletools globalatomic` | — | Bot maintainer | Set the atomicity of role assignment. |
| `-roletools migrationstatus` | — | Bot maintainer | Owner migration status. |
| `-roletools reaction ownercleanup` | — | Bot maintainer | Cleanup old/missing reaction roles and settings on the bot. |

### [Streams](../modules/streams.md) (3)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-streamset timer` | — | Bot maintainer | Set stream check refresh time. |
| `-streamset twitchtoken` | — | Bot maintainer | Explain how to set the twitch token. |
| `-streamset youtubekey` | — | Bot maintainer | Explain how to set the YouTube token. |

### [Trivia](../modules/trivia.md) (4)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-triviaset custom` | — | Bot maintainer | Manage Custom Trivia lists. |
| `-triviaset custom delete` | `remove` | Bot maintainer | Delete a trivia file. |
| `-triviaset custom list` | — | Bot maintainer | List uploaded custom trivia. |
| `-triviaset custom upload` | `add` | Bot maintainer | Upload a trivia file. |

### [Welcome](../modules/welcome.md) (1)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-welcomeset migrationstatus` | — | Bot maintainer | Owner: show the external Welcome import status. |
