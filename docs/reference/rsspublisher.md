# RSS Publisher commands

Loaded package: `rsspublisher`

Use `-help <command>` for complete syntax and argument details. Access below is
derived from declared command checks; server-specific permission rules can change it.

| Command | Aliases | Access | Description |
| --- | --- | --- | --- |
| `-rsspublisher` | `rss` | Moderator or required Discord permission | Manage this server's RSS and Atom feeds. |
| `-rsspublisher add` | — | Moderator or required Discord permission | Add an RSS feed to a channel. |
| `-rsspublisher announce` | `announcement` | Moderator or required Discord permission | Set normal content sent with each post; omit it to clear. |
| `-rsspublisher embed` | — | Moderator or required Discord permission | Embed feed settings. |
| `-rsspublisher embed color` | `colour` | Moderator or required Discord permission | Set an embed color for a feed. |
| `-rsspublisher embed image` | — | Moderator or required Discord permission | Set a tag to be a large embed image. |
| `-rsspublisher embed thumbnail` | — | Moderator or required Discord permission | Set a tag to be a thumbnail image. |
| `-rsspublisher embed toggle` | — | Moderator or required Discord permission | Toggle whether a feed is sent in an embed or not. |
| `-rsspublisher filter` | — | Moderator or required Discord permission | Filter feed entries by title prefix or exact author. |
| `-rsspublisher filter author` | — | Moderator or required Discord permission | Manage the exact author allowlist. |
| `-rsspublisher filter author allow` | `add` | Moderator or required Discord permission | Allow an exact author name after plaintext normalization. |
| `-rsspublisher filter author list` | — | Moderator or required Discord permission | List exact allowed authors for a feed. |
| `-rsspublisher filter author remove` | `delete` | Moderator or required Discord permission | Remove an exact author from the allowlist. |
| `-rsspublisher filter show` | — | Moderator or required Discord permission | Show active title, author, and tag filters for a feed. |
| `-rsspublisher filter titleprefix` | `title` | Moderator or required Discord permission | Set a case-insensitive title prefix; use `clear` to remove it. |
| `-rsspublisher find` | — | Moderator or required Discord permission | Attempts to find RSS feeds from a URL/website. |
| `-rsspublisher force` | `test`, `preview` | Moderator or required Discord permission | Preview the newest feed entry without advancing its saved marker. |
| `-rsspublisher limit` | — | Moderator or required Discord permission | Set a character limit for feed posts. Use 0 for unlimited. |
| `-rsspublisher list` | — | Moderator or required Discord permission | List saved feeds and their delivery settings for one channel. |
| `-rsspublisher listall` | — | Moderator or required Discord permission | List all server feeds with their delivery settings. |
| `-rsspublisher listtags` | — | Moderator or required Discord permission | List the tags available from a specific feed. |
| `-rsspublisher migrationstatus` | — | Bot maintainer | Owner: show legacy RSS migration status. |
| `-rsspublisher mode` | — | Moderator or required Discord permission | Set a feed to post only the latest entry or catch up on every unseen entry. |
| `-rsspublisher parse` | — | Bot maintainer | Change feed parsing for a specfic domain. |
| `-rsspublisher parse add` | — | Bot maintainer | Add a website to the list for a time parsing override. |
| `-rsspublisher parse list` | — | Bot maintainer | Show the list for time parsing overrides. |
| `-rsspublisher parse remove` | `delete`, `del` | Bot maintainer | Remove a website from the list for a time parsing override. |
| `-rsspublisher pause` | — | Moderator or required Discord permission | Pause automatic checks for a feed without removing its configuration. |
| `-rsspublisher privatehost` | — | Bot maintainer | Manage private feed hosts that the bot owner intentionally trusts. |
| `-rsspublisher privatehost add` | — | Bot maintainer | Allow one private hostname or IP address for RSS requests. |
| `-rsspublisher privatehost list` | — | Bot maintainer | List private RSS hosts explicitly trusted by the bot owner. |
| `-rsspublisher privatehost remove` | `delete` | Bot maintainer | Remove a private hostname or IP address from the RSS allowlist. |
| `-rsspublisher remove` | `delete`, `del` | Moderator or required Discord permission | Removes a feed from a channel. |
| `-rsspublisher resume` | — | Moderator or required Discord permission | Resume automatic checks for a paused feed. |
| `-rsspublisher showtemplate` | — | Moderator or required Discord permission | Show the template in use for a specific feed. |
| `-rsspublisher status` | — | Moderator or required Discord permission | Show delivery mode and recent health for a feed. |
| `-rsspublisher tag` | — | Moderator or required Discord permission | RSS post tag qualification. |
| `-rsspublisher tag allow` | — | Moderator or required Discord permission | Set an allowed tag for a feed to be posted. The tag must match exactly (without regard to title casing). |
| `-rsspublisher tag allowlist` | — | Moderator or required Discord permission | List allowed tags for feed post qualification. |
| `-rsspublisher tag remove` | `delete` | Moderator or required Discord permission | Remove a tag from the allow list. The tag must match exactly (without regard to title casing). |
| `-rsspublisher template` | — | Moderator or required Discord permission | Set a template for the feed alert. |
| `-rsspublisher version` | — | Moderator or required Discord permission | Show the RSS version. |
| `-rsspublisher view` | `info`, `settings` | Moderator or required Discord permission | Show complete settings and delivery health for one feed. |
| `-rsspublisher viewtags` | — | Moderator or required Discord permission | View a preview of template tag content available from a specific feed. |

Live `-help` output remains authoritative for enabled state, hidden commands,
arguments, cooldowns, and server-specific access.
