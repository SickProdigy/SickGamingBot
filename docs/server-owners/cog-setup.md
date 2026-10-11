# Cog setup guide for server owners

Not every loaded cog needs configuration. Member utilities often work immediately, while
moderation, roles, announcements, feeds, and external services need an owner or
administrator to choose channels, roles, policy, and delivery behavior.

This is a setup guide, not a command dump. Follow each module link for its overview and
complete reference.

## Safe setup pattern

For every cog you enable:

1. Read `-help <command-family>`.
2. Decide which channel, role, and staff position owns the feature.
3. Grant only the Discord permissions the cog needs.
4. Configure it in a private staff channel.
5. Use its status, settings, preview, or test command when available.
6. Test member behavior with a non-owner account.
7. Record how to disable it and remove any external connection.

“Administrator or required permission” can often be delegated without granting Discord
Administrator. See the [permission model](../permissions.md).

## Foundation and command policy

| Module | Owner decisions | Start with | Verify |
| --- | --- | --- | --- |
| [Core](../modules/core.md) | Enabled cogs/commands, allowed locations, and server-facing embeds | `-help command`, `-help ignore`, `-help embedset` | `-command listdisabled` and live `-help` in the intended channel |
| [Permissions](../modules/permissions.md) | Server allow/deny rules beyond Discord permissions | `-help permissions` | Review or export the server ACL before and after changes |
| [Administration](../modules/admin.md) | Available self-roles and the channel for global announcements delivered to this server | `-help selfroleset`, `-help announceset` | `-selfrole list` from a member account |
| [Aliases](../modules/alias.md) | Whether staff may create local command names | `-help alias` | `-alias list` |
| [Custom Commands](../modules/customcom.md) | Who creates commands, responses, cooldowns, and naming conflicts | `-help customcom` | `-customcom list` and `-customcom show <name>` |

Use permission overrides sparingly. Broad rules can make live help differ between
owners, staff, channels, and members.

## Moderation and safety

Configure these cogs together as one moderation policy.

| Module | Owner decisions | Start with | Verify or test |
| --- | --- | --- | --- |
| [Moderation](../modules/mod.md) | Required reasons, ban defaults, user DMs, repeats, mention spam, and nickname tracking | `-help modset` | `-modset showsettings` |
| [Moderation Log](../modules/modlog.md) | Case channel and which actions create cases | `-help modlogset` | Review settings, then perform a reversible test |
| [Mutes](../modules/mutes.md) | Muted role, duration, user DMs, moderator visibility, and failure channel | `-help muteset` | `-muteset settings` and a short test mute |
| [Warnings](../modules/warnings.md) | Reasons, points, automated actions, expiry, and custom reasons | `-help warningset`, `-help warnreason`, `-help warnaction` | Review reasons and actions before a test |
| [Reports](../modules/reports.md) | Whether reports are enabled and their private staff destination | `-help reportset` | Confirm output/toggle, then submit a test report |
| [Filter](../modules/filter.md) | Server/channel terms, name filtering, and automatic actions | `-help filter`, `-help filterset` | List filters and test in a controlled channel |
| [Cleanup](../modules/cleanup.md) | Who may delete messages and acceptable bulk-cleanup scope | `-help cleanup` | Test with a few disposable messages |

Document automatic-action thresholds and keep the bot role below roles it must never
affect.

## Roles, onboarding, and community operation

| Module | Owner decisions | Start with | Verify or test |
| --- | --- | --- | --- |
| [Welcome](../modules/welcome.md) | Welcome/goodbye channels, messages, embeds, and public visibility | `-help welcomeset` | Use a test command if offered or review all settings |
| [Administration self-roles](../modules/admin.md) | Roles members may add or remove themselves | `-help selfroleset` | `-selfrole list` and add/remove tests |
| [Role Tools](../modules/roletools.md) | Advanced self-service behavior and hierarchy limits | `-help roletools` | `-selfroles` from a member account |
| [Game Roles](../modules/gameroles.md) | Game profiles, approved roles, and delegated manager roles | `-help gameroleset` | `-gameroleset show <game>` and the member dashboard |
| [Giveaways](../modules/giveaways.md) | Operators, entrants, channel, duration, and winner count | `-help giveaway` | Run a short private giveaway |

The bot role must be above roles it assigns or edits. Do not place it above administrator
or ownership roles merely for convenience.

## Feeds and scheduled announcements

