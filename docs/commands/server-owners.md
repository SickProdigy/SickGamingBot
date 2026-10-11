# Server-owner commands

These command paths declare Discord server ownership as their primary boundary. Server owners also use member and staff commands allowed by the live permission system.

Use live help for current syntax and checks:

```text
-help <command>
-help <command> <subcommand>
-help <command> <subcommand> <nested-subcommand>
```

The catalog is generated from the sanitized production command inventory. Server
rules, role hierarchy, disabled commands, channel permissions, and module configuration
can further restrict availability. [Learn how to use command help](../using-help.md).

## Catalog (91 command paths)

### [Administration](../modules/admin.md) (3)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-announceset` | — | Server owner or required Discord permission | Change how announcements are sent in this guild. |
| `-announceset channel` | — | Server owner or required Discord permission | Change the channel where the bot will send announcements. |
| `-announceset clearchannel` | — | Server owner or required Discord permission | Unsets the channel for announcements. |

### [Core](../modules/core.md) (46)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
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
| `-bankset prune server` | `guild`, `local` | Server owner or required Discord permission | Prune bank accounts for users no longer in the server. |
| `-bankset prune user` | — | Server owner or required Discord permission | Delete the bank account of a specified user. |
| `-bankset registeramount` | — | Server owner or required Discord permission | Set the initial balance for new bank accounts. |
| `-bankset reset` | — | Server owner or required Discord permission | Delete all bank accounts. |
| `-bankset showsettings` | — | Server owner or required Discord permission | Show the current bank settings. |
| `-command` | — | Server owner or required Discord permission | Commands to enable and disable commands and cogs. |
| `-command disable` | — | Server owner or required Discord permission | Disable a command. |
| `-command disable server` | `guild` | Server owner or required Discord permission | Disable a command in this server only. |
| `-command disablecog` | — | Server owner or required Discord permission | Disable a cog in this server. |
| `-command enable` | — | Server owner or required Discord permission | Enable a command. |
| `-command enable server` | `guild` | Server owner or required Discord permission | Enable a command in this server. |
| `-command enablecog` | — | Server owner or required Discord permission | Enable a cog in this server. |
| `-command listdisabled` | — | Server owner or required Discord permission | List disabled commands. |
| `-command listdisabled global` | — | Server owner or required Discord permission | List disabled commands globally. |
| `-command listdisabled guild` | — | Server owner or required Discord permission | List disabled commands in this server. |
| `-command listdisabledcogs` | — | Server owner or required Discord permission | List the cogs which are disabled in this server. |
| `-embedset channel` | — | Server owner or required Discord permission | Set's a channel's embed setting. |
| `-embedset command` | — | Server owner or required Discord permission | Sets a command's embed setting. |
| `-embedset command server` | `guild` | Server owner or required Discord permission | Sets a command's embed setting for the current server. |
| `-embedset server` | `guild` | Server owner or required Discord permission | Set the server's embed setting. |
| `-modlogset` | — | Server owner or required Discord permission | Manage modlog settings. |
| `-modlogset cases` | — | Server owner or required Discord permission | Enable or disable case creation for a mod action. |
| `-modlogset modlog` | `channel` | Server owner or required Discord permission | Set a channel as the modlog. |
| `-modlogset resetcases` | — | Server owner or required Discord permission | Reset all modlog cases in this server. |
| `-set deletedelay` | — | Server owner or required Discord permission | Set the delay until the bot removes the command message. |
| `-set locale` | — | Server owner or required Discord permission | Changes SickGamingBot's locale in this server. |
| `-set locale server` | `guild`, `local` | Server owner or required Discord permission | Changes SickGamingBot's locale in this server. |
| `-set regionalformat` | `region` | Server owner or required Discord permission | Changes the bot's regional format in this server. This is used for formatting date, time and numbers. |
| `-set regionalformat server` | `guild`, `local` | Server owner or required Discord permission | Changes the bot's regional format in this server. This is used for formatting date, time and numbers. |
| `-set roles` | — | Server owner | Set server's admin and mod roles for SickGamingBot. |
| `-set roles addadminrole` | — | Server owner | Adds an admin role for this server. |
| `-set roles addmodrole` | — | Server owner | Adds a moderator role for this server. |
| `-set roles removeadminrole` | `deladminrole`, `deleteadminrole`, `remadmindrole` | Server owner | Removes an admin role for this server. |
| `-set roles removemodrole` | `deletemodrole`, `delmodrole`, `remmodrole` | Server owner | Removes a mod role for this server. |
| `-set serverfuzzy` | — | Server owner | Toggle whether to enable fuzzy command search for the server. |
| `-set usebotcolour` | `usebotcolor` | Server owner | Toggle whether to use the bot owner-configured colour for embeds. |

