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




def disp(self,img):
        character_surface = pygame.transform.flip(pygame.image.load(img), self.flipped, False)
        gameDisplay.blit(pygame.transform.scale(character_surface, self.scale), (self.beginning[0], self.beginning[1]))
def point_same_axis(self, point,axis):
    if (axis == 'x'):

        if (self.beginning[0] + self.scale[0] - 15 >= point[0] and self.beginning[0] + 15 <= point[0]):

            return True
        else:
            return False
    elif (axis == 'y'):

        if (self.beginning[1] + self.scale[1] > point[1] and self.beginning[1] < point[1]):
            return True
        else:
            return False
def same_axis(self,something, axis):
        if (axis == 'x'):
            beginning = something[0]
            if (self.beginning[0] + self.scale[0] - 15 >= beginning and self.beginning[0] + 15 <= beginning + something.scale[0]):

                return True
            else:
                return False
        elif (axis == 'y'):
            beginning = something[1]
            if (self.beginning[1] + self.scale[1] > beginning and self.beginning[1] < beginning + something.scale[1]):
                return True
            else:
                return False
class Block():


    flipped = False
    image = 'altm.png'
    beginning = [0,300]
    scale = (50,50)
    def create_image(self):
        return self.image + ".png"


floor = Block()
block2 = Block()
block2.beginning[1] -= block2.scale[1]
block2.beginning[0] = 300
floor.scale = (1000,50)
blocks = []
blocks.append(floor)
blocks.append(block2)
class Cart():
    image  ='begining.png'
    scale = (200,200)
    beginning = [400,200]
    flipped = False

class Character():
 boris_audzia_far = 0
 old_baf = 0
 type = 'audzia'
 flipped= False
 def create_image(self,number):
    return self.type + "/" + self.type + number + ".png"
 if not(pygame.key.get_pressed()[pygame.K_UP]):
  blocked = [False,False,False,False]
 image = type + "/" + type + "1.png"
 scale = (50, 100)
 beginning = [0,300-scale[1]]
 def collision(self):
  if(self.beginning[0] < 0):
      self.blocked[1] =  True
  else:
   for block in blocks:
     if(same_axis(self,block.beginning,'x')):
      if(self.beginning[1]+self.scale[1] >= block.beginning[1] and block.beginning[1] >self.beginning[1]):
         self.blocked[3] = True
      else:
         self.blocked[3] = False
      if (self.beginning[1]  <= block.beginning[1]+ block.scale[1] and block.beginning[1] < self.beginning[1]):
          self.blocked[2] = True

     if (same_axis(self,block.beginning, 'y')):
         if (self.beginning[0] + self.scale[0] >= block.beginning[0] and block.beginning[0] >self.beginning[0] or self.beginning[0] >1000-self.scale[0]):
             self.blocked[0] = True

         if (self.beginning[0] <= block.beginning[0]+block.scale[0] and block.beginning[0] <self.beginning[0] or self.beginning[0] <1):
             self.blocked[1] = True


 moves = [1, 1, 1, 1, 2, 3, 4]
 moves2 = [1, 2, 2, 2, 2, 3, 4]
 audzia_side = False
 clicked = []


 def go_right(self):
         self.flipped = False

         character_surface = pygame.image.load(self.create_image("2"))
         self.image = character_surface
         if (self.blocked[0] == False):
             self.beginning[0] += 25
             return "2"
         else:
             return "1"

 def go_left(self):
         self.flipped = True

         character_surface = pygame.image.load(self.create_image("2"))
         self.image = character_surface
         if (self.blocked[1] == False):
             self.beginning[0] -= 25
             return "2"
         else:
            return "1"
 def go_up(self):
     character_surface = pygame.image.load(self.create_image("3"))
     self.image = character_surface
     if (self.blocked[2] == False and not pygame.key.get_pressed()[pygame.K_DOWN] ):
       self.beginning[1] -= 100
       return "3"
     else:
         return "1"

 def go_down(self):
     character_surface = pygame.image.load(self.create_image("3"))
     self.image = character_surface
     if (self.blocked[3] == False and not pygame.key.get_pressed()[pygame.K_UP] ):
        self.beginning[1] += 50
     return "3"


 def gravity(self):
   if(self.blocked[3] == False):
       self.beginning[1] += 50

 def walk(self):
     keys = pygame.key.get_pressed()
     self.hop = True
     ret = "1"
     if (self.type == "audzia"):

         self.hop = True

         if (keys[pygame.K_RIGHT]):
             ret = self.go_right()
             self.blocked[0] = True


         elif(not keys[pygame.K_UP]):
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

         elif(not keys[pygame.K_UP]):
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
         if (audzia.beginning[0] < self.beginning[0]):
             self.audzia_side = True
         else:
             self.audzia_side = False
         if ((audzia.beginning[0] >= 0 and self.beginning[0] >= 0) or (
                 audzia.beginning[0] <= 0 and self.beginning[0] <= 0)):
             self.boris_audzia_far = abs(abs(audzia.beginning[0]) - abs(self.beginning[0]))
         else:
             boris.boris_audzia_far = abs(audzia.beginning[0]) + abs(self.beginning[0])
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
        disp(self,self.create_image(self.walk()))
        pygame.time.wait(10)
audzia = Character()
boris = Character()
boris.type = "boris"

old_baf = 0
beginning_cart = Cart()
ending_Cart = Cart()
ending_Cart.image ="ending.png"

def disp_white():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    screen.fill(white)
disp_white()
disp(beginning_cart,beginning_cart.image)
while True:
  audzia.beginning[0] = 200
  boris.beginning[0] = 0

  if(point_same_axis(beginning_cart,pygame.mouse.get_pos(),"x") and point_same_axis(beginning_cart,pygame.mouse.get_pos(),"y")):
   while True:
    disp(floor,floor.image)
    audzia.whiletrue()
    boris.whiletrue()
    disp(block2,block2.image)
    pygame.display.flip()
    if(same_axis(boris,audzia.beginning,'x') and same_axis(boris,audzia.beginning,'y')):
        break
    disp_white()

   disp(ending_Cart, ending_Cart.image)


  pygame.display.flip()
