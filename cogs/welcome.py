import discord
from discord.ext import commands
import config


class Welcome(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        channel = self.bot.get_channel(config.WELCOME_CHANNEL_ID)
        if channel is None:
            print(f"[Welcome] WELCOME_CHANNEL_ID salah atau bot gak akses channelnya.")
            return

        embed = discord.Embed(
            title="SELAMAT DATANG",
            description=f"Welcome, {member.mention}! Selamat datang di **{member.guild.name}**.",
            color=discord.Color.from_str("#C6FF3D"),  # electric lime, sesuai tema lo
        )
        embed.set_thumbnail(url=member.display_avatar.url)
        embed.set_footer(text=f"Member ke-{member.guild.member_count}")

        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        channel = self.bot.get_channel(config.GOODBYE_CHANNEL_ID)
        if channel is None:
            print(f"[Goodbye] GOODBYE_CHANNEL_ID salah atau bot gak akses channelnya.")
            return

        embed = discord.Embed(
            title="Member Keluar 👋",
            description=f"**{member.name}** telah meninggalkan server. Sampai jumpa!",
            color=discord.Color.dark_grey(),
        )
        embed.set_thumbnail(url=member.display_avatar.url)
        embed.set_footer(text=f"Sisa member: {member.guild.member_count}")

        await channel.send(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(Welcome(bot))
