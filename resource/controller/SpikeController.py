from main import *
from controller import *

class SpikeController(PersonController):
     def __init__(self,args):
          PersonController.__init__(self,args)
          self.object.sprite.SetAnimation(self.object.data["direction"])
          
     def Update(self,args):
          pass
          
     def OnObjectCollision(self,message):
          if message.obj2.name == "player":
               ctrl=self.room.GetControllerByObj(message.obj2)
               if self.object.data["damage"] < 0:
                    ctrl.Hit(message.obj2.data["HP"])
               else:
                    ctrl.Hit(self.object.data["damage"])
               

Controller=SpikeController