# Initial server setup

## Checklist

- [ ] Add SickGamingBot by sending `-invite` in a direct message to the bot or using the [published invite](https://discord.com/oauth2/authorize?client_id=691452746632658954&scope=bot&permissions=0), then review every requested permission.
- [ ] Create or select a bot channel for help and commands.
- [ ] Verify that `-help` works and shows the expected commands.
- [ ] Place the bot role only as high as required for roles it must manage.
- [ ] Confirm channel permissions for messages, embeds, reactions, threads, and intended moderation features.
- [ ] Assign moderator, administrator, and feature-manager access deliberately.
- [ ] Choose modules with the [server-owner cog setup guide](cog-setup.md).
- [ ] Configure welcome, roles, moderation logging, and optional announcements one feature at a time.
- [ ] Test member and staff behavior with representative non-owner accounts.
- [ ] Review [privacy and data](../privacy-and-data.md) before external connections.
- [ ] Record who owns each integration and how it can be revoked.

Avoid granting Discord Administrator as a shortcut. Role hierarchy still controls what the bot can manage. Live help is more reliable than old static command lists because it reflects loaded cogs, disabled commands, and the invoking member's checks.
