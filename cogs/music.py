import asyncio
import os
import discord
from discord.ext import commands
import yt_dlp

FFMPEG_EXECUTABLE = r"C:\Users\Admin\AppData\Local\Microsoft\WinGet\Links\ffmpeg.exe"

DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

YDL_OPTIONS = {
    "format": "bestaudio/best",
    "noplaylist": True,
    "default_search": "ytsearch1",
    "quiet": True,
    "no_warnings": True,
    "outtmpl": os.path.join(DOWNLOAD_DIR, "%(id)s.%(ext)s"),
    "postprocessors": [{
        "key": "FFmpegExtractAudio",
        "preferredcodec": "mp3",
        "preferredquality": "192",
    }],
    "ffmpeg_location": FFMPEG_EXECUTABLE,
}


class Music(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.queue = {}

    def get_queue(self, guild_id: int) -> list:
        if guild_id not in self.queue:
            self.queue[guild_id] = []
        return self.queue[guild_id]

    async def search_and_download(self, query: str) -> dict:
        """Cari lagu di YouTube, download jadi mp3, return path file + judul."""
        loop = asyncio.get_event_loop()

        def _download():
            with yt_dlp.YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(query, download=True)
                if "entries" in info:
                    info = info["entries"][0]
                filename = os.path.join(DOWNLOAD_DIR, f"{info['id']}.mp3")
                return {"title": info["title"], "filepath": filename}

        return await loop.run_in_executor(None, _download)

    @commands.command(name="play", aliases=["p"])
    async def play(self, ctx: commands.Context, *, query: str):
        """Cari dan mainin lagu. Contoh: !play judul lagu"""
        if ctx.author.voice is None:
            await ctx.send("❌ Masuk voice channel dulu, mas.")
            return

        voice_channel = ctx.author.voice.channel

        if ctx.voice_client is None:
            await voice_channel.connect()
        elif ctx.voice_client.channel != voice_channel:
            await ctx.voice_client.move_to(voice_channel)

        await ctx.send(f"🔎 Nyari & download: **{query}** ...")

        try:
            track = await self.search_and_download(query)
        except Exception as e:
            await ctx.send(f"❌ Gagal download lagu: {e}")
            return

        queue = self.get_queue(ctx.guild.id)
        queue.append(track)

        if ctx.voice_client.is_playing() or ctx.voice_client.is_paused():
            await ctx.send(f"➕ Ditambahin ke antrian: **{track['title']}**")
        else:
            await self.play_next(ctx)

    async def play_next(self, ctx: commands.Context):
        queue = self.get_queue(ctx.guild.id)
        if not queue:
            return

        track = queue.pop(0)

        if not os.path.exists(track["filepath"]):
            await ctx.send(f"❌ File gak ketemu: {track['filepath']}")
            await self.play_next(ctx)
            return

        source = discord.FFmpegPCMAudio(
            track["filepath"],
            executable=FFMPEG_EXECUTABLE,
        )

        def after_playing(error):
            if error:
                print(f"[Music] Error playback: {error}")
            fut = asyncio.run_coroutine_threadsafe(self.play_next(ctx), self.bot.loop)
            try:
                fut.result()
            except Exception as e:
                print(f"[Music] Error play_next: {e}")

        ctx.voice_client.play(source, after=after_playing)
        await ctx.send(f"🎶 Sekarang muter: **{track['title']}**")

    @commands.command(name="skip")
    async def skip(self, ctx: commands.Context):
        """Skip lagu yang lagi diputer."""
        if ctx.voice_client and (ctx.voice_client.is_playing() or ctx.voice_client.is_paused()):
            ctx.voice_client.stop()
            await ctx.send("⏭️ Lagu di-skip.")
        else:
            await ctx.send("❌ Gak ada lagu yang lagi diputer.")

    @commands.command(name="pause")
    async def pause(self, ctx: commands.Context):
        """Pause lagu."""
        if ctx.voice_client and ctx.voice_client.is_playing():
            ctx.voice_client.pause()
            await ctx.send("⏸️ Lagu di-pause.")
        else:
            await ctx.send("❌ Gak ada lagu yang lagi diputer.")

    @commands.command(name="resume")
    async def resume(self, ctx: commands.Context):
        """Lanjutin lagu yang di-pause."""
        if ctx.voice_client and ctx.voice_client.is_paused():
            ctx.voice_client.resume()
            await ctx.send("▶️ Lagu dilanjutin.")
        else:
            await ctx.send("❌ Gak ada lagu yang lagi di-pause.")

    @commands.command(name="stop")
    async def stop(self, ctx: commands.Context):
        """Stop musik dan keluar dari voice channel."""
        if ctx.voice_client:
            self.get_queue(ctx.guild.id).clear()
            await ctx.voice_client.disconnect()
            await ctx.send("⏹️ Musik dihentikan, bot keluar voice channel.")
        else:
            await ctx.send("❌ Bot gak lagi di voice channel.")

    @commands.command(name="queue", aliases=["q"])
    async def show_queue(self, ctx: commands.Context):
        """Liat antrian lagu."""
        queue = self.get_queue(ctx.guild.id)
        if not queue:
            await ctx.send("📭 Antrian kosong.")
            return

        text = "\n".join(f"{i+1}. {t['title']}" for i, t in enumerate(queue))
        await ctx.send(f"📋 **Antrian lagu:**\n{text}")


async def setup(bot: commands.Bot):
    await bot.add_cog(Music(bot))