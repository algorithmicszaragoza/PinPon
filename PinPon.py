from pygame import *

window = display.set_mode((700,500))

background = transform.scale(image.load('ICantBreathe.jpg'),(700,500))

game = True
finish = False

while game:


    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background,(0,0))
            
            

    display.update()