from main import *
from controller import *

class SentryController(PersonController):
     FADE=15
     def __init__(self,args):
          PersonController.__init__(self,args)
          
          self.object.sprite.Pause()
          self.hit=None    
          self.action=-2
          self.index=-1
          self.iter=0
          self.step=0
          self.xpos=-1
          self.phase=0
          self.alpha=0
          self.life=3
          
          self.object.origX=self.object.posX
          self.object.origY=self.object.posY
          
          if len(self.object.data["walk_list"]) > 0:
               self.index=0
     
     def Update(self,args):
          if self.index < 0:
               if len(self.object.data["walk_list"]) > 0:
                    self.index=0
                    
          elif self.index >= 0 and self.phase == 0:
               #determine action
               if self.action == -2:
                    cmd=self.object.data["walk_list"][ self.index ]
                    if type(cmd) == type("abc"):
                         csplit=cmd.split(":")
                         
                    if type(cmd) == type(123):
                         if cmd < 0:
                              self.action=LEFT
                              self.object.sprite.Resume()
                              self.object.sprite.SetAnimation(0)
                         elif cmd > 0:
                              self.action=RIGHT
                              self.object.sprite.Resume()
                              self.object.sprite.SetAnimation(1)
                         self.step=abs(cmd)
                    elif csplit[0] == "wait":
                         self.action=-1
                         self.step=int(csplit[1])
                         self.object.sprite.Pause()
                    elif csplit[0] == "jump":
                         self.action=JUMP
                         self.step=1
                    elif csplit[0] == "to":
                         self.xpos=int(csplit[1])
                         self.step=-2
                         if self.object.posX < self.xpos:
                              self.action=RIGHT
                              self.object.sprite.Resume()
                              self.object.sprite.SetAnimation(1)
                         elif self.object.posX > self.xpos:
                              self.action=LEFT
                              self.object.sprite.Resume()
                              self.object.sprite.SetAnimation(0)
                         else:
                              self.action=-1
                              self.step=1
                              
               #move accordingly
               if self.action >= 0:
                    self.object.GenerateAction(self.action)
                    self.room.particle.AddParticle("diamond",self.object.posX+(self.object.width/2),self.object.posY+(self.object.height/2),0,0,3.0,0.0)
                    
               #update
               self.iter+=1
               change=False
               if self.step != -2 and self.iter >= self.step:
                         change=True
                         
               else:
                    if self.action == LEFT and self.object.posX <= self.xpos:
                         change=True
                    elif self.action == RIGHT and self.object.posX >= self.xpos:
                         change=True
               
               if change:
                    self.index+=1
                    self.action=-2
                    self.xpos=-1
                    self.step=0
                    self.iter=0
                    if self.index >= len(self.object.data["walk_list"]):
                         self.index=0
                         
          elif self.phase==1:
               self.object.sprite.SetAlpha(self.object.sprite.alpha-self.alpha)
               self.step+=1
               #completely invisible now
               if self.step >= SentryController.FADE:
                    self.object.remove=True
                    self.room.RemoveController(self.id)
                         
     def Die(self):
          self.alpha=int(math.ceil(255.0/float(SentryController.FADE)))
          self.phase=1
                         
     def OnObjectCollision(self,message):
          if message.collision_type != COLLISION_WALL:
               if message.obj2.name == "player":
                    ctrl=self.room.GetControllerByObj(message.obj2)
                    ctrl.Hit(1)
               if message.obj2.type.name == "bullet" and self.phase != 2 and self.hit != message.obj2:
                    self.life-=1
                    self.hit=message.obj2
                    self.room.particle.AddParticle("circle3",self.object.posX+(self.object.width/2),self.object.posY,-5,-5,3.0,-0.01)
                    self.room.particle.AddParticle("circle3",self.object.posX+(self.object.width/2),self.object.posY,5,-5,3.0,-0.01)
                    ctrl=self.room.GetControllerByObj(message.obj2)
                    
                    if ctrl != None: ctrl.Hit()
                    if self.life <= 0:
                         self.Die()
               

Controller=SentryController