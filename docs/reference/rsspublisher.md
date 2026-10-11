# RSS Publisher commands

Loaded package: `RSS`

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
| `-rsspublisher` | `rss` | Moderator or required Discord permission | Manage this server's RSS and Atom feeds. |
| `-rsspublisher add` | — | Moderator or required Discord permission | Add a feed. |
| `-rsspublisher announce` | `announcement` | Moderator or required Discord permission | Set announcement text. |
| `-rsspublisher embed` | — | Moderator or required Discord permission | Configure feed embeds. |
| `-rsspublisher embed color` | `colour` | Moderator or required Discord permission | Set an embed color for a feed. |
| `-rsspublisher embed image` | — | Moderator or required Discord permission | Set a tag to be a large embed image. |
| `-rsspublisher embed thumbnail` | — | Moderator or required Discord permission | Set a tag to be a thumbnail image. |
| `-rsspublisher embed toggle` | — | Moderator or required Discord permission | Toggle whether a feed is sent in an embed or not. |
| `-rsspublisher filter` | — | Moderator or required Discord permission | Filter entries by title or author. |
| `-rsspublisher filter author` | — | Moderator or required Discord permission | Manage the exact author allowlist. |
| `-rsspublisher filter author allow` | `add` | Moderator or required Discord permission | Allow an exact author name after plaintext normalization. |
| `-rsspublisher filter author list` | — | Moderator or required Discord permission | List exact allowed authors for a feed. |
| `-rsspublisher filter author remove` | `delete` | Moderator or required Discord permission | Remove an exact author from the allowlist. |
| `-rsspublisher filter show` | — | Moderator or required Discord permission | Show active title, author, and tag filters for a feed. |
| `-rsspublisher filter titleprefix` | `title` | Moderator or required Discord permission | Set a case-insensitive title prefix; use `clear` to remove it. |
| `-rsspublisher find` | — | Moderator or required Discord permission | Find feeds on a website. |
| `-rsspublisher force` | `preview`, `test` | Moderator or required Discord permission | Preview the newest entry. |
| `-rsspublisher limit` | — | Moderator or required Discord permission | Set the post length limit. |
| `-rsspublisher list` | — | Moderator or required Discord permission | List feeds in one channel. |
| `-rsspublisher listall` | — | Moderator or required Discord permission | List every server feed. |
| `-rsspublisher listtags` | — | Moderator or required Discord permission | List available feed tags. |
| `-rsspublisher migrationstatus` | — | Bot maintainer | Show migration status. |
| `-rsspublisher mode` | — | Moderator or required Discord permission | Set latest or catch-up mode. |
| `-rsspublisher parse` | — | Bot maintainer | Manage domain parsing. |
| `-rsspublisher parse add` | — | Bot maintainer | Add a website to the list for a time parsing override. |
| `-rsspublisher parse list` | — | Bot maintainer | Show the list for time parsing overrides. |
| `-rsspublisher parse remove` | `del`, `delete` | Bot maintainer | Remove a website from the list for a time parsing override. |
| `-rsspublisher pause` | — | Moderator or required Discord permission | Pause a feed. |
| `-rsspublisher privatehost` | — | Bot maintainer | Manage trusted private hosts. |
| `-rsspublisher privatehost add` | — | Bot maintainer | Allow one private hostname or IP address for RSS requests. |
| `-rsspublisher privatehost list` | — | Bot maintainer | List private RSS hosts explicitly trusted by the bot owner. |
| `-rsspublisher privatehost remove` | `delete` | Bot maintainer | Remove a private hostname or IP address from the RSS allowlist. |
| `-rsspublisher remove` | `del`, `delete` | Moderator or required Discord permission | Remove a feed. |
| `-rsspublisher resume` | — | Moderator or required Discord permission | Resume a feed. |
| `-rsspublisher showtemplate` | — | Moderator or required Discord permission | Show a feed template. |
| `-rsspublisher status` | — | Moderator or required Discord permission | Show feed health. |
| `-rsspublisher tag` | — | Moderator or required Discord permission | Manage tag filters. |
| `-rsspublisher tag allow` | — | Moderator or required Discord permission | Set an allowed tag for a feed to be posted. The tag must match exactly (without regard to title casing). |
| `-rsspublisher tag allowlist` | — | Moderator or required Discord permission | List allowed tags for feed post qualification. |
| `-rsspublisher tag remove` | `delete` | Moderator or required Discord permission | Remove a tag from the allow list. The tag must match exactly (without regard to title casing). |
| `-rsspublisher template` | — | Moderator or required Discord permission | Set a feed template. |
| `-rsspublisher version` | — | Moderator or required Discord permission | Show the RSS version. |
| `-rsspublisher view` | `info`, `settings` | Moderator or required Discord permission | View one feed's settings. |
| `-rsspublisher viewtags` | — | Moderator or required Discord permission | Preview rendered tag values. |

Live `-help` output remains authoritative for syntax, enabled state, hidden commands,
arguments, cooldowns, and server-specific access.
