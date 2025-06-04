from pygame import *

window = display.set_mode((700,500))

background = transform.scale(image.load('ICantBreathe.jpg'),(700,500))

mixer.init()

mixer.music.load('galaxy-meme.ogg')

mixer.music.play(loops = -1)

speed_x = 3
speed_y = 3

class GameSprite(sprite.Sprite):
    def __init__(self, image33, speed, x, y, size_x=75, size_y=175):
        super().__init__()
        self.image = transform.scale(image.load(image33),(size_x, size_y))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))


class Player(GameSprite):

    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y <= 325:
            self.rect.y += self.speed 

class Player2(GameSprite):

    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y <= 325:
            self.rect.y += self.speed 

class Ball(GameSprite):

    def update(self):
       
        self.rect.x += speed_x 
        self.rect.y += speed_y


hero = Player2('alla.png', 3, 1, 1)
Hero = Player('jew.jpg', 3, 624, 1)
Bola = Ball('pngegg.png', 678, 320, 210, 60, 60)


game = True
finish = False

clock = time.Clock()
while game:


    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background,(0,0))
        hero.update()
        hero.reset() 
        Hero.update()
        Hero.reset()
        Bola.update()
        Bola.reset()
    clock.tick(60)
    if Bola.rect.y <= 0 or Bola.rect.y >= 440:
        speed_y *= -1
    if Bola.rect.x <= 0 or Bola.rect.x >= 660:
        speed_x *= -1
            
            

    display.update()
