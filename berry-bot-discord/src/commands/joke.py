import random
import discord


class Joke(discord.Cog):
   def __init__(self, bot: discord.Bot):
      self.bot = bot


   @discord.slash_command(name="joke", description="Get a fresh berry joke from JojoPuppy911")
   async def command(self, ctx: discord.ApplicationContext, hidden: discord.Option(bool, name="hidden", description="Hide the reply so that only you can see it?", required=False) = False):
      # get a random berry joke
      joke = random.choice([
         [ "what do you call a sad strawberry?", "a blue berry 😔" ],
         [ "what do you call berries in the wind?", "\"blewberries\"" ],
         [ "how do you fix a blueberry?", "with a blueberry patch" ],
         [ "what do you call a russian raspberry dipped in lighter fluid?", "rasp-butane!" ],
         [ "what did one cranberry say to another at christmas?", "'tis the season to be jelly!" ],
         [ "what kind of fruit is a crook?", "a _strobbery_!" ],
         [ "what is the difference between a pirate and a cranberry farmer?", "a pirate buries his treasure while a cranberry farmer treasures his berries! " ],
         [ "what do you get when you walk around with berries in your shoes?", "toe jam!" ],
         [ "how can blueberries talk on the phone if they have no hands?", "they use bluetooth!" ],
         [ "how do berries appear?", "they come out of the blue!" ],
         [ "why were the little strawberries upset?", "because their parents were in a jam!" ],
         [ "why can't you make a crumble with 3.14 blackberries?", "because that'd be a pi!" ],
         [ "why was the raspberry by himself?", "because the banana split!" ],
         [ "what do you call a magic berry?", "cherry potter!" ],
         [ "why did the strawberry stop in the middle of the road?", "because it ran out of juice!" ],
         [ "what is a scarecrow's favourite fruit?", "straw-berries!" ],
         [ "what is red, made of strawberries, and sucks your blood?", "a jam-pire!" ],
         [ "what do you do to a dead berry?", "you \\*berry\\* it" ],
         [ "what is it called when a raspberry is late to class?", "they're tarty!" ],
         [ "what did the blueberry pie say to the pecan pie?", "\"you're nuts!\"" ],
         [ "why did the blueberry go out with the fig?", "because it couldn't find a date.." ],
         [ "where do strawberries play their saxophones?", "at jam sessions!" ],
         [ "how do you make a blueberry?", "you strangle a pea!" ]
      ])

      # components
      class View(discord.ui.DesignerView):
         def __init__(self):
            super().__init__(timeout=120)
            self.revealed = False

            self.text_display = discord.ui.TextDisplay(content=f"### {joke[0]}")
            self.add_item(self.text_display)

            self.action_row = discord.ui.ActionRow()
            self.button = discord.ui.Button(style=discord.ButtonStyle.primary, custom_id=f"{ctx.interaction.id}", label=f"{joke[0].split()[0]}?")
            self.button.callback = self.button_callback

            self.action_row.add_item(self.button)
            self.add_item(self.action_row)

         async def button_callback(self, interaction: discord.Interaction):
            if interaction.user.id == ctx.user.id:
               self.revealed = True
               self.stop()
               self.remove_item(self.action_row)
               self.text_display.content = f"### {joke[0]}\n{joke[1]}"
               await interaction.response.edit_message(view=self)

            else:
               class View(discord.ui.DesignerView):
                  def __init__(self):
                     super().__init__()
                     text_display = discord.ui.TextDisplay(content=joke[1])
                     self.add_item(text_display)
               await interaction.response.send_message(view=View(), ephemeral=True)

         async def on_timeout(self):
            if self.revealed:
               return

            self.button.disabled = True
            await ctx.interaction.edit_original_message(view=self)

      # respond to the interaction
      await ctx.respond(view=View(), ephemeral=hidden)


def setup(bot: discord.Bot):
   bot.add_cog(Joke(bot))