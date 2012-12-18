from main import *
from controller import *

class BulletController(PersonController):
     def __init__(self,args):
          PersonController.__init__(self,args)
          self.color=1
          self.angle=0
          
     def Update(self,args):
          if self.color==1:
               self.room.particle.AddParticle("circle",self.object.posX+(self.object.width/2),self.object.posY+(self.object.height/2),0,0,3.0,-0.01)
          elif self.color==2:
               angle2=self.angle+180 if self.angle+180<360 else self.angle-180
               #self.room.particle.AddParticle("circle7",(self.object.posX+self.object.width/2)+(16*cos[self.angle]),(self.object.posY+self.object.width/2)-(8*sin[self.angle]), 0,0,3.0,-0.01)
               #self.room.particle.AddParticle("circle7",(self.object.posX+self.object.width/2)+(16*cos[angle2]),(self.object.posY+self.object.width/2)-(8*sin[angle2]), 0,0,3.0,-0.01)
               self.room.particle.AddParticle("circle8",(self.object.posX+self.object.width/2),(self.object.posY+self.object.width/2), 0,0,3.0,-0.01)
               self.angle=self.angle+30 if self.angle<360 else 0
               
          self.object.data["current_life"]=self.object.data["current_life"]+1
          if self.object.data["life"] >= 0:
               self.object.sprite.SetAlpha( 255-int( float(255)*(float(self.object.data["current_life"])/float(self.object.data["life"])) ) )
               if self.object.data["current_life"] >= self.object.data["life"]:
                    self.object.remove=True
                    self.room.RemoveController(self.id)
          
     def OnObjectLand(self,message):
          if self.object.data["life"] <= 0:
               self.object.remove=True
               self.room.RemoveController(self.id)
               
     def Hit(self):
          self.object.remove=True
          self.room.RemoveController(self.id)
               
     def OnObjectCollision(self,message):
          if message.collision_type != COLLISION_WALL:
               if message.obj2.name == "player":
                    ctrl=self.room.GetControllerByObj(message.obj2)
                    ctrl.Hit(1)
               elif message.obj2.type.name == "crate" or message.obj2.type.name == "cannon" \
               or message.obj2.type.name == "turret" or message.obj2.type.name == "platform" \
               or message.obj2.type.name == "gate" or message.obj2.type.name == "gate2":
                    self.Hit()
          else:
               self.Hit()

Controller=BulletController