from main import *
from controller import *
from objType import *

class FalsefloorController(PersonController):
     def __init__(self,args):
          PersonController.__init__(self,args)
          self.phase=0
          self.step=0
          self.alpha=0
          
     def Update(self,args):
          #hiding - fade out
          if self.phase == 1:
               if self.step == 0:
                    self.alpha=int(math.ceil(255.0/float(self.object.data["speed"])))
                    
               self.object.sprite.SetAlpha(self.object.sprite.alpha-self.alpha)
               self.step+=1
               #completely vanished now
               if self.step >= self.object.data["speed"]:
                    self.phase=2
                    self.step=0
          #appearing - fading in
          elif self.phase == 3:
               if self.step == 0:
                    self.alpha=int(math.ceil(255.0/float(self.object.data["speed"])))
                    
               self.object.sprite.SetAlpha(self.object.sprite.alpha+self.alpha)
               self.step+=1
               #completely visible now
               if self.step >= self.object.data["speed"]:
                    self.phase=0
                    self.step=0
          
     def Hide(self):
          self.object.collision=GHOST
          self.phase=1
          if self.object.data["respawn"] == 1:
               self.room.AddAlarm(self,self.object.data["respawn_interval"],1)
          
     def Appear(self):
          self.object.collision=SOLID
          self.phase=3
          
     def OnObjectCollision(self,message):
          if message.obj2.name == "player":
               if self.phase == 0:
                    self.Hide()
                    
     def OnAlarm(self,message):
          if message.data == 1:
               self.Appear()
               

Controller=FalsefloorController