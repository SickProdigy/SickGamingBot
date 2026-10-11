# RuneScape commands

Loaded package: `RuneScape`

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
| `-runescape` | `rs` | Member | Look up RuneScape players and wiki articles. |
| `-runescape item` | — | Member | Find an item on the Old School RuneScape Wiki. |
| `-runescape quest` | — | Member | Find a quest on the Old School RuneScape Wiki. |
| `-runescape rs3wiki` | — | Member | Search the RuneScape (RS3) Wiki. |
| `-runescape user` | `player`, `stats` | Member | Show stats. Prefix a name with `rs3` to use RuneScape 3. |
| `-runescape wiki` | `search` | Member | Search the Old School RuneScape Wiki. |

Live `-help` output remains authoritative for syntax, enabled state, hidden commands,
arguments, cooldowns, and server-specific access.
