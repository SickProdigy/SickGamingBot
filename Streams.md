# SickGamingBot Streams Command
## SickGamingBot Stream alerts and check status of stream.


### Automated Stream Alerts
Syntax: -streamalert
Note* You can run '-streamalert help' to get detailed information in discord chat.
</br>
*Manage automated stream alerts.*

**Sub-commands:**
* list - List all active stream alerts in this server.
* picarto - Toggle alerts in this channel for a Picarto stream.
* stop - Disable all stream alerts in this channel or server.
* twitch - Manage Twitch stream notifications.
* youtube - Toggle alerts in this channel for a YouTube stream.

### Stream Alert Settings
Syntax: -streamset
Note* You can run '-streamset help' to get detailed information in discord chat.
</br>
*Manage stream alert settings.*

**Sub-commands:**
* autodelete Toggle alert deletion for when streams go offline.
* ignorereruns Toggle excluding rerun streams from alerts.
* ignoreschedule Toggle excluding YouTube streams schedules from...
* mention Manage mention settings for stream alerts.
* message Manage custom messages for stream alerts.
* timer Set stream check refresh time.
* twitchtoken Explain how to set the twitch token.
* usebuttons Toggle whether to use buttons for stream alerts.

### Stream Status
Syntax:
-youtubestream <username>
  - Alias: -youtube
-picarto <username>
-twitchstream <username>
  - Alias: -twitch
</br>

### Example Commands (without channel id at the end, it will post in immediate channel you are in.)
```
-streamalert twitch <channel_name> [discord_channel=<this channel>]
-streamalert twitch kenzrosey
-streamalert twitch kenzrosey [discord_channel=447018654048190464] # not right, just noting for later
```
