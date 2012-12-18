#!/usr/bin/env python
from room import *
from map import *
from pickle import *
import pygame.gfxdraw
from guichan import *

#import psyco
#psyco.profile()

from state import *
from view import *
from particle import *

from objType import *

s=None
screen = None
room = None
v=None
key=None
clock, inputMessage=None, None
pause, done = False, False
player=None
config={}
updateRect=[]

#GUI
gui, input, graphics, font, top, action = None, None, None, None, None, None
notifyLabel=None
heartIcon, heartLabel=None, None
keyYellowIcon, keyYellowLabel=None, None
keyPinkIcon, keyPinkLabel=None, None
keyBlueIcon, keyBlueLabel=None, None
packageIcon, packageLabel=None, None
dialogContainer=None
dialogIcon=None
dialogText=None
dialogTitle=None
dialogButton=None
splashLabel=None
finLabel=False
timeLabel=False
lexLabel, lexProgress=None, None
GuiImages={}
cutscene=False
cutsceneList=[]
cutsceneIndex=-1
scrolling=False
pan=False
unpause=False
gravGun=None
boss=False
pAngle=0
gAngle=0
reload=0
gun=0

def FitText(text,size=50):
     textlist=text.split(" ")
     newtext=""
     stext=""
     for s in textlist:
          if len(stext+s) <= size:
               stext+=s+" "
          else:
               stext+=s+"\n"
               newtext+=stext
               stext=""

     if stext != "":
          newtext+=stext

     return newtext

class InitState(State):
     def __init__(self):
          State.__init__(self,"init",InitState.EventTable)

     def Start(self, args=()):
          os.chdir(BASEDIR)
          execfile("config.py")

          pygame.init()
          global screen
          screen = pygame.display.set_mode((config["SCREEN_WIDTH"], config["SCREEN_HEIGHT"]), config["DISPLAY_FLAGS"])
          pygame.display.set_caption(config["TITLE"],config["ICON_TITLE"])
          icon=pygame.image.load(config["ICON"])
          pygame.display.set_icon(icon)
          pygame.mixer.init()
          pygame.key.set_repeat(config["KEYREPEAT_DELAY"], config["KEYREPEAT_INTERVAL"])
          pygame.mouse.set_visible(False)

          global room
          room=Room()
          room.database.LoadXML(config["DATABASE"])
          room.SetTileTemplate(config["TILE_TEMPLATE"])

          particle=room.particle

          for i in config["PARTICLE_TEMPLATES"]:
               particle.AddTemplate(i)

          global clock, inputMessage
          clock = pygame.time.Clock()
          inputMessage=InputMessage(None)

          self.InitGUI()

     def InitGUI(self):
          global gui, input, graphics, font, top, action
          gui=Gui()
          input=PygameInput()
          Image.mImageLoader=PygameImageLoader()
          graphics=PygameGraphics()
          graphics.setTarget(screen)
          font=PygameFont(config["FONT_FILE"],config["FONT_SIZE"],config["FONT_COLOR"])
          font.setGlyphSpacing(config["FONT_SIZE"])
          Widget.setGlobalFont(font)
          top=Container()
          top.setOpaque(False)
          top.setPosition(0,0)
          top.setSize(config["SCREEN_WIDTH"],config["SCREEN_HEIGHT"])
          gui.setInput(input)
          gui.setTop(top)
          gui.setGraphics(graphics)

          action=ActionListener()
          action.action=OnAction
          action.valueChanged=OnAction

          #put all images in GuiImages dict
          for k, v in room.database[IMAGE].iteritems():
               i=PygameImage(v)
               GuiImages[k]=i

          global notifyLabel
          notifyLabel=Label()
          notifyLabel.setFont(font)
          notifyLabel.setTextColor(Color(255,255,255))
          notifyLabel.setPosition((config["SCREEN_WIDTH"]/2)-(notifyLabel.getWidth()/2), config["VIEW_POSY"]+(config["VIEW_HEIGHT"]*TILEHEIGHT)+5)
          top.add(notifyLabel)

          global heartLabel, heartIcon
          heartLabel=Label()
          heartLabel.setFont(font)
          heartLabel.setTextColor(Color(255,255,255))
          heartLabel.setPosition(30,10)
          heartIcon=Icon(GuiImages["heart"])
          top.add(heartIcon,10,10)
          top.add(heartLabel)

          global keyYellowLabel, keyYellowIcon
          keyYellowLabel=Label()
          keyYellowLabel.setFont(font)
          keyYellowLabel.setTextColor(Color(255,255,255))
          keyYellowLabel.setPosition(110,10)
          keyYellowIcon=Icon(GuiImages["key_yellow"])
          top.add(keyYellowIcon,90,10)
          top.add(keyYellowLabel)

          global keyBlueLabel, keyBlueIcon
          keyBlueLabel=Label()
          keyBlueLabel.setFont(font)
          keyBlueLabel.setTextColor(Color(255,255,255))
          keyBlueLabel.setPosition(190,10)
          keyBlueIcon=Icon(GuiImages["key_blue"])
          top.add(keyBlueIcon,170,10)
          top.add(keyBlueLabel)

          global keyPinkLabel, keyPinkIcon
          keyPinkLabel=Label()
          keyPinkLabel.setFont(font)
          keyPinkLabel.setTextColor(Color(255,255,255))
          keyPinkLabel.setPosition(270,10)
          keyPinkIcon=Icon(GuiImages["key_pink"])
          top.add(keyPinkIcon,250,10)
          top.add(keyPinkLabel)

          global packageLabel, packageIcon
          packageLabel=Label()
          packageLabel.setFont(font)
          packageLabel.setTextColor(Color(255,255,255))
          packageLabel.setPosition(330,10)
          packageIcon=Icon(GuiImages["package"])
          #top.add(packageIcon,330,10)
          top.add(packageLabel)

          global dialogContainer
          dialogContainer=Container()
          dialogContainer.setWidth(config["SCREEN_WIDTH"]-10)
          dialogContainer.setHeight(107)
          dialogContainer.setPosition(5,config["SCREEN_HEIGHT"]-dialogContainer.getHeight()-5)
          dialogContainer.setBaseColor(Color(1,79,107))
          dialogContainer.setFrameSize(5)
          top.add(dialogContainer)

          global dialogIcon, GuiImages
          dialogIcon=Icon(GuiImages["may"])
          dialogContainer.add(dialogIcon,15,10)

          global dialogTitle
          dialogTitle=Label("default")
          dialogTitle.setFont(font)
          dialogTitle.setTextColor(Color(255,255,255))
          dialogTitle.setPosition(47-(dialogTitle.getWidth()/2),80)
          dialogContainer.add(dialogTitle)

          global dialogText
          dialogText=TextBox("")
          dialogText.setPosition(89,10)
          dialogText.setOpaque(False)
          dialogText.setEditable(False)
          dialogContainer.add(dialogText)

          global dialogButton
          dialogButton=Button(">")
          dialogButton.setTextColor(Color(255,255,255))
          dialogButton.setBaseColor(Color(1,79,107))
          dialogButton.setPosition(dialogContainer.getWidth()-25, dialogContainer.getHeight()-25)
          dialogButton.setActionEventId("dialog")
          dialogButton.addActionListener(action)
          dialogContainer.add(dialogButton)

          global splashLabel
          splashLabel=Label("")
          splashLabel.setTextColor(Color(255,255,255))
          top.add(splashLabel,5,config["SCREEN_HEIGHT"]-16)

          global finLabel
          finLabel=Label("F i n")
          finLabel.setTextColor(Color(255,255,255))
          top.add(finLabel,(config["SCREEN_WIDTH"]/2)-(finLabel.getWidth()/2),(config["SCREEN_HEIGHT"]/2)-(finLabel.getHeight()/2))

          global timeLabel
          timeLabel=Label("")
          timeLabel.setTextColor(Color(255,255,255))
          top.add(timeLabel,config["SCREEN_WIDTH"]-50,10)

          global lexLabel, lexProgress
          lexLabel=Label("Lex")
          lexLabel.setTextColor(Color(255,255,255))
          top.add(lexLabel,10,config["SCREEN_HEIGHT"]-25)

          lexProgress=ProgressBar()
          lexProgress.setBaseColor(Color(255,0,0))
          lexProgress.setForegroundColor(Color(0,255,0))
          lexProgress.setWidth(450)
          lexProgress.setHeight(10)
          top.add(lexProgress,20+lexLabel.getWidth(),config["SCREEN_HEIGHT"]-25)

          notifyLabel.setVisible(False)
          heartLabel.setVisible(False)
          keyYellowLabel.setVisible(False)
          keyBlueLabel.setVisible(False)
          keyPinkLabel.setVisible(False)
          packageLabel.setVisible(False)
          heartIcon.setVisible(False)
          keyYellowIcon.setVisible(False)
          keyBlueIcon.setVisible(False)
          keyPinkIcon.setVisible(False)
          packageIcon.setVisible(False)
          dialogContainer.setVisible(False)
          splashLabel.setVisible(False)
          finLabel.setVisible(False)
          timeLabel.setVisible(False)
          lexLabel.setVisible(False)
          lexProgress.setVisible(False)

     def Stop(self, args=()):
          pass

     EventTable={ 'start': (Start, "splash"),
                  'stop': (Stop, None) }

