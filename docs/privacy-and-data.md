# Privacy and data

Different features store different data. Review each integration's setup message and ask server staff which optional features are enabled.

- Never send passwords, recovery codes, payment details, private keys, or unrestricted administrator tokens to the bot.
- Enter secrets only through a documented private prompt or approved website flow.
- Personal connections should be scoped, revocable, and removable by the member.
- Guild integrations should use separate credentials with minimum required permissions.
- Public logs and support messages must not contain credentials.

Use a feature's disconnect command when available. Server owners should also revoke external credentials when retiring an integration; removing the bot does not necessarily revoke a token.

For stored-personal-data requests, use the bot's documented data-management commands or contact SickGaming maintainers. Exact data and deletion behavior depend on the loaded feature.
