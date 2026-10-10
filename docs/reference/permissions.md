# Permissions commands

Loaded package: `permissions`

Use `-help <command>` for complete syntax and argument details. Access below is
derived from declared command checks; server-specific permission rules can change it.

| Command | Aliases | Access | Description |
| --- | --- | --- | --- |
| `-permissions` | — | Member | Command permission management tools. |
| `-permissions acl` | `yaml` | Server owner or required Discord permission | Manage permissions with YAML files. |
| `-permissions acl getglobal` | — | Bot maintainer | Get a YAML file detailing all global rules. |
| `-permissions acl getserver` | `getguild` | Server owner or required Discord permission | Get a YAML file detailing all rules in this server. |
| `-permissions acl setglobal` | — | Bot maintainer | Set global rules with a YAML file. |
| `-permissions acl setserver` | `setguild` | Server owner or required Discord permission | Set rules for this server with a YAML file. |
| `-permissions acl updateglobal` | — | Bot maintainer | Update global rules with a YAML file. |
| `-permissions acl updateserver` | `updateguild` | Server owner or required Discord permission | Update rules for this server with a YAML file. |
| `-permissions acl yamlexample` | — | Server owner or required Discord permission | Sends an example of the yaml layout for permissions |
| `-permissions addglobalrule` | — | Bot maintainer | Add a global rule to a command. |
| `-permissions addserverrule` | `addguildrule` | Server owner or required Discord permission | Add a rule to a command in this server. |
| `-permissions canrun` | — | Member | Check if a user can run a command. |
| `-permissions clearglobalrules` | — | Bot maintainer | Reset all global rules. |
| `-permissions clearserverrules` | `clearguildrules` | Server owner or required Discord permission | Reset all rules in this server. |
| `-permissions explain` | — | Member | Explain how permissions works. |
| `-permissions removeglobalrule` | — | Bot maintainer | Remove a global rule from a command. |
| `-permissions removeserverrule` | `removeguildrule` | Server owner or required Discord permission | Remove a server rule from a command. |
| `-permissions setdefaultglobalrule` | — | Bot maintainer | Set the default global rule for a command. |
| `-permissions setdefaultserverrule` | `setdefaultguildrule` | Server owner or required Discord permission | Set the default rule for a command in this server. |

Live `-help` output remains authoritative for enabled state, hidden commands,
arguments, cooldowns, and server-specific access.
