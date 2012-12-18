from main import *
from controller import *

class PlatformController(PersonController):
     def __init__(self,args):
          PersonController.__init__(self,args)
          self.room.AddSubscriber(self,INPUT_KEY)
          self.action=-2
          self.index=-1
          self.iter=0
          self.step=0
          self.pos=-1
          if len(self.object.data["walk_list"]) > 0:
               self.index=0
          
     def Update(self,args):
          if self.index >= 0:
               #determine action
               if self.action == -2:
                    cmd=self.object.data["walk_list"][ self.index ]
                    csplit=cmd.split(":")
                         
                    if csplit[0] == "wait":
                         self.action=-1
                         self.step=int(csplit[1])
                         self.object.sprite.Pause()
                    elif csplit[0] == "to-x":
                         self.pos=int(csplit[1])
                         self.step=-2
                         if self.object.posX < self.pos:
                              self.action=RIGHT
                         elif self.object.posX > self.pos:
                              self.action=LEFT
                         else:
                              self.action=-1
                              self.step=1
                    elif csplit[0] == "to-y":
                         self.pos=int(csplit[1])
                         self.step=-2
                         if self.object.posY < self.pos:
                              self.action=DOWN
                         elif self.object.posY > self.pos:
                              self.action=UP
                         else:
                              self.action=-1
                              self.step=1
                              
               #move accordingly
               if self.action >= 0:
                    self.object.GenerateAction(self.action)
                    
               #update
               self.iter+=1
               change=False
               if self.step != -2 and self.iter >= self.step:
                    change=True
                         
               else:
                    if self.action == LEFT and self.object.posX <= self.pos:
                         change=True
                    elif self.action == RIGHT and self.object.posX >= self.pos:
                         change=True
                    elif self.action == UP and self.object.posY <= self.pos:
                         change=True
                    elif self.action == DOWN and self.object.posY >= self.pos:
                         change=True
               
               if change:
                    self.index+=1
                    self.action=-2
                    self.pos=-1
                    self.step=0
                    self.iter=0
                    self.object.velX=0.0
                    self.object.velY=0.0
                    if self.index >= len(self.object.data["walk_list"]):
                         self.index=0
          """
          if self.room.key[K_w] and self.room.key[K_a]:
               self.object.GenerateAction(UP_LEFT)
          elif self.room.key[K_w] and self.room.key[K_d]:
               self.object.GenerateAction(UP_RIGHT)
          elif self.room.key[K_s] and self.room.key[K_a]:
               self.object.GenerateAction(DOWN_LEFT)
          elif self.room.key[K_s] and self.room.key[K_d]:
               self.object.GenerateAction(DOWN_RIGHT)
          elif self.room.key[K_a]:
               self.object.GenerateAction(LEFT)
          elif self.room.key[K_d]:
               self.object.GenerateAction(RIGHT)
          elif self.room.key[K_w]:
               self.object.GenerateAction(UP)
          elif self.room.key[K_s]:
               self.object.GenerateAction(DOWN)
          """
          
     def OnObjectCollision(self,message):
          pass
               

Controller=PlatformController