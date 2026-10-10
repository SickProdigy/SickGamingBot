# Integrations

Integrations connect SickGamingBot to an external site or service. Availability varies by deployment and server.

Before enabling one, confirm what it can read or change, whether credentials are guild-wide or personal, who can operate it, how access is revoked, and what happens to stored data.

Use separate, scoped, revocable credentials. Never reuse an administrator password or paste a token into a public channel.

## Connection types

- **Guild connectors** are configured by an administrator or manager and shared by the server.
- **Personal connections** represent one member and should use a private, ownership-verifying flow with an unlink option.
- **Managed service accounts** for Plex, Navidrome, Jellyfin, or similar services require an explicit provisioning, suspension, retention, and removal policy.

## Existing feature guides

- [Stream alerts](../../Streams.md)
- [Welcome messages](../../Welcome-Message.md)
- [Reaction and self-service roles](../../Reaction-Roles.md)

These older pages are being reviewed. Confirm current syntax with -help <command>.
