from main import *
from controller import *

class FallspikeController(PersonController):
     def __init__(self,args):
          PersonController.__init__(self,args)
          self.step=-1
          self.alpha=0
          self.object.maxVelY=self.object.data["maxVel"]
          self.object.accelY=self.object.data["accel"]
          
     def Update(self,args):
          if self.object.fall == False:
               if (self.room.player.posX+self.room.player.width >= self.object.posX and self.room.player.posX <= self.object.posX+self.object.width) \
               and self.room.player.posY > self.object.posY:
                    self.object.fall=True
          
          if self.step == 0:
               self.alpha=int(math.ceil(255.0/float(self.object.data["life"])))
               self.step+=1
               
          elif self.step > 0 and self.object.data["life"] > 0:
               self.object.sprite.SetAlpha(self.object.sprite.alpha-self.alpha)
               self.step+=1
               #completely invisible now
               if self.step >= self.object.data["life"]:
                    self.object.remove=True
                    self.room.RemoveController(self.id)
          
     def OnObjectCollision(self,message):
          if message.obj2.name == "player":
               ctrl=self.room.GetControllerByObj(message.obj2)
               if self.object.data["damage"] < 0:
                    ctrl.Hit(message.obj2.data["HP"])
               else:
                    ctrl.Hit(self.object.data["damage"])
                    
     def OnObjectLand(self,message):
          self.step=0
               

Controller=FallspikeController