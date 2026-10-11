# Economy commands

Loaded package: `Economy`

## Reading this reference

Each command is shown as its complete path. To see detailed help, put that path after
`-help` without repeating the leading hyphen:

```text
-help <command>
-help <command> <subcommand>
-help <command> <subcommand> <nested-subcommand>
```

The access column comes from the command checks declared by the running bot. Live
permissions, disabled commands, parent checks, role hierarchy, and server rules can
further restrict availability. See [Using SickGamingBot help](../using-help.md).

| Command | Aliases | Access | Description |
| --- | --- | --- | --- |
| `-bank` | — | Member | Base command to manage the bank. |
| `-bank balance` | — | Member | Show the user's account balance. |
| `-bank set` | — | Administrator or required Discord permission | Set the balance of a user's bank account. |
| `-bank transfer` | — | Member | Transfer currency to other users. |
| `-economyset` | — | Administrator or required Discord permission | Base command to manage Economy settings. |
| `-economyset paydayamount` | — | Administrator or required Discord permission | Set the amount earned each payday. |
| `-economyset paydaytime` | — | Administrator or required Discord permission | Set the cooldown for the payday command. |
| `-economyset rolepaydayamount` | — | Administrator or required Discord permission | Set the amount earned each payday for a role. |
| `-economyset showsettings` | — | Administrator or required Discord permission | Shows the current economy settings |
| `-economyset slotmax` | — | Administrator or required Discord permission | Set the maximum slot machine bid. |
| `-economyset slotmin` | — | Administrator or required Discord permission | Set the minimum slot machine bid. |
| `-economyset slottime` | — | Administrator or required Discord permission | Set the cooldown for the slot machine. |
| `-leaderboard` | — | Member | Print the leaderboard. |
| `-payday` | — | Member | Get some free currency. |
| `-payouts` | — | Member | Show the payouts for the slot machine. |
| `-slot` | — | Member | Use the slot machine. |

Live `-help` output remains authoritative for syntax, enabled state, hidden commands,
arguments, cooldowns, and server-specific access.
