from main import *
from controller import *

class SpringController(PersonController):
     def __init__(self,args):
          PersonController.__init__(self,args)
          self.object.sprite.Pause()
          
     def Update(self,args):
          pass
          
     def OnObjectCollision(self,message):
          if message.collision_type != COLLISION_WALL:
               if message.obj2.type.name=="player" and message.obj2.jump:
                    message.obj2.velY=(-self.object.data["strength"])
                    self.object.sprite.Resume()
                    self.room.PlaySound("scifi003", self.object.posX, self.object.posY)
                    ctrl=self.room.GetControllerByObj(message.obj2)
                    ctrl.spring=True

Controller=SpringController