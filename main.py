from pytube import YouTube
import time

input_file = open('./input.txt', 'r') # open the file
text = input_file.read()
url_list = text.split('\n')

counter = 0 # Tracks which video is being downloaded.

print('\n')
print('------------------------------------------')
print("AUM'S YOUTUBE VIDEO DOWNLOADER")
print('------------------------------------------')
print(f'{len(url_list)} videos detected.')
print('Proceeding to download...')
print('------------------------------------------')
time.sleep(5)

try:

    for url in url_list:
        counter = counter + 1
        yt = YouTube(url)
        print(f'Video {counter}: ' + f'{yt.title[:29]}...')
        yt.streams.get_highest_resolution().download(output_path='./output/')
        print(f'Download successful.')

    input_file.close()
    
    print('------------------------------------------')
    print('All downloads are complete.')

except:
    print('------------------------------------------')
    print('Something unexpected happened.')

print('This python app will automatically close in 60 seconds.')
time.sleep(1000)