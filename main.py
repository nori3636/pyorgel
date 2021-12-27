import pygame
import os

def play_music(music_name):
    pygame.mixer.init()
    if not(os.path.isfile('./midi/'+music_name+'.mid')):
        return
    pygame.mixer.music.load('./midi/'+music_name+'.mid')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.wait(10)
    print('music stop')

def all_music():
    pygame.mixer.init()
    musics = os.listdir('./music_midi')
    for midi_file in musics:
        pygame.mixer.music.load('./midi/'+midi_file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.wait(10)
    print('music stop')

def stop_music():
    pygame.mixer.music.pause()
    print('music stop')


music = input("なんの曲を流しますか")
if music == 'all':
    all_music()
else:
    play_music(music)



