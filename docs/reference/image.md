# Image commands

Loaded package: `Image`

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
| `-gif` | — | Member | Retrieve the first search result from Giphy. |
| `-gifr` | — | Member | Retrieve a random GIF from a Giphy search. |
| `-giphycreds` | — | Bot maintainer | Explains how to set GIPHY API tokens. |
| `-imgur` | — | Member | Retrieve pictures from Imgur. |
| `-imgur search` | — | Member | Search Imgur for the specified term. |
| `-imgur subreddit` | — | Member | Get images from a subreddit. |
| `-imgurcreds` | — | Bot maintainer | Explain how to set imgur API tokens. |

Live `-help` output remains authoritative for syntax, enabled state, hidden commands,
arguments, cooldowns, and server-specific access.
