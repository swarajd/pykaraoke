import csv
import youtube_dl

class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)

def downloadSong(url, filename=None):

    ydl_opts = {
        'logger': MyLogger(),
        'format': 'mp4',
        'outtmpl': '%(id)s.%(ext)s'
    }

    if filename is not None:
        ydl_opts["outtmpl"] = filename

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

with open('songs.csv') as songfile:
    songreader = csv.reader(songfile)
    next(songreader, None)
    for row in songreader:
        fname = "{}.mp4".format(row[0])
        downloadSong(row[3], fname)