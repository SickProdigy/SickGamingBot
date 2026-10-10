# Core commands

Always-loaded Red core commands

## Reading this reference

Each command is shown as its complete path. To see detailed help, put that path after
`-help` without repeating the leading hyphen:

```text
-help <command>
-help <command> <subcommand>
-help <command> <subcommand> <nested-subcommand>
```

The access column is derived from declared command checks. Server-specific permission
rules can change it. See [Using SickGamingBot help](../using-help.md) for examples and
an explanation of required and optional arguments.

| Command | Aliases | Access | Description |
| --- | --- | --- | --- |
| `-allowlist` | `whitelist` | Bot maintainer | Commands to manage the allowlist. |
| `-allowlist add` | — | Bot maintainer | Adds users to the allowlist. |
| `-allowlist clear` | — | Bot maintainer | Clears the allowlist. |
| `-allowlist list` | — | Bot maintainer | Lists users on the allowlist. |
| `-allowlist remove` | — | Bot maintainer | Removes users from the allowlist. |
| `-autoimmune` | — | Server owner or required Discord permission | Commands to manage server settings for immunity from automated actions. |
| `-autoimmune add` | — | Server owner or required Discord permission | Makes a user or role immune from automated moderation actions. |
| `-autoimmune isimmune` | — | Server owner or required Discord permission | Checks if a user or role would be considered immune from automated actions. |
| `-autoimmune list` | — | Server owner or required Discord permission | Gets the current members and roles configured for automatic moderation action immunity. |
| `-autoimmune remove` | — | Server owner or required Discord permission | Remove a user or role from being immune to automated moderation actions. |
| `-bankset` | — | Server owner or required Discord permission | Base command for bank settings. |
| `-bankset bankname` | — | Server owner or required Discord permission | Set the bank's name. |
| `-bankset creditsname` | — | Server owner or required Discord permission | Set the name for the bank's currency. |
| `-bankset maxbal` | — | Server owner or required Discord permission | Set the maximum balance a user can get. |
| `-bankset prune` | — | Server owner or required Discord permission | Base command for pruning bank accounts. |
| `-bankset prune global` | — | Server owner or required Discord permission | Prune bank accounts for users who no longer share a server with the bot. |
| `-bankset prune server` | `guild`, `local` | Server owner or required Discord permission | Prune bank accounts for users no longer in the server. |
| `-bankset prune user` | — | Server owner or required Discord permission | Delete the bank account of a specified user. |
| `-bankset registeramount` | — | Server owner or required Discord permission | Set the initial balance for new bank accounts. |
| `-bankset reset` | — | Server owner or required Discord permission | Delete all bank accounts. |
| `-bankset showsettings` | — | Server owner or required Discord permission | Show the current bank settings. |
| `-bankset toggleglobal` | — | Server owner or required Discord permission | Toggle whether the bank is global or not. |
| `-blocklist` | `blacklist`, `denylist` | Bot maintainer | Commands to manage the blocklist. |
| `-blocklist add` | — | Bot maintainer | Adds users to the blocklist. |
| `-blocklist clear` | — | Bot maintainer | Clears the blocklist. |
| `-blocklist list` | — | Bot maintainer | Lists users on the blocklist. |
| `-blocklist remove` | — | Bot maintainer | Removes users from the blocklist. |
| `-command` | — | Server owner or required Discord permission | Commands to enable and disable commands and cogs. |
| `-command defaultdisablecog` | — | Bot maintainer | Set the default state for a cog as disabled. |
| `-command defaultenablecog` | — | Bot maintainer | Set the default state for a cog as enabled. |
| `-command disable` | — | Server owner or required Discord permission | Disable a command. |
| `-command disable global` | — | Bot maintainer | Disable a command globally. |
| `-command disable server` | `guild` | Server owner or required Discord permission | Disable a command in this server only. |
| `-command disablecog` | — | Server owner or required Discord permission | Disable a cog in this server. |
| `-command disabledmsg` | — | Bot maintainer | Set the bot's response to disabled commands. |
| `-command enable` | — | Server owner or required Discord permission | Enable a command. |
| `-command enable global` | — | Bot maintainer | Enable a command globally. |
| `-command enable server` | `guild` | Server owner or required Discord permission | Enable a command in this server. |
| `-command enablecog` | — | Server owner or required Discord permission | Enable a cog in this server. |
| `-command listdisabled` | — | Server owner or required Discord permission | List disabled commands. |
| `-command listdisabled global` | — | Server owner or required Discord permission | List disabled commands globally. |
| `-command listdisabled guild` | — | Server owner or required Discord permission | List disabled commands in this server. |
| `-command listdisabledcogs` | — | Server owner or required Discord permission | List the cogs which are disabled in this server. |
| `-contact` | — | Member | Sends a message to the owner. |
| `-datapath` | — | Bot maintainer | Prints the bot's data path. |
| `-debuginfo` | — | Bot maintainer | Shows debug information useful for debugging. |
| `-diagnoseissues` | — | Bot maintainer | Diagnose issues with the command checks with ease! |
| `-dm` | — | Bot maintainer | Sends a DM to a user. |
| `-embedset` | — | Member | Commands for toggling embeds on or off. |
| `-embedset channel` | — | Server owner or required Discord permission | Set's a channel's embed setting. |
| `-embedset command` | — | Server owner or required Discord permission | Sets a command's embed setting. |
| `-embedset command global` | — | Bot maintainer | Sets a command's embed setting globally. |
| `-embedset command server` | `guild` | Server owner or required Discord permission | Sets a command's embed setting for the current server. |
| `-embedset global` | — | Bot maintainer | Toggle the global embed setting. |
| `-embedset server` | `guild` | Server owner or required Discord permission | Set the server's embed setting. |
| `-embedset showsettings` | — | Member | Show the current embed settings. |
| `-embedset user` | — | Member | Sets personal embed setting for DMs. |
| `-help` | — | Member | Shows commands available to you or detailed help for one command. |
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
| `-ignore` | — | Member | Commands to add servers or channels to the ignore list. |
| `-ignore channel` | — | Member | Ignore commands in the channel, thread, or category. |
| `-ignore list` | — | Member | List the currently ignored servers and channels. |
| `-ignore server` | `guild` | Administrator or required Discord permission | Ignore commands in this server. |
| `-info` | — | Member | Shows info about SickGamingBot. |
| `-invite` | — | Member | Shows SickGamingBot's invite url. |
| `-inviteset` | — | Bot maintainer | Commands to setup SickGamingBot's invite settings. |
| `-inviteset commandscope` | — | Bot maintainer | Add the `applications.commands` scope to your invite URL. |
| `-inviteset perms` | — | Bot maintainer | Make the bot create its own role with permissions on join. |
| `-inviteset public` | — | Bot maintainer | Toggles if `-invite` should be accessible for the average user. |
| `-leave` | — | Bot maintainer | Leaves servers. |
| `-licenseinfo` | `licenceinfo` | Member | Get info about Red's licenses. |
| `-load` | — | Bot maintainer | Loads cog packages from the local paths and installed cogs. |
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
| `-modlogset` | — | Server owner or required Discord permission | Manage modlog settings. |
| `-modlogset cases` | — | Server owner or required Discord permission | Enable or disable case creation for a mod action. |
| `-modlogset fixcasetypes` | — | Bot maintainer | Command to fix misbehaving casetypes. |
| `-modlogset modlog` | `channel` | Server owner or required Discord permission | Set a channel as the modlog. |
| `-modlogset resetcases` | — | Server owner or required Discord permission | Reset all modlog cases in this server. |
| `-mydata` | — | Member | Commands which interact with the data SickGamingBot has about you. |
| `-mydata 3rdparty` | — | Member | View the End User Data statements of each 3rd-party module. |
| `-mydata forgetme` | — | Member | Have SickGamingBot forget what it knows about you. |
| `-mydata getmydata` | — | Member | [Coming Soon] Get what data SickGamingBot has about you. |
| `-mydata ownermanagement` | — | Bot maintainer | Commands for more complete data handling. |
| `-mydata ownermanagement allowuserdeletions` | — | Bot maintainer | Set the bot to allow users to request a data deletion. |
| `-mydata ownermanagement deleteforuser` | — | Bot maintainer | Delete data SickGamingBot has about a user for a user. |
| `-mydata ownermanagement deleteuserasowner` | — | Bot maintainer | Delete data SickGamingBot has about a user. |
| `-mydata ownermanagement disallowuserdeletions` | — | Bot maintainer | Set the bot to not allow users to request a data deletion. |
| `-mydata ownermanagement processdiscordrequest` | — | Bot maintainer | Handle a deletion request from Discord. |
| `-mydata ownermanagement setuserdeletionlevel` | — | Bot maintainer | Sets how user deletions are treated. |
| `-mydata whatdata` | — | Member | Find out what type of data SickGamingBot stores and why. |
| `-ping` | — | Member | Pong. |
| `-reload` | — | Bot maintainer | Reloads cog packages. |
| `-restart` | — | Bot maintainer | Attempts to restart SickGamingBot. |
| `-servers` | — | Bot maintainer | Lists the servers SickGamingBot is currently in. |
| `-set` | — | Member | Commands for changing SickGamingBot's settings. |
| `-set api` | — | Bot maintainer | Commands to set, list or remove various external API tokens. |
| `-set api list` | — | Bot maintainer | Show all external API services along with their keys that have been set. |
| `-set api remove` | — | Bot maintainer | Remove the given services with all their keys and tokens. |
| `-set bot` | `metadata` | Administrator or required Discord permission | Commands for changing SickGamingBot's metadata. |
| `-set bot avatar` | — | Bot maintainer | Sets SickGamingBot's avatar |
| `-set bot avatar remove` | `clear` | Bot maintainer | Removes SickGamingBot's avatar. |
| `-set bot banner` | — | Bot maintainer | Sets SickGamingBot's banner |
| `-set bot banner remove` | `clear` | Bot maintainer | Removes SickGamingBot's banner. |
| `-set bot custominfo` | — | Bot maintainer | Customizes a section of `-info`. |
| `-set bot description` | — | Bot maintainer | Sets the bot's description. |
| `-set bot nickname` | — | Administrator or required Discord permission | Sets SickGamingBot's nickname for the current server. |
| `-set bot username` | `name` | Bot maintainer | Sets SickGamingBot's username. |
| `-set colour` | `color` | Bot maintainer | Sets a default colour to be used for the bot's embeds. |
| `-set deletedelay` | — | Server owner or required Discord permission | Set the delay until the bot removes the command message. |
| `-set errormsg` | — | Bot maintainer | Set the message that will be sent on uncaught bot errors. |
| `-set fuzzy` | — | Bot maintainer | Toggle whether to enable fuzzy command search in DMs. |
| `-set locale` | — | Server owner or required Discord permission | Changes SickGamingBot's locale in this server. |
| `-set locale global` | — | Bot maintainer | Changes SickGamingBot's default locale. |
| `-set locale server` | `local`, `guild` | Server owner or required Discord permission | Changes SickGamingBot's locale in this server. |
| `-set ownernotifications` | — | Bot maintainer | Commands for configuring owner notifications. |
| `-set ownernotifications adddestination` | — | Bot maintainer | Adds a destination text channel to receive owner notifications. |
| `-set ownernotifications listdestinations` | — | Bot maintainer | Lists the configured extra destinations for owner notifications. |
| `-set ownernotifications optin` | — | Bot maintainer | Opt-in on receiving owner notifications. |
| `-set ownernotifications optout` | — | Bot maintainer | Opt-out of receiving owner notifications. |
| `-set ownernotifications removedestination` | `remdestination`, `deletedestination`, `deldestination` | Bot maintainer | Removes a destination text channel from receiving owner notifications. |
| `-set prefix` | `prefixes`, `globalprefix`, `globalprefixes` | Bot maintainer | Sets SickGamingBot's global prefix(es). |
| `-set regionalformat` | `region` | Server owner or required Discord permission | Changes the bot's regional format in this server. This is used for formatting date, time and numbers. |
| `-set regionalformat global` | — | Bot maintainer | Changes the bot's regional format. This is used for formatting date, time and numbers. |
| `-set regionalformat server` | `local`, `guild` | Server owner or required Discord permission | Changes the bot's regional format in this server. This is used for formatting date, time and numbers. |
| `-set roles` | — | Server owner | Set server's admin and mod roles for SickGamingBot. |
| `-set roles addadminrole` | — | Server owner | Adds an admin role for this server. |
| `-set roles addmodrole` | — | Server owner | Adds a moderator role for this server. |
| `-set roles removeadminrole` | `remadmindrole`, `deladminrole`, `deleteadminrole` | Server owner | Removes an admin role for this server. |
| `-set roles removemodrole` | `remmodrole`, `delmodrole`, `deletemodrole` | Server owner | Removes a mod role for this server. |
| `-set serverfuzzy` | — | Server owner | Toggle whether to enable fuzzy command search for the server. |
| `-set serverprefix` | `serverprefixes` | Administrator or required Discord permission | Sets SickGamingBot's server prefix(es). |
| `-set showsettings` | — | Member | Show the current settings for SickGamingBot. |
| `-set status` | — | Bot maintainer | Commands for setting SickGamingBot's status. |
| `-set status competing` | — | Bot maintainer | Sets SickGamingBot's competing status. |
| `-set status custom` | — | Bot maintainer | Sets SickGamingBot's custom status. |
| `-set status dnd` | `donotdisturb`, `busy` | Bot maintainer | Set SickGamingBot's status to do not disturb. |
| `-set status idle` | `away`, `afk` | Bot maintainer | Set SickGamingBot's status to idle. |
| `-set status invisible` | `offline` | Bot maintainer | Set SickGamingBot's status to invisible. |
| `-set status listening` | — | Bot maintainer | Sets SickGamingBot's listening status. |
| `-set status online` | — | Bot maintainer | Set SickGamingBot's status to online. |
| `-set status playing` | `game` | Bot maintainer | Sets SickGamingBot's playing status. |
| `-set status streaming` | `stream`, `twitch` | Bot maintainer | Sets SickGamingBot's streaming status to a twitch stream. |
| `-set status watching` | — | Bot maintainer | Sets SickGamingBot's watching status. |
| `-set usebotcolour` | `usebotcolor` | Server owner | Toggle whether to use the bot owner-configured colour for embeds. |
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
| `-unignore` | — | Member | Commands to remove servers or channels from the ignore list. |
| `-unignore channel` | — | Member | Remove a channel, thread, or category from the ignore list. |
| `-unignore server` | `guild` | Administrator or required Discord permission | Remove this server from the ignore list. |
| `-unload` | — | Bot maintainer | Unloads previously loaded cog packages. |
| `-uptime` | — | Member | Shows SickGamingBot's uptime. |

Live `-help` output remains authoritative for enabled state, hidden commands,
arguments, cooldowns, and server-specific access.