def OnAction(action):
     id=action.getId()
     if id == "dialog":
          NextCutscene()

def Notify(caption):
     global notifyLabel, boss
     if boss == False or (boss==True and caption==""):
          notifyLabel.setCaption(caption)
          notifyLabel.setPosition((config["SCREEN_WIDTH"]/2)-(notifyLabel.getWidth()/2), config["VIEW_POSY"]+(config["VIEW_HEIGHT"]*TILEHEIGHT)+5)

notifyAlarm=-1
class ObjectListener(Listener):
     def __init__(self, room):
          self.room=room
          self.max_points=0
          if self.room != None:
               self.Reload()

     def Reload(self):
          self.max_points=0
          for i in self.room.objList:
               if i.name == "player":
                    i.AddSubscriber(self,MSG_ALL)
               if i.type.name == "door_yellow":
                    i.AddSubscriber(self,OBJECT)
               if i.type.name == "door_pink":
                    i.AddSubscriber(self,OBJECT)
               if i.type.name == "door_blue":
                    i.AddSubscriber(self,OBJECT)
               if i.type.name == "key_yellow":
                    i.AddSubscriber(self,OBJECT)
               if i.type.name == "key_blue":
                    i.AddSubscriber(self,OBJECT)
               if i.type.name == "key_pink":
                    i.AddSubscriber(self,OBJECT)
               if i.type.name == "package":
                    self.max_points=self.max_points+1

     def OnPlayerHit(self,message):
          global notifyAlarm
          heartLabel.setCaption(str(player.data["currentHP"]))

     def OnPlayerDied(self,message):
          global notifyAlarm, v
          Notify("Player died!")
          heartLabel.setCaption(str(player.data["currentHP"]))
          self.room.AddAlarm(self,150,3)
          if notifyAlarm == -1:
               notifyAlarm=self.room.AddAlarm(self,150,1)
          else:
               self.room.GetAlarmById(notifyAlarm).startFrame=main.frame

     """
     def OnPlayerScored(self,message):
          global notifyAlarm
          packageLabel.setCaption(str(player.data["score"])+" / "+str(self.max_points))
          if message.obj.data["score"] >= self.max_points:
               Notify("Got all the packages!")
               self.room.AddAlarm(self,150,2)
          else:
               Notify(str(self.max_points-message.obj.data["score"])+" package(s) left! Player score: "+str(message.obj.data["score"]))
               if notifyAlarm == -1:
                    notifyAlarm=self.room.AddAlarm(self,150,1)
               else:
                    self.room.GetAlarmById(notifyAlarm).startFrame=main.frame
     """

     def OnObjectLocked(self,message):
          global notifyAlarm
          Notify("Door locked!")
          if notifyAlarm == -1:
               notifyAlarm=self.room.AddAlarm(self,150,1)
          else:
               self.room.GetAlarmById(notifyAlarm).startFrame=main.frame

     def OnObjectOpened(self,message):
          global notifyAlarm
          o=self.room.GetObjectByName("player")
          Notify("Door unlocked!")
          keyYellowLabel.setCaption(str(player.data["key_yellow"]))
          keyPinkLabel.setCaption(str(player.data["key_pink"]))
          keyBlueLabel.setCaption(str(player.data["key_blue"]))
          if notifyAlarm == -1:
               notifyAlarm=self.room.AddAlarm(self,150,1)
          else:
               self.room.GetAlarmById(notifyAlarm).startFrame=main.frame

     def OnObjectCollision(self,message):
          global notifyAlarm
          if message.obj.type.name == "key_yellow":
               o=self.room.GetObjectByName("player")
               keyYellowLabel.setCaption(str(player.data["key_yellow"]))
          if message.obj.type.name == "key_pink":
               o=self.room.GetObjectByName("player")
               keyPinkLabel.setCaption(str(player.data["key_pink"]))
          if message.obj.type.name == "key_blue":
               o= self.room.GetObjectByName("player")
               keyBlueLabel.setCaption(str(player.data["key_blue"]))

     def OnAlarm(self,message):
          if message.data == 1:
               Notify("")
               global notifyAlarm
               notifyAlarm=-1
          #got all packages
          elif message.data == 2:
               pass
          elif message.data == 3:
               heartLabel.setCaption(str(player.data["currentHP"]))
          elif message.data == 4:
               NextCutscene()

