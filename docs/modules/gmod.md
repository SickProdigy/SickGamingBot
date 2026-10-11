# Garry's Mod

> Garry’s Mod server status, player information, Steam details, and scheduled announcements.

## At a glance

- **Category:** Games and gaming communities
- **Intended audience:** Members use lookups; administrators configure servers and announcements.
- **Loaded package:** `gmod`
- **Documented commands:** 25 commands and subcommands

## Main command families

| Command | Default access | Purpose |
| --- | --- | --- |
| `-gmod` | Member | Show Garry's Mod server status and browse official updates. |
| `-gmodowner` | Bot maintainer | Manage bot-owner-only GMod network policy. |
| `-gmodset` | Administrator or required permission | Configure Garry's Mod status and Steam announcements. |

## Using this module

Run help for a command family, then add subcommands to request more specific details:

```text
-help gmod
-help gmod <subcommand>
```

The bot only shows commands available to your account. Server-specific permission
rules, disabled commands, required integrations, and channel restrictions can change
what you can use.

## Learn more

- [Complete Garry's Mod command reference](../reference/gmod.md)
- [Using SickGamingBot help](../using-help.md)
- [Permissions and access levels](../permissions.md)
