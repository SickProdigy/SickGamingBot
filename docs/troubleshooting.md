# Troubleshooting

Start with `-help`, then use `-help <command>` or
`-help <command> <subcommand>`. Live help reflects your account, channel, enabled
modules, and current permission rules.

## A command is missing or denied

Check the `-` prefix and exact command path. The cog or command may be disabled,
blocked in the channel, restricted by Discord permissions or role hierarchy, or hidden
from your account. Try help in the intended channel and ask server staff to compare
their result. Owners can review disabled commands and the server Permissions ACL.

## The bot does not respond

Confirm that the bot is online and can view the channel, read message history when
needed, send messages, and embed links. Try `-help` once in the server's bot channel
and once in direct messages. Do not repeatedly submit commands that create posts,
roles, accounts, or external resources.

## A role or moderation action fails

The bot's highest role must be above the target role and member. Discord ownership,
protected roles, channel overwrites, and missing Manage Roles/Manage Messages
permissions can still block an otherwise authorized command. Keep the bot role only as
high as necessary.

## Music, feeds, or scheduled posts fail

Check the configured destination, the bot's send/embed/attach permissions, whether the
feature is enabled, and its status/settings command. Use preview or test before
re-enabling a schedule. A provider outage or missing global credential requires a
SickGamingBot maintainer; server owners should not attempt host commands.

## An external integration fails

Check the selected connection, endpoint, account scopes, and revocation state through
the documented private setup flow. Never paste tokens into chat or an issue. Disconnect
and reconnect only when the feature documents that workflow; repeated retries can
create duplicate accounts or posts.

## Gather a useful report

Include:

- The full command path, without secrets.
- Approximate time and timezone.
- Expected result and sanitized error text.
- Whether it affects one user, one channel, one server, or several servers.
- Which status/test command was tried.
- Screenshots only after removing private messages, tokens, and personal data.

See [Using help](using-help.md), [Permissions](permissions.md), and
[Privacy and data](privacy-and-data.md).
