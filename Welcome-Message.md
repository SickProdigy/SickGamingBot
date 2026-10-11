# Welcome and goodbye messages

The Welcome module can publish greetings and departures, send private greetings, style
embeds, and handle bot accounts separately.

Administrators begin with:

```text
-help welcomeset
-help welcomeset greeting
-help welcomeset goodbye
-help welcomeset embed
```

Choose the destination, message text, allowed mentions, embed appearance, deletion
behavior, account-age or verification handling, and whether each message type is
enabled. Use `-welcomeset greeting test`, `-welcomeset goodbye test`, and
`-welcomeset settings` before announcing the feature.

See the current [Welcome module](docs/modules/welcome.md), [complete command
reference](docs/reference/welcome.md), and [server-owner cog setup
guide](docs/server-owners/cog-setup.md).
