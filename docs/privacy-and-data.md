# Privacy and data

SickGamingBot processes only the information needed by enabled commands and integrations.
The exact data depends on which modules a server owner enables and which services a
member chooses to connect.

## What may be processed

- Discord identifiers for users, servers, channels, messages, and roles.
- Command input, moderation cases, warnings, reports, settings, and feature state.
- Game or media account identifiers supplied for an enabled integration.
- Operational records needed for cooldowns, scheduled posts, and error diagnosis.

Public commands can produce public output. Reports, moderation records, and account
setup should use the private destinations documented by the feature.

## Secrets and account connections

Never send passwords, recovery codes, payment details, private keys, or unrestricted
administrator tokens to the bot. Enter a credential only through a documented private
prompt or approved SickGaming website flow.

Personal connections should be scoped, revocable, and removable by the member. Server
integrations should use separate service accounts with the minimum required permissions.
Removing the bot from Discord does not automatically revoke credentials at an external
service.

## Access, removal, and retention

Use `-mydata` to see the data-management actions currently available to you. Some
subcommands may be unavailable while their implementation is incomplete. Use a
feature's unlink, disconnect, or delete command when one exists.

Server owners should disconnect retired integrations, revoke their external credentials,
and review feature-specific retention before enabling logs or account provisioning.
Contact SickGamingBot maintainers for a request that live `-mydata` cannot complete.

## Reporting safely

When requesting support, include the command, approximate time, and sanitized error
text. Do not include credentials, private-channel contents, moderation evidence, or
personal information that is unnecessary to diagnose the problem.

See [Permissions](permissions.md), [Troubleshooting](troubleshooting.md), and the
[server-owner integration guide](server-owners/integrations.md).
