import pygame
import os

def play_music(input):
    pygame.mixer.init()
    if not(os.path.isfile('./midi/'+input+'.mid')):
        return
    pygame.mixer.music.load('./midi/'+input+'.mid')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.wait(10)
    print('music stop')

def stop_music():
    pygame.mixer.music.pause()
    print('music stop')

music = input("曲名を教えて")
play_music(music)



