from main import *
from controller import *

class DoorController(PersonController):
     def __init__(self,args):
          PersonController.__init__(self,args)
          self.teleportable=True
          
     def Update(self,args):
          pass
          
     def OnObjectAction(self,message):
          if message.action_obj.name == "player":
               if self.object.data["open"] == 0:
                    opened=False
                    if self.object.type.name == "door_yellow" and message.action_obj.data["key_yellow"] > 0:
                              message.action_obj.data["key_yellow"]=message.action_obj.data["key_yellow"]-1
                              opened=True
                    elif self.object.type.name == "door_blue" and message.action_obj.data["key_blue"] > 0:
                              message.action_obj.data["key_blue"]=message.action_obj.data["key_blue"]-1
                              opened=True   
                    elif self.object.type.name == "door_pink" and message.action_obj.data["key_pink"] > 0:
                              message.action_obj.data["key_pink"]=message.action_obj.data["key_pink"]-1
                              opened=True
                    
                    if opened:
                         self.object.BroadcastMessage(PlayerMessage(self.object,OBJECT_OPENED))
                         self.object.data["open"]=1
                         self.room.PlaySound("thump", self.object.posX, self.object.posY)
                    else:
                         self.object.BroadcastMessage(PlayerMessage(self.object,OBJECT_LOCKED))
                         self.room.PlaySound("misc020", self.object.posX, self.object.posY)
                    
               if self.object.data["open"] == 1 and self.teleportable:
                    o, tel_x, tel_y, tel_obj = None, -1, -1, False
                    self.room.PlaySound("thump", self.object.posX, self.object.posY)
                    
                    if self.object.data["teleport_obj"] != "":
                         o=self.room.GetObjectByName(self.object.data["teleport_obj"])
                         if o != None:
                              tel_x=o.posX
                              tel_y=o.posY
                              tel_obj=True
                              
                    if tel_obj == False:
                         tel_x=self.object.data["teleport_x"]
                         tel_y=self.object.data["teleport_y"]
                    
                    if tel_x != -1 and tel_y != -1:
                         message.action_obj.posX=tel_x
                         message.action_obj.posY=tel_y
                         message.action_obj.action[DOWN] = False
                         self.teleportable=False
                         self.room.AddAlarm(self,30,1)
                         if tel_obj:
                              ctrl=self.room.GetControllerByObj(o)
                              ctrl.teleportable=False
                              self.room.AddAlarm(ctrl,30,1)
                    
     def OnAlarm(self,message):
          if message.data == 1:
               self.teleportable=True


Controller=DoorController