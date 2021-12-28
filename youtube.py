import youtube_dl
import os


# Youtube Example link: https://youtu.be/T_1Nx5YSuOA


def get_youtube_video(self, url: str):
    ydl_opts = {
        'outtmpl': os.getenv("OUTPUT_PATH") + '/%(title)s.%(ext)s',
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
