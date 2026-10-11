# Economy

> Currency balances, payday, leaderboards, transfers, and slot-machine play.

## At a glance

- **Category:** Economy, information, and utilities
- **Intended audience:** Members use the economy; server owners and maintainers configure it.
- **Loaded package:** `economy`
- **Documented commands:** 16 commands and subcommands

## Main command families

| Command | Default access | Purpose |
| --- | --- | --- |
| `-bank` | Member | Base command to manage the bank. |
| `-economyset` | Administrator or required permission | Base command to manage Economy settings. |
| `-leaderboard` | Member | Print the leaderboard. |
| `-payday` | Member | Get some free currency. |
| `-payouts` | Member | Show the payouts for the slot machine. |
| `-slot` | Member | Use the slot machine. |

## Using this module

Run help for a command family, then add subcommands to request more specific details:

```text
-help bank
-help bank <subcommand>
```

The bot only shows commands available to your account. Server-specific permission
rules, disabled commands, required integrations, and channel restrictions can change
what you can use.

## Learn more

- [Complete Economy command reference](../reference/economy.md)
- [Using SickGamingBot help](../using-help.md)
- [Permissions and access levels](../permissions.md)
