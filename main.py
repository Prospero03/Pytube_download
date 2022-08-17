
from pytube import *


def download_video(url, output_path=None):
    yt = YouTube(url)
    videos = yt.streams.all()
    video = list(enumerate(videos))
    for i in video:
        print()


    print("Выбираем формат:(Если не предложил формат по умолчанию нажимаем 1) ")
    download_format = int(input("Выбираем номер: "))
    user = input("Пишем пользователя: ")
    videos[download_format].download(output_path=f'/Users/{user}/Desktop', filename='yt_video.mp4')
    print("Загрузка завершена")

if __name__ == "__main__":
    print("Вводим URL видео: ")
    url = input()
    download_video(url)
