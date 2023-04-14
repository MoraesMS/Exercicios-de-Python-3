import pygame
#Music by Slip.stream - Alexander Nakarada "Lullaby" - https://slip.stream/tracks/e6bf20bd-2aa6-4dae-88c9-7663e573cc32
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('021_tocando_mp3.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()
