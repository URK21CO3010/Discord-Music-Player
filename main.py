import discord
import asyncio
import youtube_manager
import caesar

bot = discord.Client(intents = discord.Intents.all())

channel_id = 1006838392002195456

@bot.event
async def on_ready() -> None:
    for guild in bot.guilds:
        for channel in guild.channels:
            if channel.name == 'general':
                try:
                    await channel.send("I am ready to play some tunes!\nNormal mode: play <song name/youtube link>\nNightcore mode: nightcore <song name/youtube link>\nDeep mode: deep <song name/youtube link>\nWant some recommendations? Ask our AI: ai <your prompt>")
                except:
                    pass
    await bot.change_presence(activity=discord.Game(name="some tunes!"))


@bot.event
async def on_message(message: discord.message.Message) -> None:
    
    if not message.author.bot:

        channel = bot.get_channel(channel_id)

        if message.content.lower().split()[0] in ['play', 'nightcore', 'deep']:
            parts = message.content.split()
            url = ""
            for i in range(1, len(parts)):
                url += parts[i] + ' '
            url = url[:-1]
            if not message.author.voice:
                await message.channel.send("You have not joined in any voice channels.")
            else:
                voice_channel = message.author.voice.channel
            
                if message.content.lower().startswith("play"):
                    await play_song(voice_channel, url, message.channel, 0)

                elif message.content.lower().startswith("nightcore"):
                    await play_song(voice_channel, url, message.channel, 1)
                
                else:
                    await play_song(voice_channel, url, message.channel, 2)
        
        elif message.content.lower() == "disconnect":
            try:
                await voice_client.disconnect()
            except:
                pass


async def play_song(voice_channel, url: str, text_channel, mode):
    # Connect to the voice channel
    global voice_client
    voice_client = await voice_channel.connect()
    
    try:
        if url.startswith('http'):
            info = youtube_manager.get_video_info(url = url)
        else:
            info = youtube_manager.search_youtube(query = url)

        if info:
            audio_url, title = info

            if mode == 0:
                # Configure FFmpeg options for streaming audio
                ffmpeg_options = {
                    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                    'options': '-vn'
                }
            elif mode == 1:
                # Nightcore Mode
                ffmpeg_options = {
                    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                    'options': '-vn -af "asetrate=44100*1.25,atempo=1.05"'
                }
            
            elif mode == 2:
                # Deep Mode
                ffmpeg_options = {
                    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                    'options': '-vn -af "asetrate=44100*1.00,atempo=0.9"'
                }

            # Play the audio stream
            voice_client.play(discord.FFmpegPCMAudio(audio_url, **ffmpeg_options), after=lambda e: print(f'Player error: {e}') if e else None)

            await text_channel.send(f"Now playing: {title}")

            # Wait until the song is finished playing
            while voice_client.is_playing():
                await asyncio.sleep(1)

    
    except Exception as e:
        print(f"Error playing song: {e}")
        await text_channel.send("There was an error trying to play the song.")

    
    # Disconnect from the voice channel
    await voice_client.disconnect()

bot.run(caesar.caesar_decrypt("TAP3UgFeUKPeTAjeVAPgTgBgUn.NrcngH.6UeTdM_nhQzeIhHYnpHTsAKJlxerrcHN-_SZrv", 7))
