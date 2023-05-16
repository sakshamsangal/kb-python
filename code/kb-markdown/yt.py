# importing the module
from pytube import YouTube

# where to save
SAVE_PATH = "D:/"  # to_do

# link of the video to be downloaded
# link = "https://www.youtube.com/watch?v=xWOoBJUqlbI"
link = "https://youtu.be/q4A2eq2mtx0"


def download(link):
    # youtubeObject = YouTube(link)
    # videos = youtubeObject.streams.filter(file_extension="mp4")
    # # youtubeObject = youtubeObject.streams.get_highest_resolution()
    # youtubeObject = videos.streams.get_by_resolution("1080p")
    # try:
    #     youtubeObject.download(SAVE_PATH)
    # except:
    #     print("An error has occurred")
    # print("Download is completed successfully")
    yt = YouTube(link)
    # videos = video.streams.filter(file_extension="mp4")
    # stream = videos.get_by_resolution("1080p")

    # Quality Options
    stream = str(yt.streams.filter(progressive=True))
    print(stream)
    # stream = stream[1:]
    # stream = stream[:-1]
    # streamlist = stream.split(", ")
    # print("\nAll available options for downloads:\n")
    # for i in range(0, len(streamlist)):
    #     st = streamlist[i].split(" ")
    #     print(i + 1, ".", "Resolution: ", st[3][4:], sep="")


    # if (stream == None):
    #     stream = videos.get_highest_resolution()
    # print("{} Downloading...".format(stream.title))
    # stream.download(SAVE_PATH)
    # print("{} Downloaded...".format(stream.title))


# link = input("Enter the YouTube video URL: ")
download(link)
