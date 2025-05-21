from pygame import *

window = display.set_mode((700,500))

background = transform.scale(image.load('ICantBreathe.jpg'),(700,500))

class GameSprite(sprite.Sprite):
    def __init__(self, image33, speed, x, y):
        super().__init__()
        self.image = transform.scale(image.load(image33),(75,175))
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

hero = Player2('alla.png', 3, 1, 1)
Hero = Player('jew.jpg', 3, 624, 1)


game = True
finish = False

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
            
            

    display.update()
