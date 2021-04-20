from pytube import YouTube

print('url: ',end='')
url=input()
print('resolution: ', end='')
resolution=input()
only_audio=False
print('only_audio: ', end='')
if input():
    only_audio=True

if only_audio:
    yt=YouTube(url).streams.filter(only_audio=True).first()
else:
    if resolution==0 or resolution==None:
        yt=YouTube(url).streams.filter().order_by("resolution").desc().first()
    else:
        yt=YouTube(url).streams.filter().get_by_resolution(resolution)

yt.download()