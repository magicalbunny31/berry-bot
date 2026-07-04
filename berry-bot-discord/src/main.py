# 🫐 berry-bot-discord
# 👥 magicalbunny31 (https://nuzzles.dev)
# 👥 issu (https://github.com/TheLivingPepsi)
# 🗓️ 2021 - 2026
# 🏡 https://flufflestack.nuzzles.dev/projects/berry-bot
# 🔗 https://github.com/magicalbunny31/berry-bot


# the discord client
import discord

bot = discord.Bot(
   activity = discord.Activity(
      name = "Gentle Berry's Server 2018-2022 🕯️🫐",
      type = discord.ActivityType.watching
   ),

   status = discord.Status.online,

   intents = discord.Intents(
      messages = True,       # required for message events
      message_content = True # required for message events
   )
)


# cogs
import os

for directory in ["commands", "events"]:
   for filename in os.listdir(f"./src/{directory}"):
      if not filename.endswith(".py"):
         continue
      bot.load_extension(f"src.{directory}.{filename[0:-3]}")


# final logs
print("🫐 berry-bot-discord initialised!")


# run the bot
bot.run(os.getenv("DISCORD_TOKEN"))