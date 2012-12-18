from main import *
from controller import *

class DroidController(PersonController):
     FADE=5
     def __init__(self,args):
          PersonController.__init__(self,args)
          self.phase=0
          self.step=0
          self.alpha=0
          self.hit=None
          self.object.origX=self.object.posX
          self.object.origY=self.object.posY
          
     def Update(self,args):
          #idle mode - look for player
          if self.phase == 0:
               if (self.room.player.posX+self.room.player.width >= self.object.posX-self.object.data["distance"] \
               and self.room.player.posX <= self.object.posX+self.object.width+self.object.data["distance"]) \
               and self.room.player.posY > self.object.posY:
                    self.phase=1
                    self.object.sprite.SetAnimation(1)
          #chase mode
          elif self.phase == 1:
               #find angle between droid and player
               a=(self.object.posX+self.object.width/2)-(self.room.player.posX+self.room.player.width/2)
               b=(self.object.posY+self.object.height/2)-(self.room.player.posY+self.room.player.height/2)
               #find unit vector (||v||cos(t)i, ||v||sin(t)jd), solve for theta
               magnitude=math.sqrt((a**2)+(b**2))
               magnitude=magnitude if magnitude>0.0 else 0.1
               unitcos=float(a)/float(magnitude)
               angle=int(math.degrees(math.acos(unitcos)))
               if b < 0: angle=360-angle
               angle=0 if angle>=360 else angle
               
               self.object.velX=-self.object.data["speed"]*cos[angle]
               self.object.velY=-self.object.data["speed"]*sin[angle]
          #fade out and die
          elif self.phase == 2:
               self.object.sprite.SetAlpha(self.object.sprite.alpha-self.alpha)
               self.step+=1
               #completely invisible now
               if self.step >= DroidController.FADE:
                    self.object.remove=True
                    self.room.RemoveController(self.id)
               
     def Die(self):
          self.alpha=int(math.ceil(255.0/float(DroidController.FADE)))
          self.phase=2

     def OnObjectCollision(self,message):
          if message.collision_type != COLLISION_WALL:
               if message.obj2.name == "player":
                    ctrl=self.room.GetControllerByObj(message.obj2)
                    ctrl.Hit(2)
                    self.Die()
               if message.obj2.type.name == "bullet" and self.phase != 2 and self.hit != message.obj2:
                    self.object.data["life"]-=1
                    self.hit=message.obj2
                    self.room.particle.AddParticle("circle3",self.object.posX+(self.object.width/2),self.object.posY,-5,-5,3.0,-0.01)
                    self.room.particle.AddParticle("circle3",self.object.posX+(self.object.width/2),self.object.posY,5,-5,3.0,-0.01)
                    ctrl=self.room.GetControllerByObj(message.obj2)
                    
                    if ctrl != None: ctrl.Hit()
                    if self.object.data["life"] <= 0:
                         self.Die()
                         
          else:
               self.Die()
                    
     def OnObjectLand(self,message):
          self.Die()
               

Controller=DroidController