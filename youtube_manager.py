import yt_dlp

ydl_opts = {
            'format': 'bestaudio/best',
            'quiet': True,
            'extractaudio': True,   # Ensure only audio is extracted
            'audioformat': 'mp3',   # Output format for audio
            'outtmpl': '%(id)s.%(ext)s',
            'noplaylist': True,
            'nocheckcertificate': True,
            'force_generic_extractor': True
        }

def get_video_info(url):

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
    
    return info['url'], info['title']

def search_youtube(query):
    # Use ytsearch: followed by the query to perform a search
    search_query = f"ytsearch:{query}"
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(search_query, download=False)
        
        # Extract the first video result
        if 'entries' in info:
            video = info['entries'][0]  # Take the first entry from the result
            return video.get('url'), video.get('title')
        else:
            return None