# Using SickGamingBot help

SickGamingBot's `-help` command can explain the entire bot, one command group, or one
specific subcommand. Add each part of the command path after `-help`.

## Browse commands available to you

```text
-help
```

This opens an interactive audience-first menu. Choose an audience area, then a category,
then a command. The menu is built from commands currently visible to your account;
disabled commands and commands you cannot use may be hidden.

The audience labels organize the menu. They do not grant permissions or replace the
bot's live command checks.

## Learn about a command

```text
-help pokemon
-help cleanup
-help warningset
```

Command help normally includes a description, usage information, aliases, and available
subcommands.

## Learn about a subcommand

Include the full command path, with spaces between the parent command and each
subcommand:

```text
-help pokemon party
-help cleanup messages
-help warningset mywarnings
```

For a nested subcommand, continue adding each level:

```text
-help warningset mywarnings sendtodms
```

This is often more useful than help for the parent command because it focuses on the
specific action, arguments, and restrictions.

## Reading command syntax

- `<argument>` means the argument is required. Do not type the angle brackets.
- `[argument]` means the argument is optional. Do not type the square brackets.
- Use quotes around a name or message containing spaces when the command expects one value.
- Commands and subcommands are separated by spaces, not additional hyphens.

For example, if help shows:

```text
-command <member> [reason]
```

replace `<member>` with a member mention or accepted identifier. Add a reason if needed.

Live help is authoritative because it reflects the commands, permissions, aliases, and
configuration currently available to your account. You can also browse the
[complete command reference](reference/index.md).
