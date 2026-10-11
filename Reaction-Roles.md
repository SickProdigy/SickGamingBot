# Self-service and game roles

SickGamingBot provides multiple role systems. Use the one that matches the community:

- Administration self-roles provide a straightforward approved role list through
  `-selfroleset` and `-selfrole`.
- Role Tools provides the loaded deployment's self-service role interface through
  `-roletools` and `-selfroles`.
- Game Roles provides named profiles, approved roles, and delegated manager roles
  through `-gameroleset` and `-gameroles`.

Always place the bot above roles it must manage, but below protected administrator and
owner roles. Test assignment and removal with a non-owner account.

Start with:

```text
-help selfroleset
-help roletools
-help gameroleset
```

Do not rely on old reaction-role examples: available subcommands depend on the loaded
Role Tools version. Live help is authoritative. See [Administration](docs/modules/admin.md),
[Role Tools](docs/modules/roletools.md), [Game Roles](docs/modules/gameroles.md), and
the [server-owner cog setup guide](docs/server-owners/cog-setup.md).
