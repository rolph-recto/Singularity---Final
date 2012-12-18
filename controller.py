#!/usr/bin/env python

import main
import room
from message import *
from message_class import *

class Controller:
     def __init__(self,args):
          self.id=0
          self.priority=0
          self.room=args[0]
          self.object=args[1]
          
     def Update(self,args):
          pass     
          
     def OnMessage(self,message):
          pass

class PersonController(Controller):
     def __init__(self,args):
          Controller.__init__(self,args)
          self.object.AddSubscriber(self,OBJECT)
          
     def Update(self,args):
          pass
     
     def OnObjectDestroy(self,message):
          self.room.RemoveController(self.id)
     
     def OnMessage(self,message):
          pass
               
     def OnKeyDown(self,message):
          pass
                    
     def OnObjectMove(self,message):
          pass
         
     def OnObjectFall(self,message):
          pass
         
     def OnObjectJump(self,message):
          pass
          
     def OnObjectLand(self,message):
          pass
     
     def OnObjectCollision(self,message):
          pass
          
     def OnAlarm(self,message):
          pass
          
class PlayerController(PersonController):
     def __init__(self,args):
          PersonController.__init__(self,args)
          
          if self.object.data["startX"] == -1:
               self.object.data["startX"]=self.object.posX
          if self.object.data["startY"] == -1:
               self.object.data["startY"]=self.object.posY
          
          self.object.sprite.Pause()
          self.invincible=False
          self.alarm=-1
          self.object.sprite.Pause()
          self.spring=False
          self.keyUp=K_UP
          self.keyDown=K_DOWN
          self.keyLeft=K_LEFT
          self.keyRight=K_RIGHT
          self.keyJump=K_SPACE

     def Hit(self,damage=1):
          if self.invincible == False:
               self.object.data["currentHP"]=SetBound(self.object.data["currentHP"]-damage,0,self.object.data["currentHP"]-damage)
               self.room.particle.AddParticle("circle3",self.object.posX+(self.object.width/2),self.object.posY,-5,-5,3.0,-0.01)
               self.room.particle.AddParticle("circle3",self.object.posX+(self.object.width/2),self.object.posY,5,-5,3.0,-0.01)
               if self.object.data["currentHP"] <= 0:
                    self.room.AddAlarm(self,1,3,60)
                    self.room.AddAlarm(self,62,2)
                    self.invincible=True
                    self.object.disabled=True
                    self.object.sprite.Pause()
                    self.object.BroadcastMessage(PlayerMessage(self.object,PLAYER_DIED))
                    self.room.PlaySound("scifi035")
               else:
                    self.object.sprite.SetAlpha(100)
                    self.invincible=True
                    self.alarm=self.room.AddAlarm(self,90,1)
                    self.object.BroadcastMessage(PlayerMessage(self.object,PLAYER_HIT))
                    self.room.PlaySound("tom")
     
     def Score(self,points):  
          self.object.data["score"]=self.object.data["score"]+points
          self.object.BroadcastMessage(PlayerMessage(self.object,PLAYER_SCORED))
     
     def Update(self,args):
          key=pygame.key.get_pressed()
          
          if self.spring:
               self.room.particle.AddParticle("circle6",self.object.posX+(self.object.width/2),self.object.posY+(self.object.height/2),0,0,3.0,0.0)
          
          if self.object.disabled == False:
               if key[self.keyLeft]:
                    self.object.GenerateAction(LEFT)
                    self.object.sprite.Resume()
                    #self.object.sprite.SetAnimation(0)
               elif key[self.keyRight]:
                    self.object.GenerateAction(RIGHT)
                    self.object.sprite.Resume()
                    #self.object.sprite.SetAnimation(1)
               else:
                    self.object.sprite.Pause()
               
               if key[self.keyUp]:
                    self.object.GenerateAction(UP)
               if key[self.keyDown]:
                    self.object.GenerateAction(DOWN)
               
               if key[self.keyJump]:
                    self.object.GenerateAction(JUMP)
     
     def OnAlarm(self,message):
          if message.data == 1:
               self.invincible=False
               self.object.sprite.SetAlpha(255)
          if message.data == 2:
               self.object.posX=self.object.data["startX"]
               self.object.posY=self.object.data["startY"]
               self.object.data["currentHP"]=self.object.data["HP"]
               self.room.AddAlarm(self,1,4,65)
               self.room.AddAlarm(self,70,5)
          if message.data == 3:
               self.object.sprite.SetAlpha(self.object.sprite.alpha-4)
          if message.data == 4:
               self.object.sprite.SetAlpha(self.object.sprite.alpha+4)
          if message.data == 5:
               self.invincible=False
               self.object.disabled=False
     
     def OnMessage(self,message):
          if message.type == INPUT_KEYDOWN:
               pass
               
     def OnObjectLand(self,message):
          if self.spring:
               self.spring=False
     
     """
     def OnKeyDown(self,message):
          if message.type == INPUT_KEYDOWN:
               if message.event.key == K_LEFT:
                    self.object.GenerateAction(LEFT)
               if message.event.key == K_RIGHT:
                    self.object.GenerateAction(RIGHT)
               if message.event.key == K_UP:
                    self.object.GenerateAction(UP)
               if message.event.key == K_DOWN:
                    self.object.GenerateAction(DOWN)
               if message.event.key == K_SPACE:
                    self.object.GenerateAction(JUMP)
     """
     
