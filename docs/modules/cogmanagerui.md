# Cog Manager

> Maintainer controls for Red's installed and available cog paths.

## At a glance

- **Category:** Bot administration
- **Intended audience:** SickGamingBot maintainers only.
- **Availability:** Red core component (`CogManagerUI`)
- **Documented commands:** 6 commands and subcommands

## Main command families

| Command | Default access | Purpose |
| --- | --- | --- |
| `-cogs` | Bot maintainer | List loaded and available cogs. |
| `-paths` | Bot maintainer | List cog discovery paths. |
| `-addpath` | Bot maintainer | Add a cog discovery path. |
| `-removepath` | Bot maintainer | Remove a cog discovery path. |
| `-reorderpath` | Bot maintainer | Change cog path priority. |
| `-installpath` | Bot maintainer | View or change the cog installation path. |

These commands affect the hosted bot installation, not a Discord server's module
settings. Discord server ownership does not grant access.

## Learn more

- [Complete Cog Manager command reference](../reference/cogmanagerui.md)
- [Bot-maintainer commands](../commands/maintainers.md)
- [Permissions and access levels](../permissions.md)
