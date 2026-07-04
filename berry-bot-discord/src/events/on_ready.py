import discord


class OnReady(discord.Cog):
   def __init__(self, bot: discord.Bot):
      self.bot = bot


   @discord.Cog.listener(once=True)
   async def on_ready(self):
      guild_count = len(self.bot.guilds)
      print(f"discord client ready as @{self.bot.user.name}#{self.bot.user.discriminator} with {guild_count} {"guild" if guild_count == 1 else "guilds"}")


def setup(bot: discord.Bot):
   bot.add_cog(OnReady(bot))