def SetDialogue(args):
     global GuiImages
     if args[0] in GuiImages:
          dialogIcon.setVisible(True)
          dialogIcon.setImage(GuiImages[args[0]])
          dialogText.setPosition(89,10)
          dialogTitle.setCaption(args[1])
          dialogTitle.setVisible(True)
          dialogTitle.setPosition(47-(dialogTitle.getWidth()/2),80)
     else:
          dialogIcon.setVisible(False)
          dialogTitle.setVisible(False)
          dialogText.setPosition(15,10)

     dialogText.setText(FitText(args[2]))

def ScrollTo(args):
     global scrolling
     v.FocusToScroll(args[0],args[1])
     scrolling=True

def ScrollToPos(args):
     global scrolling
     v.ScrollTo(args[0],args[1],args[2])
     scrolling=True

def ScrollEnd(m):
     global scrolling, unpause, pause, pan
     if scrolling:
          NextCutscene()
          scrolling=False
     elif unpause:
          v.FocusTo(player.id)
          pan=False
          player.disabled=False
          pause=False
          finLabel.setVisible(False)
          unpause=False

def Wait(frames):
     room.AddAlarm(s.stateList["room"].oListen,frames,4)

def LoadCutscene(cslist,dialog=True):
     global cutsceneList, cutsceneIndex
     cutsceneList=cslist
     cutsceneIndex=0

     InitCutscene(dialog)
     PlayCutscene()

def InitCutscene(dialog=True):
     global cutscene, boss
     if cutscene: return None
     cutscene=True

     notifyLabel.setVisible(False)
     heartLabel.setVisible(False)
     keyYellowLabel.setVisible(False)
     keyBlueLabel.setVisible(False)
     keyPinkLabel.setVisible(False)
     packageLabel.setVisible(False)
     heartIcon.setVisible(False)
     keyYellowIcon.setVisible(False)
     keyBlueIcon.setVisible(False)
     keyPinkIcon.setVisible(False)
     packageIcon.setVisible(False)
     if boss:
          timeLabel.setVisible(False)
          lexLabel.setVisible(False)
          lexProgress.setVisible(False)

     player.disabled=True
     dialogContainer.setVisible(dialog)
     if dialog:
          v.ResetToMap(v.width,v.height-2)
          pygame.mouse.set_visible(True)

def PlayCutscene():
     global cutscene, cutsceneList, cutsceneIndex
     if cutscene:
          #call cutscene func with args
          cutsceneList[cutsceneIndex][0](cutsceneList[cutsceneIndex][1])
          #don't wait for NextCutscene event
          if cutsceneList[cutsceneIndex][2] == 0:
               NextCutscene()

def NextCutscene():
     global cutscene, cutsceneList, cutsceneIndex
     if cutscene:
          cutsceneIndex+=1
          if cutsceneIndex >= len(cutsceneList):
               StopCutscene()
          else:
               PlayCutscene()

def StopCutscene():
     global cutscene, cutsceneList, cutsceneIndex, boss
     cutscene=False
     cutsceneList=[]
     cutsceneIndex=-1

     notifyLabel.setVisible(True)
     heartLabel.setVisible(True)
     keyYellowLabel.setVisible(True)
     keyBlueLabel.setVisible(True)
     keyPinkLabel.setVisible(True)
     packageLabel.setVisible(True)
     heartIcon.setVisible(True)
     keyYellowIcon.setVisible(True)
     keyBlueIcon.setVisible(True)
     keyPinkIcon.setVisible(True)
     packageIcon.setVisible(True)
     if boss:
          timeLabel.setVisible(True)
          lexLabel.setVisible(True)
          lexProgress.setVisible(True)

     player.disabled=False
     if dialogContainer.isVisible():
          v.ResetToMap(v.width,v.height+2)
          dialogContainer.setVisible(False)
          pygame.mouse.set_visible(False)

     dialogIcon.setVisible(False)
     dialogTitle.setVisible(False)
     dialogText.setText("")

def PlayMusic(music):
     if room.database.ItemExists(MUSIC,music):
          pygame.mixer.music.load(room.database[MUSIC][music])
          pygame.mixer.music.play(-1)

