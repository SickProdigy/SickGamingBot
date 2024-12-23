# Reaction Roles Explained

Syntax: -roletools
</br>
*Commands for creating custom role settings*
</br>
**Note: use '-help roletools' for helpful info in discord. can define sub commands also like '-help roletools reaction'

Subcommands: # Each Sub command can have more sub commands. 
* atomic Set the atomicity of role assignment.
* autorole Set a role to be automatically applied when a user joi...
* buttons Setup role buttons
* cost Set the cost to acquire a role.
* exclude Set role exclusions
* forcerole Force a sticky role on one or more users.
* forceroleremove Force remove sticky role on one or more users.
* giverole Gives a role to designated members.
* globalatomic Set the atomicity of role assignment.
* include Set role inclusion
* message Commands for sending/editing messages for roletools
* reaction Reaction role settings
* removerole Removes a role from the designated members.
* required Set role requirements
* select Setup role select menus
* selfadd Set whether or not a user can apply the role to themsel...
* selfrem Set whether or not a user can remove the role from them...
* selfrole Add or remove a defined selfrole
* sticky Set whether or not a role will be re-applied when a user...
* viewroles View current roletools setup for each role in the ser...

<p> Note* use '-help roletools' and further like '-help roletools reaction create' to get helpful 
information in discord from bot on that specific command! </p>

Testing:
* -roletools button create role1 @role label: Super fun role style: blurple emoji: 😀
* -roletools button create Among-Us @Among Us  label: Among Us style: blurple emoji: :ghost:

<p> Syntax for adding roles: -roletools reaction create <message> <emoji> <role> </p>
<p> Aliases: '-roletools reaction make' and '-roletools reaction setup'

Create a reaction role:
- <message> can be the channel_id-message_id pair
- from copying message ID while holding SHIFT or a message link
- <emoji> The emoji you want people to react with to get the role.
- <role> The role you want people to receive for reacting.

Different emoji = different reaction to react with
* -roletools reaction create 1147713281994281040 :ghost: @Among Us
* -roletools reaction create 765426801165729794 :thumbsup: @Among Us
* -roletools reaction create 765426822010765323 :thumbsup: @Apex Legends
* -roletools reaction create 765426836909326336 :thumbsup: @Ark
* -roletools reaction create 765426851622813706 :thumbsup: @Call of Duty
* -roletools reaction create 765426871973707776 :thumbsup: @CSGO
* -roletools reaction create 765426919638302780 :thumbsup: @GTA V
* -roletools reaction create 765426931839270932 :thumbsup: @Fall Guys
* -roletools reaction create 765426947127246848 :thumbsup: @Fortnite
* -roletools reaction create 765426973304422450 :thumbsup: @League of Legends
* -roletools reaction create 765426987241439272 :thumbsup: @Minecraft
* -roletools reaction create 765427002517749780 :thumbsup: @Rocket League
* -roletools reaction create 765427020758646785 :thumbsup: @Rust
* -roletools reaction create 1147715383214739536 :thumbsup: @theHunter
* -roletools reaction create 1147722664417435807 :thumbsup: @JackBox