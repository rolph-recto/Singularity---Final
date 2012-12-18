from main import *
from controller import *

class PackageController(PersonController):
     def __init__(self,args):
          PersonController.__init__(self,args)
          self.grav=False
          
     def Update(self,args):
          pass
          
     def OnObjectCollision(self,message):
          if message.collision_type != COLLISION_WALL and self.grav==False:
               if message.obj2.name == "player":
                    ctrl=self.room.GetControllerByObj(message.obj2)
                    ctrl.Score(1)
                    self.object.remove=True
                    self.room.RemoveController(self.id)
                    self.room.PlaySound("sound45", self.object.posX, self.object.posY)

Controller=PackageController