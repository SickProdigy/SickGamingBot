# Server-owner guide

This guide is for the owner of a Discord server using SickGamingBot. It covers guild setup and policy, not maintenance of the hosted bot process.

## Invite SickGamingBot

Send `-invite` in a direct message to SickGamingBot, or use the published
[SickGamingBot invite](https://discord.com/oauth2/authorize?client_id=691452746632658954&scope=bot&permissions=0).
You must be allowed to manage the Discord server where you add the bot.

## Start here

1. Follow the [initial setup checklist](initial-setup.md).
2. Review the [permission model](../permissions.md).
3. Configure only the [integrations](integrations.md) your community needs.
4. Delegate feature management through narrow Discord or feature-specific roles.
5. Publish member and staff guidance appropriate to your server.

## Your responsibilities

- Decide where the bot may read, send, embed, react, and manage messages.
- Decide which roles may moderate or manage individual features.
- Approve server-specific external connections and their data use.
- Review destructive actions and retention behavior before enabling them.
- Remove integrations and bot access when no longer needed.

The bot host controls installed code, global credentials, restarts, infrastructure, and global policy. Server ownership does not provide those controls.

## Complete owner catalog

The [server-owner command catalog](../commands/server-owners.md) lists all 93 command
paths that declare server ownership or an equivalent Discord permission as their
primary boundary. Owners also retain the [staff commands](../commands/staff.md) and
[member commands](../commands/members.md).

The separate [bot-maintainer catalog](../commands/maintainers.md) makes the boundary
explicit: owning a Discord server does not grant access to the bot process, global
configuration, installed code, or cross-server operations.
