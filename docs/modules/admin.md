# Administration

> Role management, self-roles, announcements, and restricted global administration.

## At a glance

- **Category:** Community and server management
- **Intended audience:** Members can use self-roles; administrators and maintainers manage configuration.
- **Loaded package:** `admin`
- **Documented commands:** 19 commands and subcommands

## Main command families

| Command | Default access | Purpose |
| --- | --- | --- |
| `-addrole` | Administrator or required permission | Add a role to a user. |
| `-announce` | Bot maintainer | Announce a message to all servers the bot is in. |
| `-announceset` | Server owner or required permission | Change how announcements are sent in this guild. |
| `-editrole` | Administrator or required permission | Edit role settings. |
| `-removerole` | Administrator or required permission | Remove a role from a user. |
| `-selfrole` | Member | Add or remove a selfrole from yourself. |
| `-selfroleset` | Administrator or required permission | Manage selfroles. |
| `-serverlock` | Bot maintainer | Lock a bot to its current servers only. |

## Using this module

Run help for a command family, then add subcommands to request more specific details:

```text
-help addrole
-help addrole <subcommand>
```

The bot only shows commands available to your account. Server-specific permission
rules, disabled commands, required integrations, and channel restrictions can change
what you can use.

## Learn more

- [Complete Administration command reference](../reference/admin.md)
- [Using SickGamingBot help](../using-help.md)
- [Permissions and access levels](../permissions.md)
