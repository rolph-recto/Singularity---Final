from main import *
from controller import *

class CannonballController(PersonController):
     def __init__(self,args):
          PersonController.__init__(self,args)
          
     def Update(self,args):
          self.room.particle.AddParticle("circle5",self.object.posX+(self.object.width/2),self.object.posY+(self.object.height/2),0,0,3.0,-0.01)
          self.object.data["currentLife"]=self.object.data["currentLife"]+1
          if self.object.data["life"] >= 0:
               self.object.sprite.SetAlpha( 255-int( float(255)*(float(self.object.data["currentLife"])/float(self.object.data["life"])) ) )
               if self.object.data["currentLife"] >= self.object.data["life"]:
                    self.object.remove=True
                    self.room.RemoveController(self.id)
          
     def OnObjectLand(self,message):
          if self.object.data["life"] <= 0:
               self.object.remove=True
               self.room.RemoveController(self.id)
               
     def OnObjectCollision(self,message):
          if message.collision_type != COLLISION_WALL:
               if message.obj2.name == "player":
                    ctrl=self.room.GetControllerByObj(message.obj2)
                    ctrl.Hit(1)
          elif self.object.data["life"]<0:
               self.object.remove=True
               self.room.RemoveController(self.id)

Controller=CannonballController