# Meme commands

Loaded package: `Meme` + `Memeify`

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
| `-meme` | `memes` | Member | Post or search for online memes and GIFs. |
| `-meme community` | `reddit` | Member | Get a random Meme API result from a subreddit. |
| `-meme gif` | `imgurgif` | Member | Post an animated Imgur result, optionally searching by query. |
| `-meme imgur` | — | Member | Post a random public Imgur result, optionally searching by query. |
| `-meme search` | — | Member | Search public Imgur posts by title and tags. |
| `-meme sources` | — | Member | Show online providers and configuration status. |
| `-memeify` | `imgflip` | Member | Create a meme: `memeify <template> <top> \| <bottom>`. |
| `-memeify avatar` | — | Member | Create a meme using a member's displayed avatar. |
| `-memeify image` | `attachment`, `photo` | Member | Caption an attached image: `memeify image <top> \| <bottom>`. |
| `-memeify list` | `templates` | Member | List bundled meme templates. |
| `-memeset` | — | Administrator or required Discord permission | Configure automatic meme feeds. |
| `-memeset autopost` | — | Administrator or required Discord permission | Set or toggle a Meme API subreddit feed. |
| `-memeset autopost off` | `disable`, `remove` | Administrator or required Discord permission | Remove a Meme API feed by destination and subreddit source. |
| `-memeset autopost status` | `list` | Administrator or required Discord permission | Show Meme API feed IDs, sources, destinations, intervals, and state. |
| `-memeset feed` | — | Administrator or required Discord permission | Manage automatic meme feeds. |
| `-memeset feed add` | — | Administrator or required Discord permission | Add an advanced scheduled feed. |
| `-memeset feed list` | — | Administrator or required Discord permission | List configured feeds. |
| `-memeset feed remove` | `delete` | Administrator or required Discord permission | Remove a feed by ID. |
| `-memeset gifpost` | — | Administrator or required Discord permission | Automatically post animated Imgur results to a channel. |
| `-memeset notifications` | `notify` | Administrator or required Discord permission | Choose silent or normal delivery for automatic meme feeds. |
| `-memeversion` | — | Member | Show the installed Meme cog version. |

Live `-help` output remains authoritative for syntax, enabled state, hidden commands,
arguments, cooldowns, and server-specific access.
