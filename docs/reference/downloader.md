# Downloader commands

Loaded package: `Downloader`

## Reading this reference

Each command is shown as its complete path. To see detailed help, put that path after
`-help` without repeating the leading hyphen:

```text
-help <command>
-help <command> <subcommand>
-help <command> <subcommand> <nested-subcommand>
```

The access column comes from the command checks declared by the running bot. Live
permissions, disabled commands, parent checks, role hierarchy, and server rules can
further restrict availability. See [Using SickGamingBot help](../using-help.md).

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
| `-repo delete` | `del`, `remove` | Bot maintainer | Remove repos and their files. |
| `-repo info` | — | Bot maintainer | Show information about a repo. |
| `-repo list` | — | Bot maintainer | List all installed repos. |
| `-repo update` | — | Bot maintainer | Update all repos, or ones of your choosing. |

Live `-help` output remains authoritative for syntax, enabled state, hidden commands,
arguments, cooldowns, and server-specific access.
