from main import *
from controller import *

class LeverController(PersonController):
     def __init__(self,args):
          PersonController.__init__(self,args)
          
          self.object.sprite.SetAnimation(self.object.data["switch"])
          self.switchable=True
          
     def Update(self,args):
          pass
          
     def Switch(self):
          if self.object.data["switch"] == 0:
               self.object.data["switch"]=1
          else:
               self.object.data["switch"]=0
          
          for i in self.object.data["gate"]:
               o=self.room.GetObjectByName(i)
               if o != None:
                    o.BroadcastMessage(ObjectMessage(o,OBJECT_ACTION,(self.object,)))
               
          self.object.sprite.SetAnimation(self.object.data["switch"])
          self.room.PlaySound("sound6",self.object.posX,self.object.posY)
          
     def OnObjectAction(self,message):
          if self.switchable:
               self.Switch()
               self.room.AddAlarm(self,5,1)
               self.switchable=False

     def OnAlarm(self,message):
          if message.data == 1:
               self.switchable=True
     
Controller=LeverController