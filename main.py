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
objects = []


def display(self):
    a = pygame.transform.scale(pygame.image.load(self.image), self.scale)
    gameDisplay.blit(a, (self.x_beginning, self.y_beginning))

class Cart:
    image  ="begining.png"
    scale = (200,200)
    x_beginning = 500
    y_beginning = 100
    def display(self):
       display(self)


class Object:
    scale = (50,50)
    image = "altm.png"
    x_beginning = 0
    y_beginning = 375
    def display(self):
        display(self)

class Character:
 x_beginning = 10

 scale = (150,150)
 y_beginning = 275
 flipped = False
 type = "audzia"
 hop = False
 clicked = []
 blocked = False
 pyg = []
 me = pygame.Rect(x_beginning-scale[0],y_beginning-scale[1],scale[0]+1,scale[1]+1)
 def collision(self):
  for i in objects:
     ob = pygame.Rect(i.x_beginning-i.scale[0],i.y_beginning-i.scale[1],i.scale[0]+1,i.scale[1]+1)

     if(ob.colliderect(self.me)):
        self.blocked = True

 moves = [1,1,1,1,2,3,4]
 moves2 = [1,2,2,2,2,3,4]

 def gravity(self):
      objects_y_beginnings = []

      for i in objects:
          if(self.x_beginning >= i.x_beginning-i.scale[0] and self.x_beginning <= i.x_beginning):
           objects_y_beginnings.append([i.y_beginning,i.scale[1]])
      if(objects_y_beginnings !=  []):
       while(min(objects_y_beginnings)[0]-min(objects_y_beginnings)[1] > self.y_beginning+self.scale[1]):
             self.y_beginning +=10





 image = type+"/"+type+"1.png"

 audzia_side = False


 def character(self):
   y_corpse_place = self.y_beginning-75
   a = pygame.image.load(self.image)
   if (self.flipped == True and self.clicked.__contains__("r")):
       self.flipped = False
   elif (self.flipped == False and self.clicked.__contains__("l")):
       self.flipped = True
   a = pygame.transform.flip(a, self.flipped, False)
   a2 = pygame.transform.scale(a, self.scale)
   self.pyg.append(gameDisplay.blit(a2,(self.x_beginning-15,self.y_beginning)))


 def go_right(self):

     if(self.x_beginning <1000):
      self.image  = self.type+"/"+self.type+"2.png"
      if(self.blocked == False):
        self.x_beginning += 25
      self.clicked.append("r")
 def go_left(self):

     if (self.x_beginning > 10):
      self.image  = self.type+"/"+self.type+"2.png"
      if (self.blocked == False):
          self.x_beginning -= 25
      self.clicked.append("l")
 def go_up(self):
     self.image  = self.type+"/"+self.type+"3.png"
     self.y_beginning -=25

     self.clicked.append("u")
 def go_down(self):
     self.image  = self.type+"/"+self.type+"3.png"
     self.y_beginning += 25
     self.clicked.append("d")

 def walk(self):
  self.hop = True

  if(self.type == "audzia"):
    keys = pygame.key.get_pressed()
    self.hop = True
    if(keys[pygame.K_RIGHT]):
          self.go_right()

    if(keys[pygame.K_UP]):
        self.go_up()

    if(keys[pygame.K_DOWN]):
        self.go_down()

    if (keys[pygame.K_LEFT]):
        self.go_left()
  elif(self.type == "boris"):
     if(self.audzia_side == False):
        rand = self.moves[randint(0,len(self.moves)-1)]
     else:
         rand = self.moves2[randint(0, len(self.moves2) - 1)]
     if(rand == 1):
         self.go_right()
     elif(rand== 2):
         self.go_left()
     elif(rand == 3):
         self.go_up()
     else:
         self.go_down()
     return rand
 def whiletrue(self):
    if(self.hop == True):

      if(self.clicked.__contains__("r")):
          self.image  = self.type+"/"+self.type+"1.png"
      if (self.clicked.__contains__("l")):
          self.image  = self.type+"/"+self.type+"1.png"
      if (self.clicked.__contains__("u")):
          self.image  = self.type+"/"+self.type+"1.png"
          self.gravity()
      if (self.clicked.__contains__("d")):
          self.y_beginning -= 25
          self.image  = self.type+"/"+self.type+"1.png"
      self.clicked = []
      self.hop = False
    self.walk()
    self.character()
    self.gravity()
    self.blocked = False

i = 0
screen.fill(white)
floor = Object()
floor.scale = (1000, 50)
carts = []
second_object = Object()
second_object.x_beginning = 500
second_object.y_beginning = 325
objects.append(second_object)
objects.append(floor)
floor.display()
second_object.display()
audzia = Character()
boris = Character()
boris.type = "boris"
audzia.x_beginning =  300
old_baf = 0
beginning_cart = Cart()
carts.append(beginning_cart)
beginning_cart.display()
while True:
 #if(carts == []):
    audzia.collision()
    boris.collision()
    audzia.whiletrue()
    boris.whiletrue()

    second_object = Object()
    floor.scale = (1000, 50)
    second_object.y_beginning = 325
    second_object.x_beginning = 500
    floor.display()
    second_object.display()


    pygame.display.flip()
    if (audzia.x_beginning < boris.x_beginning):
        boris.audzia_side = True
    else:
        boris.audzia_side = False
    if((audzia.x_beginning >=0 and boris.x_beginning >= 0) or (audzia.x_beginning <= 0 and boris.x_beginning <= 0)):
     boris_audzia_far = abs(abs(audzia.x_beginning) - abs(boris.x_beginning))
    else:
        boris_audzia_far = abs(audzia.x_beginning) + abs(boris.x_beginning)
    if(old_baf > boris_audzia_far):
        if(boris.audzia_side == False):
            boris.moves.append(boris.walk())

        else:
            boris.moves2.append(boris.walk())

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    i = 1

    screen.fill(white)
    old_baf = boris_audzia_far
 #elif(pygame.mouse.get_pos()[0] > beginning_cart.x_beginning and pygame.mouse.get_pos()[0] < beginning_cart.x_beginning+beginning_cart.scale[0] and pygame.mouse.get_pos()[1] > beginning_cart.y_beginning and pygame.mouse.get_pos()[1] < beginning_cart.y_beginning+beginning_cart.scale[1]):
     #carts = []