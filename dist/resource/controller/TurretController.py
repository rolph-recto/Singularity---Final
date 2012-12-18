from main import *
from controller import *

class TurretController(PersonController):
     def __init__(self,args):
          PersonController.__init__(self,args)
          #0 = RIGHT, 1= LEFT
          self.object.sprite.SetAnimation(self.object.data["direction"])
          self.sense=False
          self.step=0
          self.life=3
          
     def Update(self,args):
          #determine if player is sensed
          self.sense=False
          player=self.room.player
          
          if (player.posY >= self.object.posY and player.posY <= self.object.posY+self.object.width) \
          or (player.posY+player.width >= self.object.posY and player.posY+player.width <= self.object.posY+self.object.width):
               x_distance=-1
               if self.object.data["direction"] == 0:
                    x_distance=player.posX-(self.object.posX+self.object.width)
               else:
                    x_distance=self.object.posX-(player.posX+player.width)
                         
               if x_distance < self.object.data["distance"] and x_distance > -1:
                    self.sense=True
          
          #prepare to fire
          self.step+=1
          if self.sense:
               if self.step >= self.object.data["interval"]:
                    self.step=0
                    if self.object.data["direction"] == 0:
                         objID=self.room.AddObject("bullet",self.object.posX+self.object.width+5,self.object.posY+5)
                         obj=self.room.GetObjectById(objID)
                         obj.velY=0.0
                         obj.velX=obj.type.maxVelX
                         obj.accelX=obj.type.accelX
                    else:
                         objID=self.room.AddObject("bullet",self.object.posX-5,self.object.posY+5)
                         obj=self.room.GetObjectById(objID)
                         obj.velY=0.0
                         obj.velX=-obj.type.maxVelX
                         obj.accelX=-obj.type.accelX
                         
                    self.room.PlaySound("laser", self.object.posX, self.object.posY)
                    
                    
          
          
Controller=TurretController