### [Moderation](../modules/mod.md) (19)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-modset` | — | Server owner or required Discord permission | Manage server administration settings. |
| `-modset defaultdays` | — | Server owner or required Discord permission | Set the default number of days worth of messages to be deleted when a user is banned. |
| `-modset defaultduration` | — | Server owner or required Discord permission | Set the default time to be used when a user is tempbanned. |
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
| `-modset tracknicknames` | — | Server owner or required Discord permission | Toggle whether server nickname changes should be tracked. |

### [Permissions](../modules/permissions.md) (9)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-permissions acl` | `yaml` | Server owner or required Discord permission | Manage permissions with YAML files. |
| `-permissions acl getserver` | `getguild` | Server owner or required Discord permission | Get a YAML file detailing all rules in this server. |
| `-permissions acl setserver` | `setguild` | Server owner or required Discord permission | Set rules for this server with a YAML file. |
| `-permissions acl updateserver` | `updateguild` | Server owner or required Discord permission | Update rules for this server with a YAML file. |
| `-permissions acl yamlexample` | — | Server owner or required Discord permission | Sends an example of the yaml layout for permissions |
| `-permissions addserverrule` | `addguildrule` | Server owner or required Discord permission | Add a rule to a command in this server. |
| `-permissions clearserverrules` | `clearguildrules` | Server owner or required Discord permission | Reset all rules in this server. |
| `-permissions removeserverrule` | `removeguildrule` | Server owner or required Discord permission | Remove a server rule from a command. |
| `-permissions setdefaultserverrule` | `setdefaultguildrule` | Server owner or required Discord permission | Set the default rule for a command in this server. |

### [Warnings](../modules/warnings.md) (14)

| Command | Aliases | Declared access | Description |
| --- | --- | --- | --- |
| `-warnaction` | — | Server owner or required Discord permission | Manage automated actions for Warnings. |
| `-warnaction add` | — | Server owner or required Discord permission | Create an automated action. |
| `-warnaction delete` | `del`, `remove` | Server owner or required Discord permission | Delete the action with the specified name. |
| `-warningset` | — | Server owner or required Discord permission | Manage settings for Warnings. |
| `-warningset allowcustomreasons` | — | Server owner or required Discord permission | Enable or disable custom reasons for a warning. |
| `-warningset mywarnings` | — | Server owner or required Discord permission | Manage the settings for `-mywarnings`. |
| `-warningset mywarnings sendtodms` | — | Server owner or required Discord permission | Whether a member self requesting their warnings with `-mywarnings` should get them sent to DMs or in the current channel. |
| `-warningset senddm` | — | Server owner or required Discord permission | Set whether warnings should be sent to users in DMs. |
| `-warningset showmoderator` | — | Server owner or required Discord permission | Decide whether the name of the moderator warning a user should be included in the DM to that user when being |
| `-warningset usewarnchannel` | — | Server owner or required Discord permission | Set if warnings should be sent to a channel set with `-warningset warnchannel`. |
| `-warningset warnchannel` | — | Server owner or required Discord permission | Set the channel where warnings should be sent to. |
| `-warnreason` | — | Server owner or required Discord permission | Manage warning reasons. |
| `-warnreason create` | `add` | Server owner or required Discord permission | Create a warning reason. |
| `-warnreason delete` | `del`, `remove` | Server owner or required Discord permission | Delete a warning reason. |
