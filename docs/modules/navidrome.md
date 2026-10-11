# Navidrome

> Member account and administrator workflows for the connected Navidrome music service.

## At a glance

- **Category:** Music, media, and feeds
- **Intended audience:** Members manage their service access; administrators manage guild integration settings.
- **Loaded package:** `navidrome`
- **Documented commands:** 32 commands and subcommands

## Main command families

| Command | Default access | Purpose |
| --- | --- | --- |
| `-navidrome` | Member | Show this server's Navidrome library information. |
| `-navidromeowner` | Bot maintainer | Manage bot-owner-approved Navidrome connections. |
| `-navidromeset` | Administrator or required permission | Configure this server's Navidrome connection and announcements. |

## Using this module

Run help for a command family, then add subcommands to request more specific details:

```text
-help navidrome
-help navidrome <subcommand>
```

The bot only shows commands available to your account. Server-specific permission
rules, disabled commands, required integrations, and channel restrictions can change
what you can use.

## Learn more

- [Complete Navidrome command reference](../reference/navidrome.md)
- [Using SickGamingBot help](../using-help.md)
- [Permissions and access levels](../permissions.md)
