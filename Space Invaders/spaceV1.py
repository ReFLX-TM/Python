import pygame
import random
import sqlite3

pygame.init()

# Database Setup

con = sqlite3.connect('highscores.db')

cursorObj = con.cursor()

# Window Setup

win = pygame.display.set_mode((750, 750))
pygame.display.set_caption('Space Invaders')
user_name = ""

# Background Image

bg = pygame.image.load('bgImg.png')

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)


class Ship(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('shipImg.png')
        self.rect = self.image.get_rect()
        self.lives = 5
        self.score = 0
        self.level = 3

    def draw(self):

        win.blit(self.image, (self.rect.x, self.rect.y))


class Enemy(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('enemyImg.png')
        self.rect = self.image.get_rect()
        self.group_rect = pygame.Rect(130, 75, 500, 250)
        self.direction = ship.level * 2
        self.lives = ship.level

    def update(self):

        self.rect.x += self.direction
        self.group_rect.x += self.direction

        if self.group_rect.x + 500 >= 725:

            self.direction = -self.direction

        if self.group_rect.x <= 25:

            self.direction = -self.direction
            self.rect.y += 5

class Bunker(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('bunkerImg.png')
        self.rect = self.image.get_rect()

class Missile(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('projectileImg.png')
        self.rect = self.image.get_rect()

    def update(self):

        self.rect.y += -10

class Bomb(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('bombImg.png')
        self.rect = self.image.get_rect()

    def update(self):

        self.rect.y += 10

# Create Ship

ship = Ship()
ship.rect.x = 375
ship.rect.y = 650

# Sprite Groups

enemy_list = pygame.sprite.Group()
bunker_list = pygame.sprite.Group()
missile_list = pygame.sprite.Group()
bomb_list = pygame.sprite.Group()

# Create Enemies

def make_enemies():

    for row in range(1, 6):
        for column in range(1, 11):
            enemy = Enemy()
            enemy.rect.x = 80 + (50 * column)
            enemy.rect.y = 25 + (50 * row)
            enemy_list.add(enemy)

make_enemies()

# Create Bunkers

def make_bunkers():

    for bunk in range(3):
        for row in range(5):
            for column in range(10):
                bunker = Bunker()
                bunker.rect.x = (50 + (275 * bunk)) + (10 * column)
                bunker.rect.y = 500 + (10 * row)
                bunker_list.add(bunker)

make_bunkers()


def redraw():
    win.blit(bg, (0,0))

    if playing:
        bottom = pygame.draw.rect(win, green, (50, 700, 650, 5))       

        # Ship Lives

        for i in range(ship.lives):
            pygame.draw.rect(win, red, (50 + (i * 130), 715, 130, 15))

        # Game Title

        font = pygame.font.SysFont('Courier New', 30)
        text = font.render('Space Invaders', False, white)
        textRect = text.get_rect()
        textRect.center = (750//2 , 25)
        win.blit(text, textRect)     

        # Level

        text = font.render('Level: ' + str(ship.level), False, white)
        textRect = text.get_rect()
        textRect.center = (100 , 25)
        win.blit(text, textRect)    

        #Score

        text = font.render('Score: ' + str(ship.score), False, white)
        textRect = text.get_rect()
        textRect.center = (650 , 25)
        win.blit(text, textRect)

        # Draw Objects

        ship.draw()
        enemy_list.update()
        enemy_list.draw(win)
        bunker_list.draw(win)
        missile_list.update()
        missile_list.draw(win)
        bomb_list.update()
        bomb_list.draw(win)

    else:
        # Title

        font = pygame.font.SysFont('Courier New', 60)
        text = font.render('Space Invaders', False, green)
        textRect = text.get_rect()
        textRect.center = (750//2 , 50)
        win.blit(text, textRect)      

        # Highscores

        text = font.render('Name:', False, white)
        textRect = text.get_rect()
        textRect.center = (250 , 200)
        win.blit(text, textRect)  

        text = font.render(user_name, False, white)
        textRect = text.get_rect()
        textRect.center = (500 , 200)
        win.blit(text, textRect)

        text = font.render('Highscores', False, green)
        textRect = text.get_rect()
        textRect.center = (370 , 300)
        win.blit(text, textRect)

        cursorObj.execute('SELECT * FROM scores ORDER BY "Score" DESC')
        scores = cursorObj.fetchall()

        counter = 0
        for i in scores:
            text = font.render(str(counter + 1), False, white)
            textRect = text.get_rect()
            textRect.center = (200, 370 + (50 * counter))
            win.blit(text, textRect)
            counter += 1

        counter = 0
        for i in scores:
            if counter < 5:
                text = font.render(i[0], False, white)
                textRect = text.get_rect()
                textRect.center = (325, 370 + (50 * counter))
                win.blit(text, textRect)
                counter += 1
            else: break

        counter = 0
        for i in scores:
            if counter < 5:
                text = font.render(str(i[1]), False, white)
                textRect = text.get_rect()
                textRect.center = (510, 370 + (50 * counter))
                win.blit(text, textRect)
                counter += 1
            else: break
        
        # Start Message

        text = font.render('Press Space to Start', False, green)
        textRect = text.get_rect()
        textRect.center = (750//2 , 700)
        win.blit(text, textRect)

    #Update Display
    pygame.display.update()

run = True
playing = False

while run:

    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if playing:
        # Movement Controls

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:

            ship.rect.x += -10

        if key[pygame.K_RIGHT]:

            ship.rect.x += 10

        if key[pygame.K_SPACE]:

            if len(missile_list) < 10:
                missile = Missile()
                missile.rect.x = ship.rect.x + 25
                missile.rect.y = ship.rect.y
                missile_list.add(missile)

        # Shooting Enemy Bombs

        shoot_chance = random.randint(1, 100)
        bomb_chance = ship.level * 10

        if shoot_chance < bomb_chance:

            if len(enemy_list) > 0:

                random_enemy = random.choice(enemy_list.sprites())
                bomb = Bomb()
                bomb.rect.x = random_enemy.rect.x + 12
                bomb.rect.y = random_enemy.rect.y + 25
                bomb_list.add(bomb)

        # Missile Hits

        for missile in missile_list:

            if missile.rect.y < -10:

                missile_list.remove(missile)               

            for enemy in enemy_list:

                if missile.rect.colliderect(enemy.rect):

                    ship.score += 1
                    missile_list.remove(missile)
                    enemy.lives -= 1

                    if enemy.lives <= 0:

                        enemy_list.remove(enemy)

            for bunker in bunker_list:

                if missile.rect.colliderect(bunker.rect):

                    missile_list.remove(missile)
                    bunker_list.remove(bunker)

        # Bomb Hits

        for bomb in bomb_list:

            if bomb.rect.y > 750:

                bomb_list.remove(bomb)

            if bomb.rect.colliderect(ship.rect):

                bomb_list.remove(bomb)
                ship.lives -= 1

            for bunker in bunker_list:

                if bomb.rect.colliderect(bunker.rect):

                    bomb_list.remove(bomb)
                    bunker_list.remove(bunker)

        if ship.lives < 0:
            
            records = (user_name, ship.score)
            cursorObj.execute('INSERT INTO scores(Name, Score) VALUES(?, ?)', records)
            con.commit()

            playing = False
            
            ship.lives = 5

        if len(enemy_list) == 0: 

            ship.level += 1
            make_enemies()           

    else:

        bomb_list.empty()
        key = pygame.key.get_pressed()        
        if len(user_name) < 3:
            if key[pygame.K_a]:
                user_name += "A"
            if key[pygame.K_b]:
                user_name += "B"
            if key[pygame.K_c]:
                user_name += "C"
            if key[pygame.K_d]:
                user_name += "D"
            if key[pygame.K_e]:
                user_name += "E"
            if key[pygame.K_f]:
                user_name += "F"
            if key[pygame.K_g]:
                user_name += "G"
            if key[pygame.K_h]:
                user_name += "H"
            if key[pygame.K_i]:
                user_name += "I"
            if key[pygame.K_j]:
                user_name += "J"
            if key[pygame.K_k]:
                user_name += "K"
            if key[pygame.K_l]:
                user_name += "L"
            if key[pygame.K_m]:
                user_name += "M"
            if key[pygame.K_n]:
                user_name += "N"
            if key[pygame.K_o]:
                user_name += "O"
            if key[pygame.K_p]:
                user_name += "P"
            if key[pygame.K_q]:
                user_name += "Q"
            if key[pygame.K_r]:
                user_name += "R"
            if key[pygame.K_s]:
                user_name += "S"
            if key[pygame.K_t]:
                user_name += "T"
            if key[pygame.K_u]:
                user_name += "U"
            if key[pygame.K_v]:
                user_name += "V"
            if key[pygame.K_w]:
                user_name += "W"
            if key[pygame.K_x]:
                user_name += "X"
            if key[pygame.K_y]:
                user_name += "Y"            
            if key[pygame.K_z]:
                user_name += "Z"
        if key[pygame.K_BACKSPACE]:
            user_name = user_name[:len(user_name) - 1]

        if key[pygame.K_SPACE]:

            playing = True
            ship.level = 1
            ship.score = 0
            bunker_list.empty()
            make_bunkers()
            enemy_list.empty()
            make_enemies()            

    redraw()

con.close()
pygame.quit()