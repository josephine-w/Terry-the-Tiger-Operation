import pygame
from time import sleep
from sys import exit
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (150,0,150)
GREEN = (0,255,0)
BLUE = (0,0,255)

pi = 3.141592

pygame.init()
 
# Set the width and height of the screen [width, height]
size = (750, 750)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Terry the Tiger's Operation")

class Tweezers(pygame.sprite.Sprite):    

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./Images/tweezers.png").convert_alpha()
        self.rect = self.image.get_rect()

    
class Item(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./Images/.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        

    def reset_pos(self):
        self.rect.x = 1500
        self.rect.y = 1500

        
class Heart(Item):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./Images/heart.png").convert_alpha()

       
class Bone(Item):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./Images/bone.png").convert_alpha()


class Liver(Item):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./Images/liver.png").convert_alpha()
        

class Hairball(Item):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./Images/hairball.png").convert_alpha()
        

class Football(Item):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./Images/football.png").convert_alpha()


class Booger(Item):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./Images/booger.png").convert_alpha()


bg = pygame.image.load("./Images/background.png").convert()


all_sprites_list = pygame.sprite.Group()
cavity_list = pygame.sprite.Group()

# Draw bad heart
heart = Heart()
heart.rect.x = 411
heart.rect.y = 334

cavity_list.add(heart)
all_sprites_list.add(heart)

# Draw bones
bone = Bone()
bone.rect.x= 420
bone.rect.y= 594

bone2 = Bone()
bone2.rect.x = 169
bone2.rect.y = 327


cavity_list.add(bone)
cavity_list.add(bone2)
all_sprites_list.add(bone)
all_sprites_list.add(bone2)

# Draw liver
liver = Liver()
liver.rect.x= 291
liver.rect.y= 487

cavity_list.add(liver)
all_sprites_list.add(liver)

# Draw hairball
hairball = Hairball()
hairball.rect.x= 282
hairball.rect.y= 647

cavity_list.add(hairball)
all_sprites_list.add(hairball)

# Draw football
football = Football()
football.rect.x= 439
football.rect.y= 49
cavity_list.add(football)
all_sprites_list.add(football)

# Draw booger
booger = Booger()
booger.rect.x = 344
booger.rect.y = 196

cavity_list.add(booger)
all_sprites_list.add(booger)

#Create the plyer instance from tweezer class
player = Tweezers()

all_sprites_list.add(player)

#For main
done = False

item = 0


clock = pygame.time.Clock()

pygame.mouse.set_visible(False)

#List of organs that have reached desired point and disappeared
disappear_list=[]

# set variables for timer
font = pygame.font.Font(None, 25)
frame_count = 0
frame_rate = 60
start_time = 10

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Drawing
    screen.fill(WHITE)

    #Blit background picture
    screen.blit(bg,(0,0))

    # --- Game logic

    #Set tweezer to follow mouse pos
    pos = pygame.mouse.get_pos()
    player.rect.x = pos[0]
    player.rect.y = pos[1]

    if item == 0:
        blocks_hit_list = pygame.sprite.spritecollide(player, cavity_list, False)
        
    #check if mouse collided with an organ/material
    #if there is a collision the sprite becomes mouse pos
    for cavity in blocks_hit_list:
        cavity.rect.x = player.rect.x
        cavity.rect.y = player.rect.y
        item = 1

        #Make organ/material disappear if in trash bucket
        if (cavity.rect.x in range(582,713)) and (cavity.rect.y in range(550,705)):
            cavity.reset_pos()
            disappear_list.append(cavity)
            item = 0
            

    #Draw all sprites
    all_sprites_list.draw(screen)

    # Countdown timer  
    total_seconds= start_time - (frame_count// frame_rate)
    if (len(disappear_list)==7) and (total_seconds>0):

        #Stop counting
        total_seconds = 0
        #Display if player won
        pygame.draw.rect(screen,BLUE,[200,200,400,100])
        
        # Select the font to use, size, bold, italics
        font = pygame.font.SysFont('Calibri', 20, True, False)

        # Render the text
        text = font.render("Congratulations! You saved Terry's life! :)",True,GREEN)

        # Put the image of the text on the screen at 220x220
        screen.blit(text, [220, 220])


    #check if player lost
    elif (total_seconds<=0):
        
        #limit timer so that it doesnt go into negatives
        total_seconds=00

        if (len(disappear_list)!=7):
          
            #Display if player lost
            pygame.draw.rect(screen,BLACK,[150,200,500,70])
            # Select the font to use, size, bold, italics
            font = pygame.font.SysFont('Calibri', 20, True, False)

            #Display text
            text = font.render("You did not remove all material from Terry. He is dead. :(",True,RED)

            # Put the image of the text on the screen at 170x220
            screen.blit(text, [170, 220])

        elif (total_seconds==-5) and (len(disappear_list)==5):
            pygame.quit()
            
        else:
            pygame.quit()
            

    #Use python string formatting to format counter
    output_string = "Time:{0:02}".format(total_seconds)

    #Blit to screen
    text = font.render(output_string,True,BLACK)
    screen.blit(text,[100,100])

    frame_count+=1

     
    #display images
    pygame.display.flip()

    #limit to 60FPS
    clock.tick(60)
    # Display Images
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
