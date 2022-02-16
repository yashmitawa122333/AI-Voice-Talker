import os
import random


def play_audio_songs():
    music_dir = "D:\\music_songs"
    songs = os.listdir(music_dir)
    randomno = random.randint(0, len(songs)-1)
    # print(songs)
    # print(randomno)
    os.startfile(os.path.join(music_dir, songs[randomno]))

def play_video_songs():
    video_dir = "D:\\video_songs"
    songs = os.listdir(video_dir)
    randomno = random.randint(0, len(songs)-1)
    # print(songs)
    # print(randomno)
    os.startfile(os.path.join(video_dir, songs[randomno]))

# if __name__ =='__main__':
#     play_video_songs()