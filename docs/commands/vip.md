# VIP commands and benefits

SickGaming VIP currently adds benefits to ordinary Pokémon commands. It is not a fifth
bot permission tier, and there is no standalone `-vip` command.

## VIP-aware member commands

| Command | Default access | VIP behavior |
| --- | --- | --- |
| `-pokemon` and its subcommands | Member | First Pokémon activity in each UTC month delivers the configured VIP supply pack once. |
| `-pokemon bag` | Member | Displays delivered VIP supplies with the trainer's other items. |
| `-pokemon collection` | Member | Supports the expanded 480-slot VIP PC capacity. |
| `-pokemon profile [@member]` | Member | Displays the gold VIP trainer marker and effective storage capacity. |

## Maintainer-only VIP commands

| Command | Default access | Purpose |
| --- | --- | --- |
| `-pokemonownerset viprole [guild-id] [role-id]` | Bot maintainer | Show or set the trusted Discord server and role. |
| `-pokemonownerset vippack <balls> <great-balls> <ultra-balls> <potions> <revives>` | Bot maintainer | Configure the monthly Pokémon supply pack. |
| `-pokemonownerset vipclear` | Bot maintainer | Disable VIP role recognition without removing prior rewards or Pokémon. |

These maintainer commands are listed for transparency. VIP membership and Discord
server ownership do not grant permission to run them.

Read the [SickGaming VIP guide](../vip/index.md) for current benefits, eligibility
boundaries, and development status. Use live `-help` for current syntax and access.
