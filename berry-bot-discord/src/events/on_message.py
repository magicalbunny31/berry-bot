from src.data.channels import gateway
from src.data.users import mee6

import discord


class OnMessage(discord.Cog):
   def __init__(self, bot: discord.Bot):
      self.bot = bot


   @discord.Cog.listener(name="on_message")
   async def gateway(self, message: discord.Message):
      if message.channel.id != gateway or message.author.id != mee6 or not message.content.endswith("berried off to another server. <:chimeCollapse:799670500636229673>"):
         return

      await message.channel.send(content="https://www.youtube.com/watch?v=PqUenEMwsdQ", reference=message, allowed_mentions=discord.AllowedMentions(replied_user=False))


def setup(bot: discord.Bot):
   bot.add_cog(OnMessage(bot))