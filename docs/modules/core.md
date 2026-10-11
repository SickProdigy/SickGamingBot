# Core

> Help, invitations, personal-data controls, server settings, and bot-host operations.

## At a glance

- **Category:** Getting started and bot controls
- **Intended audience:** Everyone; configuration and host operations are restricted by command.
- **Availability:** Always-loaded Red core
- **Documented commands:** 182 commands and subcommands

## Main command families

| Command | Default access | Purpose |
| --- | --- | --- |
| `-allowlist` | Bot maintainer | Commands to manage the allowlist. |
| `-autoimmune` | Server owner or required permission | Commands to manage server settings for immunity from automated actions. |
| `-bankset` | Server owner or required permission | Base command for bank settings. |
| `-blocklist` | Bot maintainer | Commands to manage the blocklist. |
| `-command` | Server owner or required permission | Commands to enable and disable commands and cogs. |
| `-contact` | Member | Sends a message to the owner. |
| `-datapath` | Bot maintainer | Prints the bot's data path. |
| `-debuginfo` | Bot maintainer | Shows debug information useful for debugging. |
| `-diagnoseissues` | Bot maintainer | Diagnose issues with the command checks with ease! |
| `-dm` | Bot maintainer | Sends a DM to a user. |
| `-embedset` | Member | Commands for toggling embeds on or off. |
| `-help` | Member | Shows commands available to you or detailed help for one command. |
| `-helpset` | Bot maintainer | Commands to manage settings for the help command. |
| `-ignore` | Member | Commands to add servers or channels to the ignore list. |
| `-info` | Member | Shows info about SickGamingBot. |
| `-invite` | Member | Shows SickGamingBot's invite url. |
| `-inviteset` | Bot maintainer | Commands to setup SickGamingBot's invite settings. |
| `-leave` | Bot maintainer | Leaves servers. |
| `-licenseinfo` | Member | Get info about Red's licenses. |
| `-load` | Bot maintainer | Loads cog packages from the local paths and installed cogs. |
| `-localallowlist` | Administrator or required permission | Commands to manage the server specific allowlist. |
| `-localblocklist` | Administrator or required permission | Commands to manage the server specific blocklist. |
| `-modlogset` | Server owner or required permission | Manage modlog settings. |
| `-mydata` | Member | Commands which interact with the data SickGamingBot has about you. |
| `-ping` | Member | Pong. |
| `-reload` | Bot maintainer | Reloads cog packages. |
| `-restart` | Bot maintainer | Attempts to restart SickGamingBot. |
| `-servers` | Bot maintainer | Lists the servers SickGamingBot is currently in. |
| `-set` | Member | Commands for changing SickGamingBot's settings. |
| `-shutdown` | Bot maintainer | Shuts down the bot. |
| `-slash` | Bot maintainer | Base command for managing what application commands are able to be used on SickGamingBot. |
| `-traceback` | Bot maintainer | Sends to the owner the last command exception that has occurred. |
| `-unignore` | Member | Commands to remove servers or channels from the ignore list. |
| `-unload` | Bot maintainer | Unloads previously loaded cog packages. |
| `-uptime` | Member | Shows SickGamingBot's uptime. |

## Using this module

Run help for a command family, then add subcommands to request more specific details:

```text
-help allowlist
-help allowlist <subcommand>
```

The bot only shows commands available to your account. Server-specific permission
rules, disabled commands, required integrations, and channel restrictions can change
what you can use.

## Learn more

- [Complete Core command reference](../reference/core.md)
- [Using SickGamingBot help](../using-help.md)
- [Permissions and access levels](../permissions.md)
