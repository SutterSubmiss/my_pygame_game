import pygame
from random import randint
from pygame.locals import *

resolution = (1000,600)
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
gameDisplay = pygame.display.set_mode((500,500))
screen = pygame.display.set_mode(resolution)

class Block(pygame.sprite.Sprite):
    img = 'altm'
    x_beginning = 0
    y_beginning = 300
    scale = (50,50)
    def create_image(self, number):
        return self.img + ".png"
    def disp(self):

        block_surface = pygame.image.load(self.create_image("1"))
        self.image = block_surface
        gameDisplay.blit(pygame.transform.scale(self.image, self.scale), (self.x_beginning, self.y_beginning))
Blocks = pygame.sprite.Group
floor = Block()
block2 = Block()
block2.y_beginning -= block2.scale[1]
block2.x_beginning = 200
floor.scale = (1000,50)
blocks = []
blocks.append(floor)
blocks.append(block2)

class Character(pygame.sprite.Sprite):
 boris_audzia_far = 0
 old_baf = 0
 type = 'audzia'
 flipped= False
 def create_image(self,number):
    return self.type + "/" + self.type + number + ".png"
 images =[]
 blocked = [False,False,False,False]
 def same_axis(self,something,axis):
     if(axis == 'x'):
         beginning = something.x_beginning
         if(self.x_beginning+self.scale[0]-15>=beginning and self.x_beginning+15<=beginning +something.scale[0]):

             return True
         else:
             return False
     elif(axis == 'y'):
         beginning = something.y_beginning
         if (self.y_beginning + self.scale[1] >beginning  and  self.y_beginning< beginning + something.scale[1]):
             return True
         else:
             return False
 def collision(self):
  for block in blocks:
     if(self.same_axis(block,'x')):
      if(self.y_beginning+self.scale[1] >= block.y_beginning and block.y_beginning >self.y_beginning):
         self.blocked[3] = True
      else:
         self.blocked[3] = False
      if (self.y_beginning  <= block.y_beginning+ block.scale[1] and block.y_beginning < self.y_beginning):
          self.blocked[2] = True

     if (self.same_axis(block, 'y')):
         if (self.x_beginning + self.scale[0] >= block.x_beginning and block.x_beginning >self.x_beginning or self.x_beginning >1000-self.scale[0]):
             self.blocked[0] = True

         if (self.x_beginning <= block.x_beginning+block.scale[0] and block.x_beginning <self.x_beginning or self.x_beginning <1):
             self.blocked[1] = True


 scale = (50, 100)
 x_beginning = 0
 y_beginning = 300-scale[1]
 moves = [1, 1, 1, 1, 2, 3, 4]
 moves2 = [1, 2, 2, 2, 2, 3, 4]
 audzia_side = False
 clicked = []
 def disp(self,number):
     character_surface = pygame.transform.flip(pygame.image.load(self.create_image(number)),self.flipped,False)
     self.image = character_surface
     gameDisplay.blit(pygame.transform.scale(self.image,self.scale),(self.x_beginning,self.y_beginning))

 def go_right(self):
         self.flipped = False

         character_surface = pygame.image.load(self.create_image("2"))
         self.image = character_surface
         if (self.blocked[0] == False):
             self.x_beginning += 25
             return "2"
         else:
             return "1"

 def go_left(self):
         self.flipped = True

         character_surface = pygame.image.load(self.create_image("2"))
         self.image = character_surface
         if (self.blocked[1] == False):
             self.x_beginning -= 25
             return "2"
         else:
            return "1"
 def go_up(self):
     character_surface = pygame.image.load(self.create_image("3"))
     self.image = character_surface
     if (self.blocked[2] == False and not pygame.key.get_pressed()[pygame.K_DOWN] ):
       self.y_beginning -= 100
       return "3"
     else:
         return "1"

 def go_down(self):
     character_surface = pygame.image.load(self.create_image("3"))
     self.image = character_surface
     if (self.blocked[3] == False and not pygame.key.get_pressed()[pygame.K_UP] ):
        self.y_beginning += 50
     return "3"


 def gravity(self):
   if(self.blocked[3] == False):
       self.y_beginning += 50

 def walk(self):
     keys = pygame.key.get_pressed()
     self.hop = True
     ret = "1"
     if (self.type == "audzia"):

         self.hop = True

         if (keys[pygame.K_RIGHT]):
             ret = self.go_right()
             self.blocked[0] = True


         else:
             self.blocked[0] = False

         if (keys[pygame.K_UP]):
             ret =self.go_up()
             self.blocked[2] = True

         else:
             self.blocked[2] = False
             if (keys[pygame.K_DOWN]):
               ret =self.go_down()

         if (keys[pygame.K_LEFT]):
             ret = self.go_left()
             self.blocked[1] = True

         else:
             self.blocked[1] = False
         return ret

     elif (self.type == "boris"):
         if (self.audzia_side == False):
             rand = self.moves[randint(0, len(self.moves) - 1)]
             self.moves.append(rand)
         else:
             rand = self.moves2[randint(0, len(self.moves2) - 1)]
             self.moves2.append(rand)
         self.old_baf = self.boris_audzia_far
         if (audzia.x_beginning < self.x_beginning):
             self.audzia_side = True
         else:
             self.audzia_side = False
         if ((audzia.x_beginning >= 0 and self.x_beginning >= 0) or (
                 audzia.x_beginning <= 0 and self.x_beginning <= 0)):
             self.boris_audzia_far = abs(abs(audzia.x_beginning) - abs(self.x_beginning))
         else:
             boris.boris_audzia_far = abs(audzia.x_beginning) + abs(self.x_beginning)
         if (old_baf > self.boris_audzia_far):
             if (self.audzia_side == False):
                 self.moves.append(self.walk())

             else:
                 self.moves2.append(self.walk())
         if (rand == 1):
             return self.go_right()
         elif (rand == 2):
             return self.go_left()
         elif (rand == 3):
             return  self.go_up()
         elif(self.blocked[3] == True):
             return  self.go_down()
         else:
            return self.walk()
 def whiletrue(self):
        self.collision()
        self.gravity()
        self.disp(self.walk())
        pygame.time.wait(10)
audzia = Character()
boris = Character()
boris.type = "boris"
old_baf = 0
while True:
    floor.disp()
    audzia.whiletrue()
    boris.whiletrue()
    block2.disp()
    #pygame.time.wait(100)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    screen.fill(white)
