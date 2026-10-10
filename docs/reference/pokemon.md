# Pokémon commands

Loaded package: `pokemon`

Use `-help <command>` for complete syntax and argument details. Access below is
derived from declared command checks; server-specific permission rules can change it.

| Command | Aliases | Access | Description |
| --- | --- | --- | --- |
| `-pokemon` | `pkmn`, `poke` | Member | Play the global Pokémon catching and battle game. |
| `-pokemon achievements` | `goals` | Member | View accomplishment progress and upcoming supply rewards. |
| `-pokemon bag` | — | Member | View your available medicine and items. |
| `-pokemon buy` | — | Member | Buy Poké Mart supplies with Red bank credits. |
| `-pokemon center` | — | Member | Heal your party at this server’s Pokémon Center. |
| `-pokemon collection` | `box` | Member | Browse and manage Pokémon in your global collection. |
| `-pokemon collection release` | — | Member | Permanently release one boxed Pokémon after confirmation. |
| `-pokemon gym` | — | Member | View your ordered Kanto Gym progress. |
| `-pokemon gym challenge` | — | Member | Challenge the next Kanto Gym Leader's team. |
| `-pokemon mart` | — | Member | View supplies sold for Red bank credits. |
| `-pokemon menustyle` | — | Member | Choose the Retro or Modern Pokémon main-menu style. |
| `-pokemon moves` | — | Member | Resume an unfinished move-learning choice. |
| `-pokemon party` | — | Member | View the Pokémon in your active party. |
| `-pokemon party add` | — | Member | Add a caught Pokémon to your active party. |
| `-pokemon party remove` | — | Member | Remove a Pokémon from your active party. |
| `-pokemon pokedex` | `dex` | Member | Browse the Pokémon you have seen and caught. |
| `-pokemon pokedexstyle` | `dexstyle` | Member | Choose your Pokédex display style, or follow the bot default. |
| `-pokemon profile` | — | Member | View your or another member’s trainer card and badge case. |
| `-pokemon profilestyle` | `cardstyle` | Member | Choose the Retro or Gold style for your trainer card. |
| `-pokemon research` | `daily` | Member | View today’s Professor research tasks and supply rewards. |
| `-pokemon starter` | — | Member | Choose or view your first partner Pokémon. |
| `-pokemon trade` | — | Member | Offer an exact Pokémon-for-Pokémon trade. |
| `-pokemon trade cancel` | — | Member | Cancel one of your pending trade offers. |
| `-pokemon trade collection` | — | Member | View another trainer’s numbered Pokémon for a trade. |
| `-pokemon trade give` | `gift` | Member | Offer one to three Pokémon as a confirmed gift. |
| `-pokemon use` | — | Member | Use an item on one of your Pokémon. |
| `-pokemon use potion` | — | Member | Use a Potion to restore a Pokémon’s HP. |
| `-pokemon use revive` | — | Member | Use a Revive on a fainted Pokémon. |
| `-pokemon use stone` | — | Member | Use a Kanto evolution stone on an eligible Pokémon. |
| `-pokemonownerset` | `pokeownerset`, `pkmnownerset` | Bot maintainer | Configure bot-wide Pokémon policy and owner overrides. |
| `-pokemonownerset catalogsync` | — | Bot maintainer | Cache catalog data for a generation. |
| `-pokemonownerset centercooldown` | — | Bot maintainer | Set the bot-wide free Pokémon Center cooldown. |
| `-pokemonownerset concurrency` | `slots` | Bot maintainer | Override this server’s simultaneous encounter limit. |
| `-pokemonownerset encounterlimits` | — | Bot maintainer | Set server wild-encounter lifetime boundaries. |
| `-pokemonownerset encountertime` | — | Bot maintainer | Set the inherited bot-wide wild encounter lifetime. |
| `-pokemonownerset globalconcurrency` | — | Bot maintainer | Set the concurrency ceiling for ordinary server administrators. |
| `-pokemonownerset globalgenerations` | — | Bot maintainer | Set bot-wide available generations. |
| `-pokemonownerset globallimits` | — | Bot maintainer | Set global spawn-rate floors. |
| `-pokemonownerset globalstatus` | `settings`, `status` | Bot maintainer | Show all bot-wide Pokémon policies and owner limits. |
| `-pokemonownerset martprice` | — | Bot maintainer | Set a bot-wide Poké Mart item price. |
| `-pokemonownerset pokedexstyle` | — | Bot maintainer | Choose the default Pokédex style for users following the default. |
| `-pokemonownerset rarity` | — | Bot maintainer | Choose the global rarity profile. |
| `-pokemonownerset resetplayer` | — | Bot maintainer | Reset one complete Pokémon profile. |
| `-pokemonownerset specials` | — | Bot maintainer | Allow or gate special species. |
| `-pokemonownerset timer` | — | Bot maintainer | Override this server’s jittered timer from 1 minute to one week. |
| `-pokemonownerset timermin` | `minimumtimer` | Bot maintainer | Set the fastest timer ordinary server administrators may choose. |
| `-pokemonownerset vipclear` | — | Bot maintainer | Disable the trusted VIP role without removing prior rewards or Pokémon. |
| `-pokemonownerset vippack` | — | Bot maintainer | Set the monthly VIP supply pack. |
| `-pokemonownerset viprole` | — | Bot maintainer | Set or show the trusted guild and role for global VIP benefits. |
| `-pokemonset` | `pokeset`, `pkmnset` | Administrator or required Discord permission | Configure Pokémon without cluttering player commands. |
| `-pokemonset battleexpiry` | — | Administrator or required Discord permission | Set the server battle time limit. |
| `-pokemonset center` | — | Administrator or required Discord permission | Designate the server Pokémon Center. |
| `-pokemonset channel` | — | Administrator or required Discord permission | Enable wild encounters in a channel. |
| `-pokemonset clear` | — | Administrator or required Discord permission | End the encounter in this channel, or the server’s only encounter. |
| `-pokemonset concurrency` | `slots` | Administrator or required Discord permission | Set this server’s simultaneous encounters within the bot limit. |
| `-pokemonset cooldown` | — | Administrator or required Discord permission | Set a slower custom spawn cooldown. |
| `-pokemonset disable` | — | Administrator or required Discord permission | Disable wild encounters in this server. |
| `-pokemonset encountertime` | — | Administrator or required Discord permission | Set or inherit this server's wild encounter lifetime. |
| `-pokemonset expiredcards` | `missedcards` | Administrator or required Discord permission | Delete expired wild cards or keep their dimmed result. |
| `-pokemonset generations` | — | Administrator or required Discord permission | Choose from bot-enabled generations. |
| `-pokemonset mode` | — | Administrator or required Discord permission | Choose timed spawning or the optional activity system. |
| `-pokemonset notificationrole` | `alertrole` | Administrator or required Discord permission | Set or clear the opt-in encounter alert role. |
| `-pokemonset notifications` | `notify` | Administrator or required Discord permission | Choose silent, normal, or opt-in-role encounter alerts. |
| `-pokemonset pace` | — | Administrator or required Discord permission | Choose a preset encounter pace. |
| `-pokemonset quiethours` | — | Administrator or required Discord permission | Set local quiet hours or disable them with `off`. |
| `-pokemonset removecenter` | — | Administrator or required Discord permission | Remove the server Pokémon Center. |
| `-pokemonset removechannel` | — | Administrator or required Discord permission | Stop wild encounters in a channel. |
| `-pokemonset spawn` | — | Administrator or required Discord permission | Trigger a test encounter; bot owners may use `shiny`. |
| `-pokemonset status` | `settings` | Administrator or required Discord permission | Show channels, schedule, and effective server settings. |
| `-pokemonset threshold` | — | Administrator or required Discord permission | Set a slower custom activity threshold. |
| `-pokemonset timer` | — | Administrator or required Discord permission | Set this server’s jittered timer within the bot-owner floor. |

Live `-help` output remains authoritative for enabled state, hidden commands,
arguments, cooldowns, and server-specific access.
