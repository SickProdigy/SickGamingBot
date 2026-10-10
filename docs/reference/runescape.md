# RuneScape commands

Loaded package: `runescape`

## Reading this reference

Each command is shown as its complete path. To see detailed help, put that path after
`-help` without repeating the leading hyphen:

```text
-help <command>
-help <command> <subcommand>
-help <command> <subcommand> <nested-subcommand>
```

The access column is derived from declared command checks. Server-specific permission
rules can change it. See [Using SickGamingBot help](../using-help.md) for examples and
an explanation of required and optional arguments.

| Command | Aliases | Access | Description |
| --- | --- | --- | --- |
| `-runescape` | `rs` | Member | Look up RuneScape players and wiki articles. |
| `-runescape item` | — | Member | Find an item on the Old School RuneScape Wiki. |
| `-runescape quest` | — | Member | Find a quest on the Old School RuneScape Wiki. |
| `-runescape rs3wiki` | — | Member | Search the RuneScape (RS3) Wiki. |
| `-runescape user` | `player`, `stats` | Member | Show stats. Prefix a name with `rs3` to use RuneScape 3. |
| `-runescape wiki` | `search` | Member | Search the Old School RuneScape Wiki. |

Live `-help` output remains authoritative for enabled state, hidden commands,
arguments, cooldowns, and server-specific access.
