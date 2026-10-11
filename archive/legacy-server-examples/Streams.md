# Stream alerts

SickGamingBot can check Twitch, YouTube, and Picarto channels and publish automatic
live alerts.

Members can check stream status with `-twitchstream`, `-youtubestream`, and
`-picarto`. Authorized staff configure alerts with `-streamalert` and presentation
behavior with `-streamset`.

Start with:

```text
-help streamalert
-help streamalert twitch
-help streamset
```

Choose the destination channel, permitted mentions, message format, button behavior,
rerun/schedule policy, and whether offline alerts are removed. List and test alerts
before relying on them publicly. Twitch and YouTube provider credentials are managed by
SickGamingBot maintainers.

See the current [Streams module](docs/modules/streams.md), [complete command
reference](docs/reference/streams.md), and [server-owner cog setup
guide](docs/server-owners/cog-setup.md).
