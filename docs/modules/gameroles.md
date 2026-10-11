# Game Roles

> Named game-role profiles with self-service assignment and delegated managers.

## At a glance

- **Category:** Community and server management
- **Intended audience:** Members choose approved roles; administrators or delegated managers configure profiles.
- **Loaded package:** `gameroles`
- **Documented commands:** 11 commands and subcommands

## Main command families

| Command | Default access | Purpose |
| --- | --- | --- |
| `-gameroles` | Member | Assign approved game roles through a dashboard or fallback commands. |
| `-gameroleset` | Administrator or required permission | Configure delegated game-role profiles. |

## Using this module

Run help for a command family, then add subcommands to request more specific details:

```text
-help gameroles
-help gameroles <subcommand>
```

The bot only shows commands available to your account. Server-specific permission
rules, disabled commands, required integrations, and channel restrictions can change
what you can use.

## Learn more

- [Complete Game Roles command reference](../reference/gameroles.md)
- [Using SickGamingBot help](../using-help.md)
- [Permissions and access levels](../permissions.md)
