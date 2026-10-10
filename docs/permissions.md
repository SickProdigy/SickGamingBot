# Permissions

Access is determined at runtime, not by documentation alone. The effective result can
include Discord guild and channel permissions, role hierarchy, Red command checks,
server-specific Red Permissions rules, disabled commands or cogs, feature-manager
roles, and required integrations.

| Audience | Intended scope |
| --- | --- |
| Member | Everyday commands and actions affecting the member's own account |
| Moderator | Routine moderation and incident response |
| Administrator | Guild-wide configuration and sensitive management |
| Server Owner | Guild ownership decisions and initial integration approval |
| SickGaming Maintainer | Bot process, code, global credentials, infrastructure, and global policy |

## SickGaming staff and other servers

“SickGaming staff” is a community role, not a separate Red permission level. In the
official SickGaming Discord, its roles may be configured as moderator, administrator,
or feature-manager roles. In another Discord server, that server's owner decides who
receives those permissions. Being SickGaming staff does not automatically grant
moderator or administrator commands there.

SickGaming maintainers are different from SickGaming community staff. Maintainers can
operate the hosted bot and may have Red bot-owner access. Those global capabilities are
not part of the public moderator or server-owner command sets.

## How Red levels relate

Discord Administrator, Discord server ownership, and Red bot ownership are different
things. A Discord server owner can control commands in their guild except global or
host-level operations. Moderators handle routine moderation; administrators configure
guild-wide behavior; delegated manager roles can control a single feature.

Audience labels are not a security control. Use `-help` and direct command help to see
the current result for your account. See the [complete command reference](reference/index.md)
for source-derived access labels.
