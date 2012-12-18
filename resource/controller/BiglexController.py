from main import *
from controller import *

class BiglexController(PersonController):
     FADE=90
     def __init__(self,args):
          PersonController.__init__(self,args)
          self.object.data["maxHP"]=25
          self.object.data["HP"]=25
          self.alpha=0
          self.step=0
          self.object.data["fade"]=False
          self.object.data["hit"]=True
          self.object.data["dead"]=False
          self.hit=None
          
     def Update(self,args):
          if self.object.data["fade"]:
               self.object.sprite.SetAlpha(self.object.sprite.alpha-self.alpha)
               self.step+=1
               #completely invisible now
               if self.step >= BiglexController.FADE:
                    self.object.data["fade"]=False
     
     def Die(self):
          self.dead=True
          self.alpha=int(math.ceil(255.0/float(BiglexController.FADE)))
          self.object.BroadcastMessage(ObjectMessage(self.object,OBJECT_ACTION,(self.object,)))
          
     def OnObjectCollision(self,message):
          if message.collision_type != COLLISION_WALL:
               if message.obj2.name == "player":
                    ctrl=self.room.GetControllerByObj(message.obj2)
                    ctrl.Hit(message.obj2.data["HP"])
               elif message.obj2.type.name == "bullet" and message.obj2 != self.hit and self.object.data["dead"] == False:
                    self.object.data["HP"]-=1
                    self.hit=message.obj2
                    self.room.particle.AddParticle("circle3",self.object.posX+(self.object.width/2),self.object.posY,-5,-5,3.0,-0.01)
                    self.room.particle.AddParticle("circle3",self.object.posX+(self.object.width/2),self.object.posY,5,-5,3.0,-0.01)
                    ctrl=self.room.GetControllerByObj(message.obj2)
                    
                    if ctrl != None: ctrl.Hit()
                    if self.object.data["HP"] <= 0:
                         self.Die()
               

Controller=BiglexController