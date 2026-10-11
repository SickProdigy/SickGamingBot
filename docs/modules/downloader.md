# Downloader

> Cog repository, installation, dependency, and update management.

## At a glance

- **Category:** Bot administration
- **Intended audience:** SickGaming maintainers only.
- **Loaded package:** `downloader`
- **Documented commands:** 22 commands and subcommands

## Main command families

| Command | Default access | Purpose |
| --- | --- | --- |
| `-cog` | Bot maintainer | Base command for cog installation management commands. |
| `-findcog` | Member | Find which cog a command comes from. |
| `-pipinstall` | Bot maintainer | Install a group of dependencies using pip. |
| `-repo` | Bot maintainer | Base command for repository management. |

## Using this module

Run help for a command family, then add subcommands to request more specific details:

```text
-help cog
-help cog <subcommand>
```

The bot only shows commands available to your account. Server-specific permission
rules, disabled commands, required integrations, and channel restrictions can change
what you can use.

## Learn more

- [Complete Downloader command reference](../reference/downloader.md)
- [Using SickGamingBot help](../using-help.md)
- [Permissions and access levels](../permissions.md)