def StopMusic(fade=2000):
     pygame.mixer.music.fadeout(fade)

class RoomState(State):
     def __init__(self):
          global room
          State.__init__(self,"room",RoomState.EventTable)
          self.level=0
          self.oListen=ObjectListener(room)
          #0 = Initialize, 1 = Normal, 2 = Stop
          self.status=0

     def OnViewFadeEnd(self,message):
          #fading in
          if self.status == 0 or self.status == 1:
               player.disabled=False
               global notifyLabel, keyYellowLabel, keyBlueLabel, keyPinkLabel, packageLabel, lexLabel, lexProgress, boss
               notifyLabel.setVisible(True)
               heartLabel.setVisible(True)
               keyYellowLabel.setVisible(True)
               keyBlueLabel.setVisible(True)
               keyPinkLabel.setVisible(True)
               packageLabel.setVisible(True)
               heartIcon.setVisible(True)
               keyYellowIcon.setVisible(True)
               keyBlueIcon.setVisible(True)
               keyPinkIcon.setVisible(True)
               packageIcon.setVisible(True)
               execfile(os.path.join(CURRENTLEVELDIR,"level.py"))
               if boss:
                    lexLabel.setVisible(True)
                    lexProgress.setVisible(True)

          #fading out
          elif self.status == 2:
               pause=False
               s.OnMessage("reloadlevel")
          elif self.status == 3:
               self.stop=True
          elif self.status == 4:
               s.OnMessage("tosplash")

     def Start(self, args=()):
          self.status=0
          global CURRENTLEVELDIR
          CURRENTLEVELDIR=os.path.join(LEVELDIR,config["LEVELS"][self.level])
          global pause, boss
          pause=False
          boss=False

          global player
          room.RemoveAll()
          room.map.Load(os.path.join(CURRENTLEVELDIR,"map.txt"))
          room.LoadObjects(os.path.join(CURRENTLEVELDIR,"object.txt"))

          global v
          if v == None:
               v=RoomView(room,config["VIEW_WIDTH"],config["VIEW_HEIGHT"])
               v.SetPosition(config["VIEW_POSX"],config["VIEW_POSY"])
          else:
               v.ResetToMap()

          v.FocusTo(room.GetObjectIdByName("player"))
          player=room.GetObjectByName("player")
          v.AddSubscriber(self,VIEW_FADEEND)
          v.FadeIn(60)
          player.disabled=True

          l=Listener(ScrollEnd)
          v.AddSubscriber(l,VIEW_SCROLLEND)

          #put player at bottom
          room.MoveObjectIndex(player.id,len(room.objList))

          self.oListen.room=room
          self.oListen.Reload()

          heartLabel.setCaption(str(player.data["currentHP"]))
          keyYellowLabel.setCaption(str(player.data["key_yellow"]))
          keyBlueLabel.setCaption(str(player.data["key_blue"]))
          keyPinkLabel.setCaption(str(player.data["key_pink"]))
          packageLabel.setCaption("Plasma Gun")

          self.status=1
          Notify("")

          ctrl=room.GetControllerByObj(player)
          ctrl.keyLeft=K_a
          ctrl.keyRight=K_d
          ctrl.keyUp=K_w
          ctrl.keyDown=K_s

          global reload, gun
          reload=0
          gun=0

     def NextLevel(self, args=()):
          l=self.level
          self.level+=1
          if self.level>len(config["LEVELS"])-1:
               self.status=3
               pause=True
               v.FadeOut(90)
               notifyLabel.setVisible(False)
               heartLabel.setVisible(False)
               keyYellowLabel.setVisible(False)
               keyBlueLabel.setVisible(False)
               keyPinkLabel.setVisible(False)
               packageLabel.setVisible(False)
               heartIcon.setVisible(False)
               keyYellowIcon.setVisible(False)
               keyBlueIcon.setVisible(False)
               keyPinkIcon.setVisible(False)
               packageIcon.setVisible(False)
               timeLabel.setVisible(False)
               lexLabel.setVisible(False)
               lexProgress.setVisible(False)
          else:
               global CURRENTLEVELDIR, room
               CURRENTLEVELDIR=os.path.join(LEVELDIR,config["LEVELS"][self.level])

               if l != self.level:
                    self.ReloadLevel()

     def PrevLevel(self, args=()):
          l=self.level
          self.level-=1
          if self.level < 0:
               self.status=4
               pause=True
               v.FadeOut(90)
               notifyLabel.setVisible(False)
               heartLabel.setVisible(False)
               keyYellowLabel.setVisible(False)
               keyBlueLabel.setVisible(False)
               keyPinkLabel.setVisible(False)
               packageLabel.setVisible(False)
               heartIcon.setVisible(False)
               keyYellowIcon.setVisible(False)
               keyBlueIcon.setVisible(False)
               keyPinkIcon.setVisible(False)
               packageIcon.setVisible(False)
               timeLabel.setVisible(False)
               lexLabel.setVisible(False)
               lexProgress.setVisible(False)
          else:
               global CURRENTLEVELDIR
               CURRENTLEVELDIR=os.path.join(LEVELDIR,config["LEVELS"][self.level])

               if l != self.level:
                    self.ReloadLevel()

     def ReturnToSplash(self,m):
          pass

     def ReloadLevel(self, args=()):
          global pause
          self.status=2
          pause=True
          v.FadeOut(90)
          notifyLabel.setVisible(False)
          heartLabel.setVisible(False)
          keyYellowLabel.setVisible(False)
          keyBlueLabel.setVisible(False)
          keyPinkLabel.setVisible(False)
          packageLabel.setVisible(False)
          heartIcon.setVisible(False)
          keyYellowIcon.setVisible(False)
          keyBlueIcon.setVisible(False)
          keyPinkIcon.setVisible(False)
          packageIcon.setVisible(False)
          timeLabel.setVisible(False)
          lexLabel.setVisible(False)
          lexProgress.setVisible(False)

     def Update(self, args=()):
          global done, pause, cutscene, pan, pAngle, gravGun, gAngle, reload, gun
          particle=room.particle
          clock.tick(30)
          room.key=pygame.key.get_pressed()
          room.mouse=pygame.mouse.get_pressed()
          for event in pygame.event.get():
               if event.type == QUIT:
                    done=True
               elif event.type == MOUSEMOTION:
                    if pause == False and cutscene == False:
                         a=(event.pos[0]-v.posX+v.camX)-(player.posX+(player.width/2))
                         b=player.posY-(event.pos[1]-v.posY+v.camY)
                         #find unit vector (||v||cos(t)i, ||v||sin(t)jd), solve for theta
                         magnitude=math.sqrt((a**2)+(b**2))
                         magnitude=0.01 if magnitude == 0.0 else magnitude
                         unitcos=float(a)/float(magnitude)
                         angle=int(math.degrees(math.acos(unitcos)))
                         if b < 0:
                              angle=360-angle

                         angle=0 if angle>=360 else angle
                         player.sprite.SetAnimation(int(angle/11.25))

                         v.SetOffFocus(a/config["OFFSET_FACTOR"],-b/config["OFFSET_FACTOR"])

               elif event.type == MOUSEBUTTONDOWN:
                    if event.button==1 and pause == False and cutscene == False and player.disabled == False \
                    and reload == 0 and gun == 0:
                         a=(event.pos[0]-v.posX+v.camX)-(player.posX+(player.width/2))
                         b=player.posY-(event.pos[1]-v.posY+v.camY)+player.height/2
                         #find unit vector (||v||cos(t)i, ||v||sin(t)jd), solve for theta
                         magnitude=math.sqrt((a**2)+(b**2))
                         magnitude=0.01 if magnitude == 0.0 else magnitude
                         unitcos=float(a)/float(magnitude)
                         angle=int(math.degrees(math.acos(unitcos)))
                         if b < 0:
                              angle=360-angle

                         angle=0 if angle>=360 else angle
                         player.sprite.SetFrame(int(angle/11.25))

                         objID=room.AddObject("bullet",(player.posX+player.width/2)+(40*cos[angle]),(player.posY+player.width/2)-(40*sin[angle]))
                         obj=room.GetObjectById(objID)
                         room.GetControllerById(obj.ctrl).color=2
                         obj.velY=-obj.type.maxVelY*sin[angle]
                         obj.velX=obj.type.maxVelX*cos[angle]
                         player.velY=SetBound(player.velY+sin[angle]*config["GUNRECOIL_X"],-player.maxVelY,player.maxVelY)
                         player.velX=SetBound(player.velX-cos[angle]*config["GUNRECOIL_Y"],-player.maxVelX,player.maxVelX)

                         reload=config["RELOAD_TIME"]
                         room.PlaySound("sound68")

                    elif event.button==1 and pause == False and cutscene == False and gun == 1:
                         if gravGun==None:
                              gravGun=room.GetObjectByPos(event.pos[0]-v.posX+v.camX,event.pos[1]-v.posY+v.camY)
                              if gravGun != None:
                                   if gravGun.type.name=="crate" or gravGun.type.name=="key_yellow" or gravGun.type.name=="key_blue" \
                                   or gravGun.type.name=="key_pink" or gravGun.type.name=="package":
                                        gravGun.fall=False
                                        gravGun.jump=True
                                        gAngle=0
                                        player.disabled=True
                                        room.PlaySound("sound62")
                                        if gravGun.type.name=="key_yellow" or gravGun.type.name=="key_blue" \
                                        or gravGun.type.name=="key_pink" or gravGun.type.name=="package":
                                             ctrl=room.GetControllerByObj(gravGun)
                                             ctrl.grav=True

                                   else:
                                        gravGun=None
                         else:
                              gravGun.velX=0.0
                              gravGun.velY=0.0
                              if gravGun.type.fall: gravGun.fall=True
                              if gravGun.type.name=="key_yellow" or gravGun.type.name=="key_blue" \
                              or gravGun.type.name=="key_pink" or gravGun.type.name=="package":
                                   ctrl=room.GetControllerByObj(gravGun)
                                   ctrl.grav=False

                              gravGun=None
                              player.disabled=False

                    elif event.button==3 and pause == False and cutscene == False and player.disabled == False:
                         room.AddObject("crate",event.pos[0]-v.posX+v.camX,event.pos[1]-v.posY+v.camY)

               elif event.type == KEYDOWN:
                    if event.key == K_F1 and cutscene == False:
                         self.PrevLevel()

                    if event.key == K_F2 and cutscene == False:
                         self.ReloadLevel()
                    if event.key == K_F3 and cutscene == False:
                         self.NextLevel()

                    if room.key[K_SPACE] and pan and unpause == False:
                         pos=pygame.mouse.get_pos()
                         if pos[0] <= v.posX+(v.width*TILEWIDTH) and pos[1] <= v.posY+(v.height*TILEHEIGHT):
                              v.ScrollTo(v.camX+(pos[0]-v.posX)-(v.width*TILEWIDTH/2), v.camY+(pos[1]-v.posY)-(v.height*TILEHEIGHT/2), 20)
                              room.particle.AddParticle("circle4",v.camX+(pos[0]-v.posX),v.camY+(pos[1]-v.posY),0,0,3.0,-0.05)

                    if event.key == K_TAB and cutscene == False and pause == False and gravGun == None:
                         gun=0 if gun==1 else 1
                         if gun==0:
                              packageLabel.setCaption("Plasma Gun")
                         elif gun==1:
                              packageLabel.setCaption("Gravity Gun")

                    if room.key[K_LEFT] and pan and unpause == False:
                         v.SetCamPosition(v.camX-10,v.camY)

                    if room.key[K_RIGHT] and pan and unpause == False:
                         v.SetCamPosition(v.camX+10,v.camY)

                    if room.key[K_DOWN] and pan and unpause == False:
                         v.SetCamPosition(v.camX,v.camY+10)

                    if room.key[K_UP] and pan and unpause == False:
                         v.SetCamPosition(v.camX,v.camY-10)

                    if event.key == K_ESCAPE:
                         global pause, unpause
                         if pause:
                              v.FocusToScroll(player.id,30)
                              unpause=True
                         else:
                              v.FocusTo(-1)
                              pan=True
                              player.disabled=True
                              pause=True
                              finLabel.setVisible(True)
                              finLabel.setCaption("P A U S E")
                              finLabel.setPosition((config["SCREEN_WIDTH"]/2)-(finLabel.getWidth()/2),(config["SCREEN_HEIGHT"]/2)-(finLabel.getHeight()/2))

               inputMessage.ChangeEvent(event)
               room.BroadcastMessage(inputMessage)
               input.pushInput(event)
               gui.logic()

          #Draw Everything
          if pause==False:
               room.UpdateControllers()
               room.Logic()
          else:
               room.particle.Update()

          screen.fill((0,0,0))
          v.Draw(screen)
          gui.draw()

          if gravGun != None:
               pos=pygame.mouse.get_pos()
               velX=SetBound((pos[0]-v.posX+v.camX-gravGun.width/2)-gravGun.posX,-gravGun.maxVelX,gravGun.maxVelX)
               velY=SetBound((pos[1]-v.posY+v.camY-gravGun.height/2)-gravGun.posY,-gravGun.maxVelY,gravGun.maxVelY)

               a=(player.posX+player.width/2)-(gravGun.posX+(gravGun.width/2))
               b=(player.posY+player.height/2)-(gravGun.posY+gravGun.height/2)
               #find unit vector (||v||cos(t)i, ||v||sin(t)jd), solve for theta
               magnitude=math.sqrt((a**2)+(b**2))
               magnitude=0.01 if magnitude == 0.0 else magnitude
               unitcos=float(a)/float(magnitude)
               angle=int(math.degrees(math.acos(unitcos)))
               if b < 0: angle=360-angle
               angle=0 if angle>=360 else angle

               screen.set_clip(v.posX,v.posY,v.width*TILEWIDTH,v.height*TILEHEIGHT)
               #pygame.gfxdraw.line(screen, int((player.posX+player.width/2-v.camX+v.posX)-25*cos[angle]), int((player.posY+player.height/2-v.camY+v.posY)-25*sin[angle]), int((gravGun.posX-v.camX+v.posX)+gravGun.width/2), int((gravGun.posY-v.camY+v.posY)+gravGun.height/2), (0,255,255))
               pygame.gfxdraw.circle(screen,int((player.posX+player.width/2-v.camX+v.posX)-(7*magnitude/8)*cos[angle]), int((player.posY+player.height/2-v.camY+v.posY)-(7*magnitude/8)*sin[angle]), 8, (0,255,100))
               pygame.gfxdraw.circle(screen,int((player.posX+player.width/2-v.camX+v.posX)-(3*magnitude/4)*cos[angle]), int((player.posY+player.height/2-v.camY+v.posY)-(3*magnitude/4)*sin[angle]), 7, (0,255,100))
               pygame.gfxdraw.circle(screen,int((player.posX+player.width/2-v.camX+v.posX)-(5*magnitude/8)*cos[angle]), int((player.posY+player.height/2-v.camY+v.posY)-(5*magnitude/8)*sin[angle]), 6, (0,255,100))
               pygame.gfxdraw.circle(screen,int((player.posX+player.width/2-v.camX+v.posX)-(magnitude/2)*cos[angle]), int((player.posY+player.height/2-v.camY+v.posY)-(magnitude/2)*sin[angle]), 5, (0,255,100))
               pygame.gfxdraw.circle(screen,int((player.posX+player.width/2-v.camX+v.posX)-(3*magnitude/8)*cos[angle]), int((player.posY+player.height/2-v.camY+v.posY)-(3*magnitude/8)*sin[angle]), 4, (0,255,100))
               pygame.gfxdraw.circle(screen,int((player.posX+player.width/2-v.camX+v.posX)-(magnitude/4)*cos[angle]), int((player.posY+player.height/2-v.camY+v.posY)-(magnitude/4)*sin[angle]), 3, (0,255,100))
               pygame.gfxdraw.circle(screen,int((player.posX+player.width/2-v.camX+v.posX)-(magnitude/8)*cos[angle]), int((player.posY+player.height/2-v.camY+v.posY)-(magnitude/8)*sin[angle]), 2, (0,255,100))
               #pygame.gfxdraw.circle(screen,int((gravGun.posX-v.camX+v.posX)+gravGun.width/2-gravGun.width*cos[gAngle]), int((gravGun.posY-v.camY+v.posY)+gravGun.height/2-gravGun.width*sin[gAngle]), gravGun.width/16, (0,255,100))

               gAngle=gAngle+15 if gAngle+15 < 360 else 0
               gAngle2=gAngle+90 if gAngle+90 < 360 else gAngle-270
               gAngle3=gAngle+180 if gAngle+180 < 360 else gAngle-180
               gAngle4=gAngle-90 if gAngle-90 >= 0 else gAngle+270

               room.particle.AddParticle("circle7",int((gravGun.posX)+gravGun.width/2-gravGun.width*cos[gAngle]), int((gravGun.posY)+gravGun.height/2-gravGun.width*sin[gAngle]), 0,0,3.0,-0.01,5)
               room.particle.AddParticle("circle7",int((gravGun.posX)+gravGun.width/2-gravGun.width*cos[gAngle2]), int((gravGun.posY)+gravGun.height/2-gravGun.width*sin[gAngle2]), 0,0,3.0,-0.01,5)
               room.particle.AddParticle("circle7",int((gravGun.posX)+gravGun.width/2-gravGun.width*cos[gAngle3]), int((gravGun.posY)+gravGun.height/2-gravGun.width*sin[gAngle3]), 0,0,3.0,-0.01,5)
               room.particle.AddParticle("circle7",int((gravGun.posX)+gravGun.width/2-gravGun.width*cos[gAngle4]), int((gravGun.posY)+gravGun.height/2-gravGun.width*sin[gAngle4]), 0,0,3.0,-0.01,5)
               screen.set_clip(None)

               if velY < 0: gravGun.jump=True

               if pause == False:
                    room.MoveObject(gravGun.id,velX,0)
                    room.MoveObject(gravGun.id,0,velY)

          screen.set_clip(v.posX,v.posY,v.width*TILEWIDTH,v.height*TILEHEIGHT)
          pos=pygame.mouse.get_pos()
          if gun == 0 and cutscene == False and pause == False:
               img=room.database[IMAGE]["plasma_cursor"]
               screen.blit(img,(pos[0]-img.get_width()/2,pos[1]-img.get_height()/2))
          elif gun == 1 and cutscene == False and pause == False:
               img=room.database[IMAGE]["grav_cursor"]
               screen.blit(img,(pos[0]-img.get_width()/2,pos[1]-img.get_height()/2))
          screen.set_clip(None)

          if reload > 0: reload-=1

          pygame.display.flip()
          main.total+=clock.get_fps()
          main.frame+=1

     def Stop(self, args=()):
          self.status=0
          #print "FPS:", main.total/main.frame, "Objects: ", len(room.objList), "Controllers:", len(room.controllerList), "Alarms:", len(room.alarmList)
          notifyLabel.setVisible(False)
          heartLabel.setVisible(False)
          keyYellowLabel.setVisible(False)
          keyBlueLabel.setVisible(False)
          keyPinkLabel.setVisible(False)
          packageLabel.setVisible(False)
          heartIcon.setVisible(False)
          keyYellowIcon.setVisible(False)
          keyBlueIcon.setVisible(False)
          keyPinkIcon.setVisible(False)
          packageIcon.setVisible(False)
          timeLabel.setVisible(False)
          lexLabel.setVisible(False)
          lexProgress.setVisible(False)
          dialogContainer.setVisible(False)
          room.RemoveAll()
          StopMusic()

     EventTable={ 'start': (Start, None),
                  'update': (Update, None),
                  'stop': (Stop, "end"),
                  'tosplash': (ReturnToSplash, "splash"),
                  'reloadlevel': (ReloadLevel, "room") }

