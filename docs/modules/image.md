# Image

> GIF and image-search commands backed by configured providers.

## At a glance

- **Category:** Music, media, and feeds
- **Intended audience:** Members use searches; maintainers configure global provider credentials.
- **Loaded package:** `image`
- **Documented commands:** 7 commands and subcommands

## Main command families

| Command | Default access | Purpose |
| --- | --- | --- |
| `-gif` | Member | Retrieve the first search result from Giphy. |
| `-gifr` | Member | Retrieve a random GIF from a Giphy search. |
| `-giphycreds` | Bot maintainer | Explains how to set GIPHY API tokens. |
| `-imgur` | Member | Retrieve pictures from Imgur. |
| `-imgurcreds` | Bot maintainer | Explain how to set imgur API tokens. |

## Using this module

Run help for a command family, then add subcommands to request more specific details:

```text
-help gif
-help gif <subcommand>
```

The bot only shows commands available to your account. Server-specific permission
rules, disabled commands, required integrations, and channel restrictions can change
what you can use.

## Learn more

- [Complete Image command reference](../reference/image.md)
- [Using SickGamingBot help](../using-help.md)
- [Permissions and access levels](../permissions.md)
