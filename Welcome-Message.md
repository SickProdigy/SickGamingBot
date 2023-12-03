# Here's how to set a Welcome message with SickGamingBot

```Syntax: -welcomeset```
Sets welcome module settings

Subcommands:
* bot - Special greeting for bots.
* embed - Set various embed options.
* goodbye - Manage goodbye messages.
* greeting - Manage welcome messages
* settings - Show the servers welcome settings
* whisper - Sets whether or not a DM is sent to the new user

---

```Syntax: -welcomeset embed```
Set various embed options.

Subcommands:
* author - Toggle the author field being filled in the embed.
* colour - Set the embed colour.
* footer - Set the embed footer.
* icon - Set the embed icon image.
* image - Set embed image options.
* mention - Toggle mentioning the user when they join.
* thumbnail - Set the embed thumbnail image.
* timestamp - Toggle the timestamp in embeds.
* title Set - the embed title.
* toggle - Toggle embed messages.

---

```Syntax: -welcomeset greeting```
Alias: -welcomeset welcome
Manage welcome messages

Subcommands:
* add Adds a greeting message format for the guild to be chosen a...
* allowedmentions Determine the bots allowed mentions for greetings
* channel Sets the channel to send the greeting message.
* count Turns on/off showing how many users join each day.
* deleteafter Set the time after which a greeting message is dele...
* deleteprevious Turns on/off deleting the previous greeting mess...
* filter Set what to do when a username matches the bots filter.
* Subcommands: (continued)
* grouped Set whether to group greeting messages
* list Lists the greeting messages of this guild and allows editi...
* minimumage Set the minimum number of days a user account must b...
* test Test the greeting message deleted after 60 seconds.
* toggle Turns on/off welcoming new users to the guild.


Example Commands:
```
-welcomeset embed title Look who just spawned..
-welcomeset embed icon https://cdn.discordapp.com/avatars/691452746632658954/1521ca5ce3b930f92aef0d7ff109cdb1.png?size=1024
-welcomeset greeting test
```