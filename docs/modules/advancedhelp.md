# Advanced Help

> Interactive, permission-aware help plus a sanitized maintainer command inventory.

## At a glance

- **Category:** Getting started and bot controls
- **Intended audience:** Everyone uses the help menu; SickGamingBot maintainers configure it and export command metadata.
- **Loaded package:** `advancedhelp`
- **Documented commands:** 19 commands and subcommands

## Main command families

| Command | Default access | Purpose |
| --- | --- | --- |
| `-help` | Member | Browse commands available in the current context or request detailed command help. |
| `-advancedhelpset` | Bot maintainer | Configure delivery, presentation, categories, audiences, and role-backed help groups. |
| `-docsreport` | Bot maintainer | Export a sanitized inventory of registered commands for documentation maintenance. |

## Using help

Run `-help` to browse the interactive audience and category menu. Direct help remains
available for complete command paths:

```text
-help pokemon
-help pokemon party
```

The menu organizes commands that Red permits in the current context; it does not grant
access. Live permissions, disabled state, parent checks, and server rules remain
authoritative.

## Learn more

- [Using SickGamingBot help](../using-help.md)
- [Complete Advanced Help command reference](../reference/advancedhelp.md)
- [Permissions and access levels](../permissions.md)
