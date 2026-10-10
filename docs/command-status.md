# Command and documentation status

This documentation is migrating from hand-maintained command dumps to audience- and feature-based guides.

## Source of truth

The live bot is authoritative for loaded cogs, enabled commands, aliases, current help text, permission checks, and server configuration. Use -help and -help <command> for the current result visible to your account.

Public pages describe workflows and intended audiences. They must not expose global credentials, private endpoints, hidden maintainer utilities, or internal callback details.

The older lists remain as migration references, not a current permission map. A future sanitized inventory should record command name, aliases, cog, description, declared privilege level, documentation category, and reviewed bot version or commit. It can detect stale documentation without exporting secrets or configuration.

## Review state

- Audience navigation and member/staff/server-owner boundaries: established.
- Existing feature pages: retained, pending command-by-command review.
- Official SickGamingBot cog baseline: reviewed 2026-10-10.
- Sanitized audience command indexes: established; subcommand review remains ongoing.
- Automated stale-documentation check against a live bot export: planned.
