# Dictionary commands

Loaded package: `dictionary`

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
| `-antonym` | `antonyms`, `ant` | Member | Show antonyms for an English word. |
| `-dictionary` | `dict`, `define` | Member | Look up an English word or phrase. |
| `-synonym` | `synonyms`, `syn` | Member | Show synonyms for an English word. |

Live `-help` output remains authoritative for enabled state, hidden commands,
arguments, cooldowns, and server-specific access.
