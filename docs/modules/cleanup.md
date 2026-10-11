# Cleanup

> Targeted deletion of command messages, user messages, bot messages, duplicates, and other channel content.

## At a glance

- **Category:** Moderation and safety
- **Intended audience:** Moderators or members with the required Manage Messages permission.
- **Loaded package:** `cleanup`
- **Documented commands:** 12 commands and subcommands

## Main command families

| Command | Default access | Purpose |
| --- | --- | --- |
| `-cleanup` | Member | Base command for deleting messages. |
| `-cleanupset` | Administrator or required permission | Manage the settings for the cleanup command. |

## Using this module

Run help for a command family, then add subcommands to request more specific details:

```text
-help cleanup
-help cleanup <subcommand>
```

The bot only shows commands available to your account. Server-specific permission
rules, disabled commands, required integrations, and channel restrictions can change
what you can use.

## Learn more

- [Complete Cleanup command reference](../reference/cleanup.md)
- [Using SickGamingBot help](../using-help.md)
- [Permissions and access levels](../permissions.md)
