# AIO Discord Bot

Bot Discord modular berbasis `python`. All-in-one, tinggal nambah fitur baru kapan aja.

## Fitur Saat Ini

-  **Welcome & Goodbye** — kirim embed otomatis pas member join/leave server
-  **Musik Player** — search lagu by judul atau paste link YouTube, download otomatis, play/pause/skip/stop/queue

## Struktur

```
AIO-discord-bot/
├── main.py           # entry point, auto-load semua cog
├── config.py         # baca konfigurasi dari .env
├── requirements.txt
├── .env.example       # contoh isi .env
└── cogs/
    ├── welcome.py     # fitur welcome & goodbye
    └── music.py       # fitur musik player
```

Tiap fitur baru = file baru di folder `cogs/`. Gak perlu edit `main.py`.

## Cara Setup

1. **Buat bot di Discord Developer Portal**
   - Buka https://discord.com/developers/applications → New Application
   - Bot tab → Add Bot → copy token
   - Aktifin **Server Members Intent** dan **Message Content Intent** (Privileged Gateway Intents) — wajib

2. **Install dependency**
   ```bash
   python -m pip install -r requirements.txt
   ```

3. **Install FFmpeg** (dibutuhin buat fitur musik)
   - Download dari https://www.gyan.dev/ffmpeg/builds/ atau `winget install ffmpeg`
   - Cek lokasi `ffmpeg.exe` di laptop lo, isi ke `FFMPEG_EXECUTABLE` di `cogs/music.py`

4. **Setup config**
   - Copy `.env.example` jadi `.env`
   - Isi `DISCORD_TOKEN` dengan token bot lo
   - Isi `WELCOME_CHANNEL_ID` dan `GOODBYE_CHANNEL_ID` (aktifin Developer Mode di Discord buat copy channel ID)

5. **Invite bot ke server**
   - Developer Portal → OAuth2 → URL Generator
   - Scope `bot`, permission: `Send Messages`, `Embed Links`, `View Channel`, `Connect`, `Speak`

6. **Jalankan bot**
   ```bash
   python main.py
   ```

## Command

**Musik**
| Command | Alias | Fungsi |
|---|---|---|
| `!play <judul/link>` | `!p` | Cari & muter lagu |
| `!skip` | | Skip ke lagu berikutnya |
| `!pause` | | Jeda lagu |
| `!resume` | | Lanjutin lagu |
| `!stop` | | Berhenti, bot keluar voice channel |
| `!queue` | `!q` | Liat antrian lagu |
