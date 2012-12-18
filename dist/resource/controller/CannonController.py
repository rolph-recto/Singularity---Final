from main import *
from controller import *

class CannonController(PersonController):
     def __init__(self,args):
          PersonController.__init__(self,args)
          self.action=-2
          self.index=-1
          self.iter=0
          self.step=0
          self.pos=-1
          if len(self.object.data["walk_list"]) > 0:
               self.index=0
          
     def Update(self,args):
          if self.index >= 0:
               #determine action
               if self.action == -2:
                    cmd=self.object.data["walk_list"][ self.index ]
                    csplit=cmd.split(":")
                         
                    if csplit[0] == "wait":
                         self.action=-1
                         self.step=int(csplit[1])
                         self.object.sprite.Pause()
                    elif csplit[0] == "to-x":
                         self.pos=int(csplit[1])
                         self.step=-2
                         if self.object.posX < self.pos:
                              self.action=RIGHT
                         elif self.object.posX > self.pos:
                              self.action=LEFT
                         else:
                              self.action=-1
                              self.step=1
                    elif csplit[0] == "to-y":
                         self.pos=int(csplit[1])
                         self.step=-2
                         if self.object.posY < self.pos:
                              self.action=DOWN
                         elif self.object.posY > self.pos:
                              self.action=UP
                         else:
                              self.action=-1
                              self.step=1
                              
               #move accordingly
               if self.action >= 0:
                    self.object.GenerateAction(self.action)
                    
               #update
               self.iter+=1
               change=False
               if self.step != -2 and self.iter >= self.step:
                         change=True
                         
               else:
                    if self.action == LEFT and self.object.posX <= self.pos:
                         change=True
                    elif self.action == RIGHT and self.object.posX >= self.pos:
                         change=True
                    elif self.action == UP and self.object.posY <= self.pos:
                         change=True
                    elif self.action == DOWN and self.object.posY >= self.pos:
                         change=True
               
               if change:
                    self.index+=1
                    self.action=-2
                    self.pos=-1
                    self.step=0
                    self.iter=0
                    self.object.velX=0.0
                    self.object.velY=0.0
                    if self.index >= len(self.object.data["walk_list"]):
                         self.index=0
     
          self.object.data["step"]=self.object.data["step"]+1
          if self.object.data["step"] == self.object.data["interval"]:
               self.object.data["step"]=0
               objID=-1
               obj=None
               
               for i in range(len(self.object.data["upShot"])):
                    objID=self.room.AddObject("cannonball",self.object.posX+(self.object.width/2),self.object.posY-5)
                    obj=self.room.GetObjectById(objID)
                    obj.data["life"]=60
                    obj.velX=self.object.data["upShot"][i][1]
                    obj.velY=-self.object.data["upShot"][i][2]
                    obj.accelX=self.object.data["upShot"][i][1]
                    obj.accelY=-self.object.data["upShot"][i][2]
                         
                    if self.object.data["upShot"][i][0] != 1:     
                         obj.fall=False
                         
               for i in range(len(self.object.data["downShot"])):
                    objID=self.room.AddObject("cannonball",self.object.posX+(self.object.width/2),self.object.posY+self.object.width+5)
                    obj=self.room.GetObjectById(objID)
                    obj.data["life"]=60
                    obj.velX=self.object.data["downShot"][i][1]
                    obj.velY=self.object.data["downShot"][i][2]
                    obj.accelX=self.object.data["downShot"][i][1]
                    obj.accelY=self.object.data["downShot"][i][2]
                         
                    if self.object.data["downShot"][i][0] != 1:
                         obj.fall=False
                         
               for i in range(len(self.object.data["leftShot"])):
                    objID=self.room.AddObject("cannonball",self.object.posX-5,self.object.posY+(self.object.height/2))
                    obj=self.room.GetObjectById(objID)
                    obj.data["life"]=60
                    obj.velX=-self.object.data["leftShot"][i][1]
                    obj.velY=self.object.data["leftShot"][i][2]
                    obj.accelX=-self.object.data["leftShot"][i][1]
                    obj.accelY=self.object.data["leftShot"][i][2]
                         
                    if self.object.data["leftShot"][i][0] != 1:
                         obj.fall=False
                    
               for i in range(len(self.object.data["rightShot"])):
                    objID=self.room.AddObject("cannonball",self.object.posX+(self.object.width)+5,self.object.posY+(self.object.height/2))
                    obj=self.room.GetObjectById(objID)
                    obj.data["life"]=60
                    obj.velX=self.object.data["rightShot"][i][1]
                    obj.velY=self.object.data["rightShot"][i][2]
                    obj.accelX=self.object.data["rightShot"][i][1]
                    obj.accelY=self.object.data["rightShot"][i][2]
                         
                    if self.object.data["rightShot"][i][0] != 1:
                         obj.fall=False
                         
               self.room.PlaySound("scifi018",self.object.posX,self.object.posY)

Controller=CannonController