# Moderator and administrator commands

Access depends on Discord permissions, role hierarchy, Red checks, and server policy.
Review direct help before destructive or bulk actions.

This guide uses “staff” as shorthand for people granted moderator, administrator, or
delegated feature access in a Discord server. A SickGaming community staff title does
not automatically grant commands in another server. See [Permissions](../permissions.md)
for the distinction.

For every subcommand and its declared access level, use the [complete reference](../reference/index.md).

## Moderation

- Warnings: `-warn`, `-unwarn`, `-warnings`, `-reasonlist`, and `-actionlist`
- Mutes: `-mute`, `-unmute`, `-mutechannel`, and `-unmutechannel`
- Removal: `-kick`, `-ban`, `-softban`, `-tempban`, `-unban`, and `-massban`
- Cases: `-case`, `-casesfor`, `-listcases`, and `-reason`
- Utilities: `-userinfo`, `-names`, `-rename`, `-cleanup`, and `-report`

## Roles and community features

- `-addrole`, `-removerole`, `-selfrole`, and `-selfroleset`
- `-roletools` and `-gameroleset`
- `-giveaway`, `-welcomeset`, `-streamalert`, `-streamset`, and `-rss`

## Game and media configuration

- `-arkset`, `-dayzset`, `-gmodset`, and `-icarusset`
- `-cocset`
- `-rocketleagueset` (alias `-rlset`) and `-rlcsset`
- `-movieset`, `-navidromeset`, and `-memeset`
- `-audioset`, `-playlist`, and `-eq`

## Server policy

- `-filter` and `-filterset`
- `-warningset`, `-warnaction`, and `-warnreason`
- `-muteset`, `-modset`, and `-modlogset`
- `-command`, `-ignore`, `-unignore`, and `-alias`

Delegated feature access does not grant bot-host access. Loading cogs, changing global
credentials, restarting the process, and repository management remain maintainer tasks.
