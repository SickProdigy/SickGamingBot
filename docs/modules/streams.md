# Streams

> Live-status checks and automatic alerts for supported streaming platforms.

## At a glance

- **Category:** Music, media, and feeds
- **Intended audience:** Members can check streams; administrators configure alerts.
- **Loaded package:** `streams`
- **Documented commands:** 26 commands and subcommands

## Main command families

| Command | Default access | Purpose |
| --- | --- | --- |
| `-picarto` | Member | Check if a Picarto channel is live. |
| `-streamalert` | Moderator or required permission | Manage automated stream alerts. |
| `-streamset` | Moderator or required permission | Manage stream alert settings. |
| `-twitchstream` | Member | Check if a Twitch channel is live. |
| `-youtubestream` | Member | Check if a YouTube channel is live. |

## Using this module

Run help for a command family, then add subcommands to request more specific details:

```text
-help picarto
-help picarto <subcommand>
```

The bot only shows commands available to your account. Server-specific permission
rules, disabled commands, required integrations, and channel restrictions can change
what you can use.

## Learn more

- [Complete Streams command reference](../reference/streams.md)
- [Using SickGamingBot help](../using-help.md)
- [Permissions and access levels](../permissions.md)
- [Detailed Streams guide](../../Streams.md)
