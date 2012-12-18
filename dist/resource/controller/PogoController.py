from main import *
from controller import *

class PogoController(PersonController):
     def __init__(self,args):
          PersonController.__init__(self,args)
          self.object.sprite.SetAnimation(self.object.data["direction"])
     
     def Update(self,args):
          if self.object.data["direction"] == 0:
               self.object.GenerateAction(LEFT)
          else:
               self.object.GenerateAction(RIGHT)
          
          self.object.GenerateAction(JUMP)
                         
     def OnObjectCollision(self,message):
          if message.collision_type != COLLISION_WALL:
               if message.obj2.name == "player":
                    ctrl=self.room.GetControllerByObj(message.obj2)
                    ctrl.Hit(1)
          #if pogo hits wall, change direction
          else:
               self.object.data["direction"]=1 if self.object.data["direction"] == 0 else 0
               self.object.sprite.SetAnimation(self.object.data["direction"])
               
               
               

Controller=PogoController