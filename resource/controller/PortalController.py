from main import *
from controller import *

class PortalController(PersonController):
     def __init__(self,args):
          PersonController.__init__(self,args)
          
     def Update(self,args):
          pass
          
     def OnObjectCollision(self,message):
          if message.collision_type != COLLISION_WALL:
               if message.obj2.type.name=="player":
                    self.room.MoveObjectToPos(message.obj2.id, self.object.data["teleport_spot"][0], self.object.data["teleport_spot"][1])
                    self.room.particle.AddParticle("circle2",self.object.data["teleport_spot"][0],self.object.data["teleport_spot"][1],-5,-5,3.0,-0.01)
                    self.room.particle.AddParticle("circle2",self.object.data["teleport_spot"][0],self.object.data["teleport_spot"][1],-5,5,3.0,-0.01)
                    self.room.particle.AddParticle("circle2",self.object.data["teleport_spot"][0],self.object.data["teleport_spot"][1],5,-5,3.0,-0.01)
                    self.room.particle.AddParticle("circle2",self.object.data["teleport_spot"][0],self.object.data["teleport_spot"][1],5,5,3.0,-0.01)
                    
                    self.room.PlaySound("scifi014", self.object.data["teleport_spot"][0], self.object.data["teleport_spot"][1])

Controller=PortalController