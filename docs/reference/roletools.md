# Role Tools commands

Loaded package: `RoleTools`

## Reading this reference

Each command is shown as its complete path. To see detailed help, put that path after
`-help` without repeating the leading hyphen:

```text
-help <command>
-help <command> <subcommand>
-help <command> <subcommand> <nested-subcommand>
```

The access column comes from the command checks declared by the running bot. Live
permissions, disabled commands, parent checks, role hierarchy, and server rules can
further restrict availability. See [Using SickGamingBot help](../using-help.md).

| Command | Aliases | Access | Description |
| --- | --- | --- | --- |
| `-roletools` | — | Member | Member role help and server role-management commands. |
| `-roletools adminhelp` | `setuphelp` | Administrator or required Discord permission | Manager command guide. |
| `-roletools atomic` | — | Administrator or required Discord permission | Configure safe role changes. |
| `-roletools autorole` | `auto` | Administrator or required Discord permission | Configure join roles. |
| `-roletools buttons` | `button` | Administrator or required Discord permission | Manage button roles. |
| `-roletools buttons cleanup` | — | Administrator or required Discord permission | Check each button that has registered a message still exists and remove buttons with |
| `-roletools buttons create` | — | Administrator or required Discord permission | Create a role button |
| `-roletools buttons delete` | `del`, `remove` | Administrator or required Discord permission | Delete a saved button. |
| `-roletools buttons view` | — | Administrator or required Discord permission | View current buttons setup for role assign in this server. |
| `-roletools cost` | — | Administrator or required Discord permission | Set a role Bank cost. |
| `-roletools exclude` | `exclusive` | Member | Manage conflicting roles. |
| `-roletools exclude add` | — | Administrator or required Discord permission | Add role exclusion (This will remove if the designated role is acquired |
| `-roletools exclude mutual` | — | Administrator or required Discord permission | Allow setting roles mutually exclusive to eachother |
| `-roletools exclude remove` | — | Administrator or required Discord permission | Remove role exclusion |
| `-roletools forcerole` | — | Administrator or required Discord permission | Force a sticky role. |
| `-roletools forceroleremove` | — | Administrator or required Discord permission | Remove a forced sticky role. |
| `-roletools giverole` | — | Administrator or required Discord permission | Give a role in bulk. |
| `-roletools globalatomic` | — | Bot maintainer | Set the atomicity of role assignment. |
| `-roletools group` | `groups`, `privategroups` | Member | View or manage private access groups. |
| `-roletools group accessrole` | `gateway` | Administrator or required Discord permission | Set the group's member access role; omit the role to clear it. |
| `-roletools group archive` | — | Administrator or required Discord permission | Archive an unpublished private group. |
| `-roletools group conflicts` | — | Administrator or required Discord permission | No short description is declared. |
| `-roletools group conflicts add` | — | Administrator or required Discord permission | No short description is declared. |
| `-roletools group conflicts remove` | — | Administrator or required Discord permission | No short description is declared. |
| `-roletools group cost` | — | Administrator or required Discord permission | Set the one-time access cost; use 0 for free. |
| `-roletools group create` | — | Administrator or required Discord permission | Create a private group and its unpublished named menu. |
| `-roletools group delete` | — | Administrator or required Discord permission | Delete an unpublished private group; append `confirm`. |
| `-roletools group description` | `describe` | Administrator or required Discord permission | Set the manager/member description for a private group. |
| `-roletools group duration` | — | Administrator or required Discord permission | Set gateway access in minutes; use 0 for permanent. |
| `-roletools group join` | — | Member | Join a private group after its prerequisites and access cost are checked. |
| `-roletools group leave` | — | Member | Leave a private group and remove its gateway/selectable roles. |
| `-roletools group publish` | — | Administrator or required Discord permission | Publish a group through private, dropdown, reactions, or role_channel layout. |
| `-roletools group required` | — | Administrator or required Discord permission | No short description is declared. |
| `-roletools group required add` | — | Administrator or required Discord permission | No short description is declared. |
| `-roletools group required mode` | — | Administrator or required Discord permission | No short description is declared. |
| `-roletools group required remove` | — | Administrator or required Discord permission | No short description is declared. |
| `-roletools group restore` | — | Administrator or required Discord permission | Restore an archived private group. |
| `-roletools group roles` | — | Administrator or required Discord permission | Add or remove private-group selectable roles. |
| `-roletools group roles add` | — | Administrator or required Discord permission | No short description is declared. |
| `-roletools group roles remove` | — | Administrator or required Discord permission | No short description is declared. |
| `-roletools group view` | — | Member | Show a private group's access rules and roles. |
| `-roletools include` | `inclusive` | Member | Manage linked roles. |
| `-roletools include add` | — | Administrator or required Discord permission | Add role inclusion (This will add roles if the designated role is acquired |
| `-roletools include mutual` | — | Administrator or required Discord permission | Allow setting roles mutually inclusive to eachother |
| `-roletools include remove` | — | Administrator or required Discord permission | Remove role inclusion |
| `-roletools menu` | — | Administrator or required Discord permission | Manage published role menus. |
| `-roletools menu add` | — | Administrator or required Discord permission | Add shared-catalog roles to a saved menu. |
| `-roletools menu archive` | — | Administrator or required Discord permission | Archive an unpublished menu while keeping its configuration. |
| `-roletools menu create` | — | Administrator or required Discord permission | Create an unpublished named menu using roles from the shared library. |
| `-roletools menu delete` | — | Administrator or required Discord permission | Permanently delete an unpublished menu; append `confirm`. |
| `-roletools menu diagnose` | `diagnostics` | Administrator or required Discord permission | Check a menu for missing roles, messages, emoji, and permissions. |
| `-roletools menu duplicate` | — | Administrator or required Discord permission | Copy a saved menu into a new unpublished draft. |
| `-roletools menu layout` | — | Administrator or required Discord permission | Set private, dropdown, reactions, or role_channel layout. |
| `-roletools menu presentation` | — | Administrator or required Discord permission | Set `label \| description \| emoji \| group`; omit values to reset. |
| `-roletools menu preview` | — | Administrator or required Discord permission | Preview a saved menu without changing its published messages. |
| `-roletools menu publish` | — | Administrator or required Discord permission | Publish or move a saved menu using its selected layout. |
| `-roletools menu remove` | — | Administrator or required Discord permission | Remove roles from a saved menu without deleting the Discord roles. |
| `-roletools menu restore` | — | Administrator or required Discord permission | Restore an archived menu to active management. |
| `-roletools menu sync` | — | Administrator or required Discord permission | Synchronize a saved menu's published Discord messages. |
| `-roletools menu unpublish` | — | Administrator or required Discord permission | Remove published messages but keep the saved menu. |
| `-roletools menu view` | — | Administrator or required Discord permission | Show one saved menu's roles, layout, and destination. |
| `-roletools message` | — | Member | Manage RoleTools messages. |
| `-roletools message edit` | — | Member | Edit a bots message to include Role Buttons |
| `-roletools message editbutton` | — | Member | Edit a bots message to include Role Buttons |
| `-roletools message editselect` | — | Member | Edit a bots message to include Select Menus |
| `-roletools message send` | — | Member | Send a select menu to a specified channel for role assignment |
| `-roletools message sendbutton` | — | Member | Send buttons to a specified channel with optional message. |
| `-roletools message sendselect` | — | Member | Send a select menu to a specified channel for role assignment |
| `-roletools migrationstatus` | — | Bot maintainer | Owner migration status. |
| `-roletools notify` | `notifications` | Administrator or required Discord permission | Configure role notices. |
| `-roletools notify channel` | — | Administrator or required Discord permission | Send successful member role-change notices to this channel. |
| `-roletools notify disable` | `clear`, `off` | Administrator or required Discord permission | Disable public RoleTools role-change notices for this server. |
| `-roletools picker` | — | Administrator or required Discord permission | Create and maintain scalable self-role picker cards. |
| `-roletools picker add` | — | Administrator or required Discord permission | Add one or more roles to a picker without rebuilding it. |
| `-roletools picker create` | — | Administrator or required Discord permission | Create and publish a managed role picker card. |
| `-roletools picker delete` | — | Administrator or required Discord permission | Delete a picker configuration and remove its published card. |
| `-roletools picker move` | — | Administrator or required Discord permission | Move a picker role to a one-based position and switch to manual ordering. |
| `-roletools picker remove` | — | Administrator or required Discord permission | Remove one or more roles from a picker without deleting the Discord roles. |
| `-roletools picker replace` | — | Administrator or required Discord permission | Replace a picker role in place while retaining its position. |
| `-roletools picker sort` | — | Administrator or required Discord permission | Sort a picker alphabetically or retain manual order. |
| `-roletools picker sync` | — | Administrator or required Discord permission | Refresh a published picker card from its saved configuration. |
| `-roletools picker view` | — | Administrator or required Discord permission | Show a picker's saved roles and published message. |
| `-roletools reaction` | `react`, `reactions` | Member | Manage reaction roles. |
| `-roletools reaction bulk` | `bulkcreate`, `bulkmake` | Administrator or required Discord permission | Create multiple roles reactions for a single message |
| `-roletools reaction cleanup` | — | Administrator or required Discord permission | Cleanup old/missing reaction roles and settings. |
| `-roletools reaction clearreact` | `clearreacts` | Administrator or required Discord permission | Clear the reactions for reaction roles. This will remove |
| `-roletools reaction create` | `make`, `setup` | Administrator or required Discord permission | Create a reaction role |
| `-roletools reaction ownercleanup` | — | Bot maintainer | Cleanup old/missing reaction roles and settings on the bot. |
| `-roletools reaction reactroles` | `reactionroles`, `reactrole` | Administrator or required Discord permission | View current bound roles in the server |
| `-roletools reaction remove` | `rem` | Administrator or required Discord permission | Remove a reaction role |
| `-roletools removerole` | — | Administrator or required Discord permission | Remove a role in bulk. |
| `-roletools required` | `req`, `require`, `requires` | Member | Manage role requirements. |
| `-roletools required add` | — | Administrator or required Discord permission | Add role requirements |
| `-roletools required any` | — | Administrator or required Discord permission | Set the required roles to require any of the roles instead of all of them |
| `-roletools required remove` | — | Administrator or required Discord permission | Remove role requirements |
| `-roletools select` | `selects` | Administrator or required Discord permission | Manage dropdown roles. |
| `-roletools select cleanup` | — | Administrator or required Discord permission | Check each select menu that has registered a message still exists and remove buttons with |
| `-roletools select create` | — | Administrator or required Discord permission | Create a select menu |
| `-roletools select createoption` | `addoption` | Administrator or required Discord permission | Create a select menu option |
| `-roletools select delete` | `del`, `remove` | Administrator or required Discord permission | Delete a saved select menu. |
| `-roletools select deleteoption` | `deloption`, `remoption`, `removeoption` | Administrator or required Discord permission | Delete a saved option. |
| `-roletools select view` | `list` | Administrator or required Discord permission | View current select menus setup for role assign in this server. |
| `-roletools select viewoptions` | `listoption`, `listoptions`, `viewoption` | Administrator or required Discord permission | View current select menus setup for role assign in this server. |
| `-roletools selfassignable` | `selfadd`, `selfassign` | Administrator or required Discord permission | Allow self-assignment. |
| `-roletools selfremovable` | `selfrem` | Administrator or required Discord permission | Allow self-removal. |
| `-roletools selfrole` | — | Member | Toggle a self-role. |
| `-roletools setup` | — | Administrator or required Discord permission | Open interactive setup. |
| `-roletools sticky` | — | Administrator or required Discord permission | Configure sticky roles. |
| `-roletools temporary` | `temp` | Member | Manage temporary roles. |
| `-roletools temporary list` | — | Member | List the currently pending temporary roles and when they expire. |
| `-roletools temporary set` | — | Administrator or required Discord permission | Set the duration the role will last before being removed. |
| `-roletools viewroles` | `viewrole` | Member | View available or configured roles. |
| `-selfroles` | — | Member | List available self-roles. |

Live `-help` output remains authoritative for syntax, enabled state, hidden commands,
arguments, cooldowns, and server-specific access.