class SplashState(State):
     def __init__(self):
          State.__init__(self,"splash",SplashState.EventTable)
          self.dialogueList=None
          self.dialogueIndex=-1

     def Start(self, args=()):
          splashLabel.setVisible(True)
          self.dialogueList=config["SPLASH_DIALOGUE"]
          if len(self.dialogueList) > 0:
               self.dialogueIndex=0
               splashLabel.setCaption(self.dialogueList[self.dialogueIndex])

          PlayMusic("splash")

     def Update(self, args=()):
          global done, pause
          clock.tick(30)
          room.key=pygame.key.get_pressed()
          room.mouse=pygame.mouse.get_pressed()
          for event in pygame.event.get():
               if event.type == QUIT:
                    done=True
               elif event.type == KEYDOWN:
                    self.dialogueIndex+=1
                    if self.dialogueIndex >= len(self.dialogueList):
                         self.stop=True
                    else:
                         splashLabel.setCaption(self.dialogueList[self.dialogueIndex])

               input.pushInput(event)
               gui.logic()

          screen.fill((0,0,0))
          gui.draw()
          pygame.display.flip()

     def Stop(self, args=()):
          splashLabel.setVisible(False)
          StopMusic()
          s.stateList["room"].level=0

     EventTable={ 'start': (Start, None),
                  'update': (Update, None),
                  'stop': (Stop, "room") }

