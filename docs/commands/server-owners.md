# Server-owner commands

A Discord server owner normally uses the same guild configuration as an administrator.
Ownership does not grant access to the bot host or Red bot-owner commands.

Start with `[p]help`, then review direct help for `[p]command`, `[p]modset`,
`[p]modlogset`, `[p]warningset`, and `[p]muteset`.

## Guild-wide command families

- `[p]command` for guild command and cog availability
- `[p]localallowlist` and `[p]localblocklist` for guild access policy
- `[p]ignore` and `[p]unignore` for ignored locations
- `[p]embedset`, `[p]helpset`, and `[p]inviteset` for guild-facing core behavior
- `[p]modset`, `[p]modlogset`, `[p]warningset`, and `[p]muteset` for moderation policy
- `[p]selfroleset`, `[p]roletools`, and `[p]gameroleset` for member role systems
- `[p]welcomeset`, `[p]streamset`, `[p]rss`, `[p]movieset`, and game integration
  `*set` commands for optional features

Use narrow manager roles for day-to-day operation. Keep sensitive setup in a private
staff channel and never paste credentials into public chat.

Commands that load code, install repositories or dependencies, restart or shut down
the process, manage global credentials, enumerate every guild, or change host-wide
policy belong to SickGaming maintainers.

See the [staff command guide](staff.md) for the shared moderation and configuration list.
