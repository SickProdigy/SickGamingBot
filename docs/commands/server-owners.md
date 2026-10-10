# Server-owner commands

A Discord server owner normally uses the same guild configuration as an administrator.
Ownership does not grant access to the bot host or Red bot-owner commands.

Start with `-help`, then review direct help for `-command`, `-modset`,
`-modlogset`, `-warningset`, and `-muteset`.

## Guild-wide command families

- `-command` for guild command and cog availability
- `-localallowlist` and `-localblocklist` for guild access policy
- `-ignore` and `-unignore` for ignored locations
- `-embedset`, `-helpset`, and `-inviteset` for guild-facing core behavior
- `-modset`, `-modlogset`, `-warningset`, and `-muteset` for moderation policy
- `-selfroleset`, `-roletools`, and `-gameroleset` for member role systems
- `-welcomeset`, `-streamset`, `-rss`, `-movieset`, and game integration
  `*set` commands for optional features

Use narrow manager roles for day-to-day operation. Keep sensitive setup in a private
staff channel and never paste credentials into public chat.

Commands that load code, install repositories or dependencies, restart or shut down
the process, manage global credentials, enumerate every guild, or change host-wide
policy belong to SickGaming maintainers.

See the [staff command guide](staff.md) for the shared moderation and configuration list.