class EndState(State):
     def __init__(self):
          State.__init__(self,"end",EndState.EventTable)
          self.dialogueList=None
          self.dialogueIndex=-1

     def Start(self, args=()):
          splashLabel.setVisible(True)
          self.dialogueList=config["END_DIALOGUE"]
          if len(self.dialogueList) > 0:
               self.dialogueIndex=0
               splashLabel.setCaption(self.dialogueList[self.dialogueIndex])

          PlayMusic("end")
          self.back=False

     def Update(self, args=()):
          global done, pause
          clock.tick(30)
          room.key=pygame.key.get_pressed()
          room.mouse=pygame.mouse.get_pressed()
          for event in pygame.event.get():
               if event.type == QUIT:
                    done=True
               elif event.type == KEYDOWN:
                    if event.key == K_F1 and self.back:
                         s.OnMessage("back")
                    if event.key == K_F2 and self.back:
                         s.OnMessage("stop")

                    self.dialogueIndex+=1
                    if self.dialogueIndex >= len(self.dialogueList) and self.back != True:
                         global finLabel
                         splashLabel.setCaption("")
                         finLabel.setCaption("F i n")
                         finLabel.setPosition((config["SCREEN_WIDTH"]/2)-(finLabel.getWidth()/2),(config["SCREEN_HEIGHT"]/2)-(finLabel.getHeight()/2))
                         finLabel.setVisible(True)
                         self.back=True
                    elif self.dialogueIndex < len(self.dialogueList):
                         splashLabel.setCaption(self.dialogueList[self.dialogueIndex])

               input.pushInput(event)
               gui.logic()

          screen.fill((0,0,0))
          gui.draw()
          pygame.display.flip()

     def Stop(self, args=()):
          global finLabel
          splashLabel.setVisible(False)
          finLabel.setVisible(False)
          StopMusic()

     def Back(self, args=()):
          global finLabel
          finLabel.setCaption("")
          splashLabel.setVisible(False)
          finLabel.setVisible(False)
          StopMusic()
          s.stateList["room"].level=len(config["LEVELS"])-1

     EventTable={ 'start': (Start, None),
                  'update': (Update, None),
                  'back': (Back, "room"),
                  'stop': (Stop, "end") }

