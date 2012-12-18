from main import *
from controller import *
from objType import *

class BreakController(PersonController):
     def __init__(self,args):
          PersonController.__init__(self,args)
          self.hidden=False
          
     def Update(self,args):
          pass
          
     def Hide(self):
          self.hidden=True
          self.object.sprite.SetAlpha(0)
          self.object.collision=GHOST
          
     def Appear(self):
          self.hidden=False
          self.object.sprite.SetAlpha(255)
          self.object.collision=SOLID
     
     def OnObjectCollision(self,message):
          if message.obj2.type.name == "bullet" and self.hidden == False:
               self.Hide()
               if self.object.data["respawn"] == 1:
                    self.room.AddAlarm(self,self.object.data["respawn_time"],1)
                    
               message.obj2.remove=True
               self.room.RemoveController(message.obj2.ctrl)
                    
     def OnAlarm(self,message):
          if message.data == 1:
               self.Appear()
               

Controller=BreakController