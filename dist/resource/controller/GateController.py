from main import *
from controller import *
from objType import *

class GateController(PersonController):
     def __init__(self,args):
          PersonController.__init__(self,args)
          
          if self.object.data["switch"] == 0:
               self.object.collision=SOLID
          else:
               self.object.collision=GHOST

          self.object.sprite.SetAnimation(self.object.data["switch"])
          
     def Update(self,args):
          pass
          
     def Switch(self):
          if self.object.data["switch"] == 0:
               self.object.data["switch"]=1
               self.object.collision=GHOST
          else:
               self.object.data["switch"]=0
               self.object.collision=SOLID
          
          self.object.sprite.SetAnimation(self.object.data["switch"])
     
     def OnObjectAction(self,message):
          if message.action_obj.name != "player":
               self.Switch()

Controller=GateController