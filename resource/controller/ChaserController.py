from main import *
from controller import *

class ChaserController(PersonController):
     def __init__(self,args):
          PersonController.__init__(self,args)
          
          self.object.sprite.SetAnimation(self.object.data["direction"])
          self.object.sprite.Pause()
          
          self.xpos=self.object.posX
          self.origDirection=self.object.data["direction"]
          self.phase=0
          self.idle=0
          self.sense=False
          self.object.origX=self.object.posX
          self.object.origY=self.object.posY
     
     def Update(self,args):
          #idle mode - sense player
          self.idle+=1
          if self.phase==0 and self.idle>30:
               
               self.sense=False
               player=self.room.GetObjectByName("player")
          
               if (player.posY >= self.object.posY and player.posY <= self.object.posY+self.object.width) \
               or (player.posY+player.width >= self.object.posY and player.posY+player.width <= self.object.posY+self.object.width):
                    x_distance=-1
                    if self.object.data["direction"] == 1:
                         x_distance=player.posX-(self.object.posX+self.object.width)
                    else:
                         x_distance=self.object.posX-(player.posX+player.width)
                         
                    if x_distance < self.object.data["distance"] and x_distance > -1:
                         self.sense=True
                         self.object.sprite.Resume()
                         
               if self.sense:
                    self.phase=1
                    self.idle=0
                    self.room.PlaySound("sound44", self.object.posX, self.object.posY)
                    
          #chase mode
          if self.phase==1:
               #move left
               if self.origDirection == 0:
                    self.object.GenerateAction(LEFT)
               else:
                    self.object.GenerateAction(RIGHT)
                    
               self.room.particle.AddParticle("diamond2",self.object.posX+(self.object.width/2),self.object.posY+(self.object.height/2),0,0,3.0,0.0)
                    
          #retreat mode
          elif self.phase==2:
               home=False
               if self.object.data["direction"]==0:
                    self.object.GenerateAction(LEFT)
                    if self.object.posX <= self.xpos:
                         home=True
               else:
                    self.object.GenerateAction(RIGHT)
                    if self.object.posX >= self.xpos:
                         home=True
                         
               self.room.particle.AddParticle("diamond2",self.object.posX+(self.object.width/2),self.object.posY+(self.object.height/2),0,0,3.0,0.0)
                    
               #if back to original position, return to idle mode
               if home:
                    self.phase=0
                    self.object.data["direction"]=self.origDirection
                    self.object.sprite.SetAnimation(self.origDirection)
                    self.sense=False
                    self.object.sprite.Resume()
                    self.object.sprite.Pause()
                    
                         
     def OnObjectCollision(self,message):
          retreat=False
          if message.collision_type != COLLISION_WALL:
               if message.obj2.name == "player":
                    ctrl=self.room.GetControllerByObj(message.obj2)
                    ctrl.Hit(1)
                    if self.phase==1: retreat=True
               elif message.collision_type != COLLISION_PASS and self.phase==1:
                    retreat=True
          elif message.collision_type == COLLISION_WALL:
               #if hit wall in chase mode, retreat
               if self.phase==1:
                    retreat=True
          
          if retreat:
               self.phase=2
               if self.origDirection==0:
                    self.object.data["direction"]=1
                    self.object.sprite.SetAnimation(1)
               else:
                    self.object.data["direction"]=0
                    self.object.sprite.SetAnimation(0)
               

Controller=ChaserController