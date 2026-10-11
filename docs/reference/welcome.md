# Welcome commands

Loaded package: `Welcome`

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
| `-welcomeset` | — | Administrator or required Discord permission | Sets welcome module settings |
| `-welcomeset bot` | — | Administrator or required Discord permission | Special greeting for bots. |
| `-welcomeset bot goodbyemsg` | `goodbyemessage` | Administrator or required Discord permission | Set the goodbye msg for bots. |
| `-welcomeset bot msg` | — | Administrator or required Discord permission | Set the greeting msg for bots. |
| `-welcomeset bot role` | — | Administrator or required Discord permission | Set the role to put bots in when they join. |
| `-welcomeset bot test` | — | Administrator or required Discord permission | Test the bot joining message |
| `-welcomeset embed` | — | Administrator or required Discord permission | Set various embed options. |
| `-welcomeset embed author` | — | Administrator or required Discord permission | Toggle the author field being filled in the embed. |
| `-welcomeset embed colour` | `color` | Administrator or required Discord permission | Set the embed colour. |
| `-welcomeset embed footer` | — | Administrator or required Discord permission | Set the embed footer. |
| `-welcomeset embed goodbyecolour` | `gcolor`, `gcolour`, `goodbyecolor` | Administrator or required Discord permission | Set the embed colour. |
| `-welcomeset embed icon` | — | Administrator or required Discord permission | Set the embed icon image. |
| `-welcomeset embed image` | — | Administrator or required Discord permission | Set embed image options. |
| `-welcomeset embed image goodbye` | — | Administrator or required Discord permission | Set the embed image link for goodbyes. |
| `-welcomeset embed image greeting` | — | Administrator or required Discord permission | Set the embed image link for greetings. |
| `-welcomeset embed mention` | — | Administrator or required Discord permission | Toggle mentioning the user when they join. |
| `-welcomeset embed thumbnail` | — | Administrator or required Discord permission | Set the embed thumbnail image. |
| `-welcomeset embed timestamp` | — | Administrator or required Discord permission | Toggle the timestamp in embeds. |
| `-welcomeset embed title` | — | Administrator or required Discord permission | Set the embed title. |
| `-welcomeset embed toggle` | — | Administrator or required Discord permission | Toggle embed messages. |
| `-welcomeset goodbye` | `leave` | Administrator or required Discord permission | Manage goodbye messages. |
| `-welcomeset goodbye add` | — | Administrator or required Discord permission | Adds a goodbye message format for the guild to be chosen at random |
| `-welcomeset goodbye allowedmentions` | — | Administrator or required Discord permission | Determine the bots allowed mentions for greetings |
| `-welcomeset goodbye channel` | — | Administrator or required Discord permission | Sets the channel to send the goodbye message. |
| `-welcomeset goodbye deleteafter` | — | Administrator or required Discord permission | Set the time after which a greeting message is deleted in seconds. |
| `-welcomeset goodbye deleteprevious` | — | Administrator or required Discord permission | Turns on/off deleting the previous greeting message when a user joins. |
| `-welcomeset goodbye list` | `del`, `delete`, `edit` | Administrator or required Discord permission | Lists the goodbye messages of this guild and allows editing the settings. |
| `-welcomeset goodbye test` | — | Administrator or required Discord permission | Test the goodbye message deleted after 60 seconds |
| `-welcomeset goodbye toggle` | — | Administrator or required Discord permission | Turns on/off sending goodbye messages to users who leave to the guild. |
| `-welcomeset greeting` | `welcome` | Administrator or required Discord permission | Manage welcome messages |
| `-welcomeset greeting add` | — | Administrator or required Discord permission | Adds a greeting message format for the guild to be chosen at random |
| `-welcomeset greeting allowedmentions` | — | Administrator or required Discord permission | Determine the bots allowed mentions for greetings |
| `-welcomeset greeting channel` | — | Administrator or required Discord permission | Sets the channel to send the greeting message. |
| `-welcomeset greeting count` | — | Administrator or required Discord permission | Turns on/off showing how many users join each day. |
| `-welcomeset greeting deleteafter` | — | Administrator or required Discord permission | Set the time after which a greeting message is deleted in seconds. |
| `-welcomeset greeting deleteprevious` | — | Administrator or required Discord permission | Turns on/off deleting the previous greeting message when a user joins. |
| `-welcomeset greeting filter` | — | Administrator or required Discord permission | Set what to do when a username matches the bots filter. |
| `-welcomeset greeting grouped` | — | Administrator or required Discord permission | Set whether to group greeting messages |
| `-welcomeset greeting list` | `del`, `delete`, `edit` | Administrator or required Discord permission | Lists the greeting messages of this guild and allows editing the settings. |
| `-welcomeset greeting minimumage` | `age` | Administrator or required Discord permission | Set the minimum number of days a user account must be to show up in the greeting message. |
| `-welcomeset greeting pending` | — | Administrator or required Discord permission | Set whether to wait for the user to pass verification to send the welcome |
| `-welcomeset greeting test` | — | Administrator or required Discord permission | Test the greeting message deleted after 60 seconds. |
| `-welcomeset greeting toggle` | — | Administrator or required Discord permission | Turns on/off welcoming new users to the guild. |
| `-welcomeset migrationstatus` | — | Bot maintainer | Owner: show the external Welcome import status. |
| `-welcomeset settings` | — | Administrator or required Discord permission | Show the servers welcome settings |
| `-welcomeset whisper` | — | Administrator or required Discord permission | Sets whether or not a DM is sent to the new user |

Live `-help` output remains authoritative for syntax, enabled state, hidden commands,
arguments, cooldowns, and server-specific access.
