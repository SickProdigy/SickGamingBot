# SickGamingBot public documentation workflow

- SickGamingBot uses `-` as its public command prefix. Do not use a generic variable-prefix placeholder in user-facing pages.
- The official documentation baseline is the package list loaded by the production
  SickGamingBot runtime, plus always-loaded Red core commands. Cog data directories can
  remain after a package is unloaded and are not sufficient evidence by themselves.
- When the loaded package list changes, reconcile all of these together:
  - `docs/features/index.md`
  - `docs/modules/`
  - `docs/reference/`
  - curated audience guides under `docs/commands/`
  - `docs/command-status.md`
- Module pages explain purpose, audience, top-level command families, and setup/access
  expectations. Reference pages enumerate every command and subcommand.
- Keep live `-help`, `-help <command>`, and `-help <command> <subcommand>` documented as
  authoritative because runtime permissions and disabled state vary by server and user.
- Do not publish private server addresses, SSH details, filesystem paths, credentials,
  tokens, or configuration values in this public repository.
- Preserve the legacy command-list files under `archive/legacy-command-lists/` as
  historical snapshots while the owner evaluates the current documentation direction.
- Regenerate reference and audience catalogs with `tools/update_command_docs.py` using
  the sanitized production `-docsreport` JSON, then reconcile narrative pages and counts.