def mainFunc():
     global s
     s=StateMachine()
     s.AddState(InitState())
     s.AddState(SplashState())
     s.AddState(RoomState())
     s.AddState(EndState())
     s.startState="init"
     s.Start()

     while done == False:
          s.Update()

     s.Stop()


#this calls the 'main' function when this script is executed
#if __name__ == '__main__': profile.run("mainFunc()","profile.txt")
#s=pstats.Stats(BASEDIR+"\profile.txt")
#s.sort_stats("cumulative")
#s.print_stats()
if __name__ == '__main__': mainFunc()
"""
m=MapData()
m.tileset.Load("templates2.tmp")
m.tileset.SetColorKey(Color(255,0,255))
m.CreateTileTemplate("SP",0,True,False,False,False,-1.0)
m.CreateTileTemplate("SP_VT",1,True,False,False,False,-1.0)
m.CreateTileTemplate("SP_HZ",2,True,False,False,False,-1.0)
m.CreateTileTemplate("SP_TL",3,True,False,False,False,-1.0)
m.CreateTileTemplate("SP_BL",4,True,False,False,False,-1.0)
m.CreateTileTemplate("SP_TR",5,True,False,False,False,-1.0)
m.CreateTileTemplate("SP_BR",6,True,False,False,False,-1.0)
m.CreateTileTemplate("SP_TLBR",7,True,False,False,False,-1.0)
m.CreateTileTemplate("SP_TRBL",8,True,False,False,False,-1.0)
m.CreateTileTemplate("SP_VT_TE",9,True,False,False,False,-1.0)
m.CreateTileTemplate("SP_VT_BE",10,True,False,False,False,-1.0)
m.CreateTileTemplate("SP_HZ_LE",11,True,False,False,False,-1.0)
m.CreateTileTemplate("SP_HZ_RE",12,True,False,False,False,-1.0)
m.CreateTileTemplate("SP_BL_E",13,True,False,False,False,-1.0)
m.CreateTileTemplate("SP_TL_E",14,True,False,False,False,-1.0)
m.CreateTileTemplate("SP_BR_E",15,True,False,False,False,-1.0)
m.CreateTileTemplate("SP_TR_E",16,True,False,False,False,-1.0)
m.CreateTileTemplate("SP_TLBR_EE",17,True,False,False,False,-1.0)
m.CreateTileTemplate("SP_TRBL_EE",18,True,False,False,False,-1.0)
m.CreateTileTemplate("SP_TLBR_BE",19,True,False,False,False,-1.0)
m.CreateTileTemplate("SP_TLBR_TE",20,True,False,False,False,-1.0)
m.CreateTileTemplate("SP_TRBL_TE",21,True,False,False,False,-1.0)
m.CreateTileTemplate("SP_TRBL_BE",22,True,False,False,False,-1.0)
m.CreateTileTemplate("BL_MI",23,False,False,False,False,1.0)
m.CreateTileTemplate("BL_TP",24,False,False,False,False,1.0)
m.CreateTileTemplate("BL_BM",25,False,False,False,False,1.0)
m.CreateTileTemplate("BL_RT",26,False,False,False,False,1.0)
m.CreateTileTemplate("BL_LT",27,False,False,False,False,1.0)
m.CreateTileTemplate("BL_TR",28,False,False,False,False,1.0)
m.CreateTileTemplate("BL_BR",29,False,False,False,False,1.0)
m.CreateTileTemplate("BL_TL",30,False,False,False,False,1.0)
m.CreateTileTemplate("BL_BL",31,False,False,False,False,1.0)
m.CreateTileTemplate("BL_IC_TP",32,False,False,False,False,0.0)
m.CreateTileTemplate("BL_IC_TR",33,False,False,False,False,0.0)
m.CreateTileTemplate("BL_IC_TL",34,False,False,False,False,0.0)
m.CreateTileTemplate("BL_MI_GR",35,False,False,False,False,1.0)
m.CreateTileTemplate("BL_MI_GL",36,False,False,False,False,1.0)
m.CreateTileTemplate("BL_TP_GR",37,False,False,False,False,1.0)
m.CreateTileTemplate("BL_BM_GR",38,False,False,False,False,1.0)
m.CreateTileTemplate("BL_TP_GL",39,False,False,False,False,1.0)
m.CreateTileTemplate("BL_BM_GL",40,False,False,False,False,1.0)
m.CreateTileTemplate("GN_MI",41,False,False,False,False,1.0)
m.CreateTileTemplate("GN_TP",42,False,False,False,False,1.0)
m.CreateTileTemplate("GN_BM",43,False,False,False,False,1.0)
m.CreateTileTemplate("GN_RT",44,False,False,False,False,1.0)
m.CreateTileTemplate("GN_LT",45,False,False,False,False,1.0)
m.CreateTileTemplate("GN_TR",46,False,False,False,False,1.0)
m.CreateTileTemplate("GN_BR",47,False,False,False,False,1.0)
m.CreateTileTemplate("GN_TL",48,False,False,False,False,1.0)
m.CreateTileTemplate("GN_BL",49,False,False,False,False,1.0)
m.CreateTileTemplate("GN_IC_TP",50,False,False,False,False,0.0)
m.CreateTileTemplate("GN_IC_TR",51,False,False,False,False,0.0)
m.CreateTileTemplate("GN_IC_TL",52,False,False,False,False,0.0)
m.CreateTileTemplate("SP_INV",53,True,False,False,False,-1.0)
m.SaveTemplates("templates2x.tmp")
"""
"""
spr=Sprite()
spr.CreateFromFile("heroangle3.bmp","player",32,32)
spr.SetColorKey(Color(255,0,255))
o=ObjectType("player")
o.Load("player.obj")
o.sprite=spr
o.Save("player.obj")
"""