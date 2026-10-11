# Rocket League

> Rocket League and RLCS news, schedules, standings, clips, and community tools.

## At a glance

- **Category:** Games and gaming communities
- **Intended audience:** Members use information commands; administrators configure announcements and defaults.
- **Loaded package:** `rocketleague`
- **Documented commands:** 46 commands and subcommands

## Main command families

| Command | Default access | Purpose |
| --- | --- | --- |
| `-rlcs` | Member | Show the next RLCS event (short form of rocketleague rlcs). |
| `-rlcsset` | Administrator or required permission | Admin: configure automatic RLCS schedule announcements. |
| `-rocketleague` | Member | Browse Rocket League commands and announcement administration. |
| `-rocketleagueset` | Administrator or required permission | Admin: configure server-specific tournaments and automatic clips. |

## Using this module

Run help for a command family, then add subcommands to request more specific details:

```text
-help rlcs
-help rlcs <subcommand>
```

The bot only shows commands available to your account. Server-specific permission
rules, disabled commands, required integrations, and channel restrictions can change
what you can use.

## Learn more

- [Complete Rocket League command reference](../reference/rocketleague.md)
- [Using SickGamingBot help](../using-help.md)
- [Permissions and access levels](../permissions.md)
