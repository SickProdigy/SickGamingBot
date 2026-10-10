# Downloader commands

Loaded package: `downloader`

Use `-help <command>` for complete syntax and argument details. Access below is
derived from declared command checks; server-specific permission rules can change it.

| Command | Aliases | Access | Description |
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
| `-findcog` | — | Member | Find which cog a command comes from. |
| `-pipinstall` | — | Bot maintainer | Install a group of dependencies using pip. |
| `-repo` | — | Bot maintainer | Base command for repository management. |
| `-repo add` | — | Bot maintainer | Add a new repo. |
| `-repo delete` | `remove`, `del` | Bot maintainer | Remove repos and their files. |
| `-repo info` | — | Bot maintainer | Show information about a repo. |
| `-repo list` | — | Bot maintainer | List all installed repos. |
| `-repo update` | — | Bot maintainer | Update all repos, or ones of your choosing. |

Live `-help` output remains authoritative for enabled state, hidden commands,
arguments, cooldowns, and server-specific access.
