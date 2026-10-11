# SickGaming VIP guide

SickGaming VIP is an additional benefit role maintained by SickGaming. It is not a
Discord permission level, server staff role, or substitute for the checks attached to
bot commands.

## Current availability

VIP support is still developing. The production bot currently provides VIP benefits
through the [Pokémon module](../modules/pokemon.md). There is no separate `-vip`
command, and VIP membership does not unlock moderation, server-owner, or bot-maintainer
commands.

Eligibility is determined from one trusted SickGaming Discord server and role. A role
named “VIP” in another Discord server does not automatically provide these benefits.

## Current Pokémon benefits

- A gold VIP marker appears on the eligible trainer's profile embed and generated card.
- PC storage expands from 240 to 480 Pokémon, in addition to the six-Pokémon party.
- The first Pokémon command used during each UTC month grants the configured monthly
  supply pack once. The current default is 20 Poké Balls, 5 Great Balls, 2 Ultra Balls,
  10 Potions, and 3 Revives.
- Losing eligibility never deletes Pokémon or previously delivered supplies. A trainer
  above the normal storage limit cannot store another catch until their owned total is
  below that limit.

The pack contents are configurable and may change. The bot's delivery message and live
`-help` output are authoritative.

## Commands VIP members use

These are ordinary Pokémon commands with additional VIP-aware behavior; they are not
exclusive commands.

| Command | What VIP changes |
| --- | --- |
| `-pokemon` and its subcommands | The first Pokémon activity in a UTC month delivers the monthly pack once. |
| `-pokemon bag` | Shows supplies, including any monthly VIP items already delivered. |
| `-pokemon collection` | Uses the expanded 480-slot VIP PC capacity. |
| `-pokemon profile [@member]` | Shows the eligible trainer's gold VIP marker and expanded capacity. |

For every Pokémon action and subcommand, use the
[complete Pokémon reference](../reference/pokemon.md) or run `-help pokemon`.

## VIP administration

The explicit VIP configuration commands are reserved for SickGamingBot maintainers:

| Command | Purpose |
| --- | --- |
| `-pokemonownerset viprole [guild-id] [role-id]` | Show or set the trusted Discord server and role used for global Pokémon VIP benefits. |
| `-pokemonownerset vippack <balls> <great-balls> <ultra-balls> <potions> <revives>` | Set the monthly supply pack. |
| `-pokemonownerset vipclear` | Disable the trusted VIP role without deleting existing Pokémon or delivered rewards. |

Discord server owners and ordinary VIP members cannot run these maintainer commands.

## Server-specific VIP roles

Some servers may independently use [Role Tools](../modules/roletools.md) to create a
private group or role menu named VIP. Those server-specific roles control only what
that server configured. They do not automatically grant SickGaming's global Pokémon
VIP benefits.

## As VIP expands

This page will list new benefits only after they are implemented and loaded on the
official bot. Planned ideas are not documented as available commands.

See [Permissions](../permissions.md) for the difference between membership benefits,
Discord roles, staff access, server ownership, and bot maintenance.
