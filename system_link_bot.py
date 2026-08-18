# [System Link] Bot
# Programmed With Codex
# MIT License: Copyright (c) 2026 Kevin de 3ngineer

import os
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv

# load environmental variables

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

if not TOKEN:
    raise RuntimeError(
        "DISCORD_TOKEN was not found. "
        "make sure you created a .env file with DISCORD_TOKEN=your_token"
    )


# links

WEBSITE = "https://guns.lol/kevinde3ngineer" # change with your own info
GITHUB = "https://github.com/kevinde3ngineer" # change with your own info
YOUTUBE = "https://www.youtube.com/channel/UCJDC2xHrSmBhc7IvTgRFw9g" # change with your own info
TIKTOK = "https://tiktok.com/@kevinde3ngineer" # change with your own info
MAKERWORLD = "https://makerworld.com/en/@kevinde3ngineer" # change with your own info

GUNS_LOL = "https://guns.lol/kevinde3ngineer" # change with your own info


# bot setup

intents = discord.Intents.default()

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)


# buttons (they could be changed)

class LinksView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

        self.add_item(
            discord.ui.Button(
                label="Website",
                emoji="🌐",
                url=WEBSITE,
                style=discord.ButtonStyle.link
            )
        )

        self.add_item(
            discord.ui.Button(
                label="GitHub",
                emoji="💻",
                url=GITHUB,
                style=discord.ButtonStyle.link
            )
        )

        self.add_item(
            discord.ui.Button(
                label="YouTube",
                emoji="▶️",
                url=YOUTUBE,
                style=discord.ButtonStyle.link
            )
        )

        self.add_item(
            discord.ui.Button(
                label="TikTok",
                emoji="🎵",
                url=TIKTOK,
                style=discord.ButtonStyle.link
            )
        )

        self.add_item(
            discord.ui.Button(
                label="MakerWorld",
                emoji="🖨️",
                url=MAKERWORLD,
                style=discord.ButtonStyle.link
            )
        )


# embed

def create_links_embed():
    embed = discord.Embed(
        title="Official Links",
        description=(
            f"> **Website:** {WEBSITE}\n"
            f">\n"
            f"> **GitHub:** {GITHUB}\n"
            f">\n"
            f"> **YouTube:** {YOUTUBE}\n"
            f">\n"
            f"> **TikTok:** {TIKTOK}\n"
            f">\n"
            f"> **MakerWorld:** {MAKERWORLD}"
        ),
        color=discord.Color.blurple()
    )

    embed.add_field(
        name="guns.lol",
        value=f"[View my guns.lol profile]({GUNS_LOL})",
        inline=False
    )

    embed.set_footer(
        text="official links"
    )

    return embed


# /CHANNEL command

@bot.tree.command(
    name="channel",
    description="post the official links in this channel"
)
@app_commands.checks.has_permissions(administrator=True)
async def channel(interaction: discord.Interaction):

    if interaction.channel is None:
        await interaction.response.send_message(
            "I couldn't access this channel",
            ephemeral=True
        )
        return

    embed = create_links_embed()

    await interaction.channel.send(
        embed=embed,
        view=LinksView()
    )

    await interaction.response.send_message(
        "official links posted",
        ephemeral=True
    )


# command error handling

@channel.error
async def channel_error(
    interaction: discord.Interaction,
    error: app_commands.AppCommandError
):

    if isinstance(error, app_commands.MissingPermissions):

        if not interaction.response.is_done():
            await interaction.response.send_message(
                "❌ You need Administrator permission to use /channel.",
                ephemeral=True
            )

        return

    print(f"Error while running /channel: {error}")

    if not interaction.response.is_done():
        await interaction.response.send_message(
            "something went wrong",
            ephemeral=True
        )


# bot ready

@bot.event
async def on_ready():

    print(f"Logged in as {bot.user}")

    try:
        synced = await bot.tree.sync()
        print(f"synced {len(synced)} slash command(s).")

    except Exception as error:
        print(f"failed to sync commands: {error}")

    print("Bot is ready.")


# start bot

bot.run(TOKEN)
