# Moderator and administrator guide

Staff access is split between moderation and administration. A custom manager role may operate one feature without receiving broader Discord permissions.

“Staff” means staff of the Discord server using the bot. SickGaming community staff
do not automatically receive moderation powers in someone else's server. See
[Permissions](../permissions.md).

## Moderators and delegated managers

Typical responsibilities include warnings, mutes, reports, cleanup, incident handling, moderation history, giveaways, and delegated announcement or integration tasks.

Delegated access is feature-specific. It does not imply Discord Administrator, server ownership, or bot-host access.

## Administrators

Administrators may configure guild-wide command and channel policy; welcome, role, stream, feed, and event settings; integration endpoints; manager roles; and sensitive Discord permissions needed by features.

Use the least privilege that supports the task. Do not grant Discord Administrator merely to make one command work.

## Safe operation

- Use -help <command> before a destructive or unfamiliar action.
- Enter credentials only through a documented private flow.
- Test configuration in a private staff channel when possible.
- Treat role hierarchy and channel overwrites as part of effective access.
- Escalate bot-host failures to a SickGaming maintainer.

See [Permissions](../permissions.md), [Privacy and data](../privacy-and-data.md), and [Troubleshooting](../troubleshooting.md).

## Complete staff catalog

The [staff command catalog](../commands/staff.md) lists all 412 command paths whose
declared checks require moderation, administration, or a specific Discord permission.
Staff also retain the [300 member command paths](../commands/members.md).

Commands reserved specifically for a Discord server owner are listed separately in
the [server-owner catalog](../commands/server-owners.md). Host-wide operations are
reserved for [SickGamingBot maintainers](../commands/maintainers.md).