Each publisher needs a destination, posting policy, and staff owner. Preview first so
enabling it does not flood a public channel.

| Module | Owner decisions | Start with | Verify before enabling |
| --- | --- | --- | --- |
| [Streams](../modules/streams.md) | Sources, alert channels, mentions, and message format | `-help streamalert`, `-help streamset` | List alerts and test the destination |
| [RSS Publisher](../modules/rsspublisher.md) | Feed, channel, delivery mode, filters, template, embed, and pause ownership | `-help rsspublisher` | Use `force`, `status`, or `view` |
| [Movie Releases](../modules/movies.md) | Channel, date window, vote threshold, daily cap, and mention role | `-help movieset` | `-movieset preview` and `-movieset settings` |
| [Meme](../modules/meme.md) | Whether automatic feeds are appropriate and where they post | `-help memeset` | Review settings and preview privately |
| [ARK](../modules/ark.md) | Channel, categories, interval, presentation, and mention role | `-help arkset` | `-arkset preview` and `-arkset status` |
| [DayZ](../modules/dayz.md) | Channel, categories, interval, presentation, and mention role | `-help dayzset` | Preview and status subcommands |
| [Icarus](../modules/icarus.md) | Channel, categories, interval, presentation, and mention role | `-help icarusset` | Preview and status subcommands |
| [Garry's Mod](../modules/gmod.md) | Game-server address, status channel, Steam announcements, and schedule | `-help gmodset` | Review status and test each destination |
| [Rocket League](../modules/rocketleague.md) | Tournaments, clip sources/channel/interval, and RLCS schedule channel | `-help rocketleagueset`, `-help rlcsset` | Status/list commands and a controlled `postnow` |
| [Age-Restricted](../modules/nsfw.md) | Whether it is allowed and which age-restricted channel may receive a feed | `-help nsfwset` | Confirm channel restrictions, then preview |

Age-restricted content must never be configured in a general-access channel.

## External and game-service connections

Provider credentials may already be configured globally by a SickGamingBot maintainer.
Owners select approved connections or supply server identifiers; they do not receive
global credentials.

| Module | Server setup | Start with | Boundary |
| --- | --- | --- | --- |
| [Navidrome](../modules/navidrome.md) | Approved connection, channel, interval, quiet hours, notifications, and account policy | `-help navidromeset setup` | A maintainer approves connections; passwords stay private |
| [Clash of Clans](../modules/coc.md) | Clan, war channel, timezone, events, mention role, and manager role | `-help cocset` | Set the manager role before delegating |
| [Rocket League](../modules/rocketleague.md) | start.gg/Challonge events and approved clip URLs | `-help rocketleagueset` | Credentials are global; subscriptions are server-specific |
| [Garry's Mod](../modules/gmod.md) | Public server details and announcement destinations | `-help gmodset` | Never publish administration credentials |
| [Wolfram](../modules/wolfram.md) | Usually only command/cog availability | `-help wolfram` | Provider credentials are maintainer-managed |
| [Image](../modules/image.md) | Usually only channel and command policy | `-help gif`, `-help imgur` | Provider credentials are maintainer-managed |

Never post tokens, passwords, recovery codes, or private keys. If a provider is
unavailable, contact a maintainer instead of trying bot-host commands.

## Optional systems with server policy

| Module | Owner decisions | Start with |
| --- | --- | --- |
| [Audio](../modules/audio.md) | DJ mode, volume/length limits, autoplay, disconnect behavior, restrictions, and economy charges | `-help audioset` |
| [Economy](../modules/economy.md) | Currency and balance limits, payday, role bonuses, and slot limits | `-help bankset`, `-help economyset` |
| [Trivia](../modules/trivia.md) | Timing, payouts, and server defaults; custom-list files remain maintainer-managed | `-help triviaset` |
| [Pokémon](../modules/pokemon.md) | Channels, spawn mode/timing, lifetime, generations, battles, and Pokémon Center | `-help pokemonset` |

Avatar, Dictionary, General, RuneScape lookups, and ordinary search commands normally
need no server setup beyond deciding whether the cog or command is enabled.

## Finish the rollout

- Re-run `-help` as an owner, staff member, and ordinary member.
- Confirm automatic posts use only their intended channels.
- Confirm the bot cannot manage protected roles or users above it.
- Publish the [member guide](../members/index.md) and [staff guide](../staff/index.md).
- Use the [server-owner command catalog](../commands/server-owners.md) for exact paths,
  but use live help for arguments and current checks.
