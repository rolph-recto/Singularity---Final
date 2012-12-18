from main import *
from controller import *

class KeyController(PersonController):
     def __init__(self,args):
          PersonController.__init__(self,args)
          self.grav=False
          
     def Update(self,args):
          pass
          
               
     def OnObjectCollision(self,message):
          if message.collision_type != COLLISION_WALL and self.grav==False:
               if message.obj2.name == "player":
                    if self.object.type.name == "key_yellow":
                         message.obj2.data["key_yellow"]+=1
                    elif self.object.type.name == "key_blue":
                         message.obj2.data["key_blue"]+=1
                    elif self.object.type.name == "key_pink":
                         message.obj2.data["key_pink"]+=1
               
                    self.object.remove=True
                    self.room.RemoveController(self.id)
                    self.room.PlaySound("light", self.object.posX, self.object.posY)

Controller=KeyController