# PixelmonStatsDiscordBot

This is a small Discord bot made so that players on my server can access the EVs and IVs of pokemon in their party.  Works with the Pixelmon-Reforged mod.

## How it works
First, a player must link their discord account to their minecraft account.  This is to ensure that you can only access your own pokemon's stats.  To do this, a player can type: `!!register <minecraft username>` .  The bot will perform some sanity checks, such as ensuring that it is a valid minecraft username.

After registering, a player can type `!!check_poke #`, where # is an integer from 1-6, specifying which pokemon in their party they would like.  The bot will return the EVs and IVs of said pokemon.
