# Command and documentation status

This documentation uses audience guides, module overviews, setup workflows, and source-reviewed command references.

## Source of truth

The live bot is authoritative for loaded cogs, enabled commands, aliases, current help text, permission checks, and server configuration. Use -help and -help <command> for the current result visible to your account.

Public pages describe workflows and intended audiences. They must not expose global credentials, private endpoints, hidden maintainer utilities, or internal callback details.

The [complete command reference](reference/index.md) records command paths, aliases,
descriptions, declared privilege levels, loaded modules, Red version, and production
inventory metadata. The older lists remain migration references, not a current permission
map.

## Review state

- Exhaustive member/staff/server-owner/bot-maintainer catalogs and boundaries: established.
- Server-owner cog selection and setup guidance: established.
- Feature pages and legacy setup entry points: reviewed and linked to current references.
- Official production inventory: generated and reviewed 2026-10-11.
- Sanitized audience indexes and complete 1,181-entry command reference: established.
- All 1,181 command paths assigned once to a primary audience tier: established.
- Complete module catalog with 41 module/core overview pages: established.
- Manual baseline, link, audience-count, prefix, and privacy validation: established.
- Repeatable catalog regeneration from future `-docsreport` exports: established with `tools/update_command_docs.py`.
