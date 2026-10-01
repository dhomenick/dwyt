from pytube import YouTube
url = 'https://www.youtube.com/live/WpoqhxbFacE'
yt = YouTube(url)
stream = yt.streams.get_highest_resolution()
stream.download()

