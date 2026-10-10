# Meme commands

Loaded package: `meme`

Use `-help <command>` for complete syntax and argument details. Access below is
derived from declared command checks; server-specific permission rules can change it.

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
| `-memeset autopost off` | `remove`, `disable` | Administrator or required Discord permission | Remove a Meme API feed by destination and subreddit source. |
| `-memeset autopost status` | `list` | Administrator or required Discord permission | Show Meme API feed IDs, sources, destinations, intervals, and state. |
| `-memeset feed` | — | Administrator or required Discord permission | Manage automatic meme feeds. |
| `-memeset feed add` | — | Administrator or required Discord permission | Add an advanced scheduled feed. |
| `-memeset feed list` | — | Administrator or required Discord permission | List configured feeds. |
| `-memeset feed remove` | `delete` | Administrator or required Discord permission | Remove a feed by ID. |
| `-memeset gifpost` | — | Administrator or required Discord permission | Automatically post animated Imgur results to a channel. |
| `-memeversion` | — | Member | Show the installed Meme cog version. |

Live `-help` output remains authoritative for enabled state, hidden commands,
arguments, cooldowns, and server-specific access.
