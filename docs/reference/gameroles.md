# Game Roles commands

Loaded package: `gameroles`

Use `-help <command>` for complete syntax and argument details. Access below is
derived from declared command checks; server-specific permission rules can change it.

| Command | Aliases | Access | Description |
| --- | --- | --- | --- |
| `-gameroles` | `gamerole`, `clanroles`, `clanrole` | Member | Assign approved game roles through a dashboard or fallback commands. |
| `-gameroles add` | `assign` | Member | Add an approved game role; the optional game keeps legacy syntax working. |
| `-gameroles remove` | `rem`, `unassign` | Member | Remove an approved game role; the optional game keeps legacy syntax working. |
| `-gameroleset` | — | Administrator or required Discord permission | Configure delegated game-role profiles. |
| `-gameroleset allow` | — | Administrator or required Discord permission | Configure roles that delegated managers may add or remove. |
| `-gameroleset allow add` | — | Administrator or required Discord permission | Approve a role for delegated management in one game profile. |
| `-gameroleset allow remove` | `delete` | Administrator or required Discord permission | Remove a role from one game's approved list. |
| `-gameroleset manager` | — | Administrator or required Discord permission | Configure roles allowed to manage one game's approved roles. |
| `-gameroleset manager add` | — | Administrator or required Discord permission | Allow a role to manage one game profile. |
| `-gameroleset manager remove` | `delete` | Administrator or required Discord permission | Remove a delegated manager role from one game profile. |
| `-gameroleset show` | `status` | Administrator or required Discord permission | Show the configured manager and member roles for a game. |

Live `-help` output remains authoritative for enabled state, hidden commands,
arguments, cooldowns, and server-specific access.
