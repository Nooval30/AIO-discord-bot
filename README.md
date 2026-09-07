# Discord Bot

Bot Discord modular berbasis `discord.py`. Fitur pertama: **Welcome & Goodbye message**.

## Struktur

```
discord-bot/
├── main.py           # entry point, auto-load semua cog
├── config.py         # baca konfigurasi dari .env
├── requirements.txt
├── .env.example       # contoh isi .env
└── cogs/
    └── welcome.py     # fitur welcome & goodbye
```

Tiap fitur baru = file baru di folder `cogs/`. Gak perlu edit `main.py`.

## Cara Setup

1. **Buat bot di Discord Developer Portal**
   - Buka https://discord.com/developers/applications → New Application
   - Bot tab → Add Bot → copy token
   - Di tab "Bot", aktifkan **Server Members Intent** dan **Message Content Intent** (bagian Privileged Gateway Intents) — wajib buat fitur welcome/goodbye

2. **Install dependency**
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup config**
   - Copy `.env.example` jadi `.env`
   - Isi `DISCORD_TOKEN` dengan token bot lo
   - Aktifkan Developer Mode di Discord (Settings → Advanced), lalu klik kanan channel yang mau dipake buat welcome/goodbye → Copy Channel ID
   - Isi `WELCOME_CHANNEL_ID` dan `GOODBYE_CHANNEL_ID`

4. **Invite bot ke server**
   - Di Developer Portal → OAuth2 → URL Generator
   - Centang scope `bot`, permission minimal: `Send Messages`, `Embed Links`, `View Channel`
   - Buka URL yang di-generate, pilih server lo

5. **Jalankan bot**
   ```bash
   python main.py
   ```

## Nambah Fitur Baru

Bikin file baru di `cogs/`, contoh `cogs/moderasi.py`, dengan pola:

```python
from discord.ext import commands

class NamaFitur(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # command atau listener di sini

async def setup(bot):
    await bot.add_cog(NamaFitur(bot))
```

Restart bot, otomatis ke-load.
