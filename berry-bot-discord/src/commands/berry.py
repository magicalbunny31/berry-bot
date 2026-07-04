import os
import random
import discord


class Berry(discord.Cog):
   def __init__(self, bot: discord.Bot):
      self.bot = bot


   @discord.slash_command(name="berry", description="Get a random berry media")
   async def command(self, ctx: discord.ApplicationContext, hidden: discord.Option(bool, name="hidden", description="Hide the reply so that only you can see it?", required=False) = False):
      # defer the interaction
      await ctx.defer(ephemeral=hidden)

      # get a random berry media
      raw_berry_filename = random.choice(os.listdir("./assets/berries"))
      extension = raw_berry_filename.split(".")[1]
      berry_filename = f"berry.{extension}"

      # components
      class View(discord.ui.DesignerView):
         def __init__(self):
            super().__init__()
            gallery = discord.ui.MediaGallery()
            gallery.add_item(url=f"attachment://{berry_filename}")
            self.add_item(gallery)

      # edit the deferred interaction
      file = discord.File(filename=berry_filename, fp=f"./assets/berries/{raw_berry_filename}")
      await ctx.interaction.edit_original_response(view=View(), files=[file])


def setup(bot: discord.Bot):
   bot.add_cog(Berry(bot))