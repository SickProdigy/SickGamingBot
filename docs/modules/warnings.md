# Warnings

> Warnings, reasons, automated actions, member history, and warning policy.

## At a glance

- **Category:** Moderation and safety
- **Intended audience:** Members can review their own warnings; moderators warn; server owners configure policy.
- **Loaded package:** `warnings`
- **Documented commands:** 20 commands and subcommands

## Main command families

| Command | Default access | Purpose |
| --- | --- | --- |
| `-actionlist` | Administrator or required permission | List all configured automated actions for Warnings. |
| `-mywarnings` | Member | List warnings for yourself. |
| `-reasonlist` | Administrator or required permission | List all configured reasons for Warnings. |
| `-unwarn` | Administrator or required permission | Remove a warning from a user. |
| `-warn` | Administrator or required permission | Warn the user for the specified reason. |
| `-warnaction` | Server owner or required permission | Manage automated actions for Warnings. |
| `-warnings` | Administrator | List the warnings for the specified user. |
| `-warningset` | Server owner or required permission | Manage settings for Warnings. |
| `-warnreason` | Server owner or required permission | Manage warning reasons. |

## Using this module

Run help for a command family, then add subcommands to request more specific details:

```text
-help actionlist
-help actionlist <subcommand>
```

The bot only shows commands available to your account. Server-specific permission
rules, disabled commands, required integrations, and channel restrictions can change
what you can use.

## Learn more

- [Complete Warnings command reference](../reference/warnings.md)
- [Using SickGamingBot help](../using-help.md)
- [Permissions and access levels](../permissions.md)
