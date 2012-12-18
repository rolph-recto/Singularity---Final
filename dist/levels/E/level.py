#!/usr/bin/env python
#LEVEL FIVE - BOSS

l=None
sp=room.map.GetTemplateIdByName("SP")
bl_lt=room.map.GetTemplateIdByName("GN_LT")
bl_rt=room.map.GetTemplateIdByName("GN_RT")
bl_bm=room.map.GetTemplateIdByName("GN_BM")
bl_mi=room.map.GetTemplateIdByName("GN_MI")
bl_tr=room.map.GetTemplateIdByName("GN_TR")
bl_tl=room.map.GetTemplateIdByName("GN_TL")
bl_br=room.map.GetTemplateIdByName("GN_BR")
bl_bl=room.map.GetTemplateIdByName("GN_BL")
bl_tp=room.map.GetTemplateIdByName("GN_TP")
lex=room.GetObjectByName("lex")

def SwitchLexSide(s,o):
     global sp, bl_lt, bl_rt, bl_bm, bl_mi, bl_tr, bl_tl, bl_br, bl_bl, bl_tp
     #left
     if s==0:
          for y in range(8):
                    if o==0:
                         room.map.base[33][33+y]=sp
                         room.map.base[34][33+y]=sp
                         room.map.base[32][33+y]=sp
                    else:
                         room.map.base[32][33+y]=bl_lt
                         room.map.base[33][33+y]=bl_mi
                         room.map.base[34][33+y]=bl_mi
          if o==0:
               room.map.base[32][32]=sp
               room.map.base[33][32]=sp
               room.map.base[34][32]=sp
               room.map.base[32][41]=sp
               room.map.base[33][41]=sp
               room.map.base[34][41]=sp
          else:
               room.map.base[32][32]=bl_tl
               room.map.base[33][32]=bl_tp
               room.map.base[34][32]=bl_tp
               room.map.base[32][41]=bl_bl
               room.map.base[33][41]=bl_bm
               room.map.base[34][41]=bl_bm
          
     #bottom                    
     elif s==1:
          for x in range(8):
               if o==0:
                    room.map.base[33+x][39]=sp
                    room.map.base[33+x][40]=sp
                    room.map.base[33+x][41]=sp
               else:
                    room.map.base[33+x][39]=bl_mi
                    room.map.base[33+x][40]=bl_mi
                    room.map.base[33+x][41]=bl_bm
          if o==0:
               room.map.base[32][39]=sp
               room.map.base[32][40]=sp
               room.map.base[32][41]=sp
               room.map.base[41][39]=sp
               room.map.base[41][40]=sp
               room.map.base[41][41]=sp
          else:
               room.map.base[32][39]=bl_lt
               room.map.base[32][40]=bl_lt
               room.map.base[32][41]=bl_bl
               room.map.base[41][39]=bl_rt
               room.map.base[41][40]=bl_rt
               room.map.base[41][41]=bl_br

                    
     #right
     elif s==2:
          for y in range(8):
                    if o==0:
                         room.map.base[39][33+y]=sp
                         room.map.base[40][33+y]=sp
                         room.map.base[41][33+y]=sp
                    else:
                         room.map.base[39][33+y]=bl_mi
                         room.map.base[40][33+y]=bl_mi
                         room.map.base[41][33+y]=bl_rt
          if o==0:
               room.map.base[39][32]=sp
               room.map.base[40][32]=sp
               room.map.base[41][32]=sp
               room.map.base[39][41]=sp
               room.map.base[40][41]=sp
               room.map.base[41][41]=sp
          else:
               room.map.base[39][32]=bl_tp
               room.map.base[40][32]=bl_tp
               room.map.base[41][32]=bl_tr
               room.map.base[39][41]=bl_bm
               room.map.base[40][41]=bl_bm
               room.map.base[41][41]=bl_br
               
                         
lexSide=0
lexProtected=True
lexHitCount=0
def SwitchLex(s):
     global SwitchLexSide, lexSide, lexProtected
     #use lexSide
     if s==-1:
          s=lexSide
     #left
     if s==0:
          SwitchLexSide(1,1)
          SwitchLexSide(2,1)
          SwitchLexSide(0,0)
          lexProtected=False
     #bottom
     elif s==1:
          SwitchLexSide(0,1)
          SwitchLexSide(2,1) 
          SwitchLexSide(1,0)
          lexProtected=False
     #right
     elif s==2:
          SwitchLexSide(0,1)
          SwitchLexSide(1,1)
          SwitchLexSide(2,0)
          lexProtected=False
     #none
     elif s==3:
          SwitchLexSide(0,1)
          SwitchLexSide(1,1)
          SwitchLexSide(2,1)
          lexProtected=True
          
          
def ProgressLexSide(arg):
     global lexSide
     lexSide=lexSide+1 if lexSide+1 <= 2 else 0
     
frameIter=0
frameEnd=18000
timerAlarm=-1

def StartTimer(args=()):
     global timeLabel, room, frameIter, timerAlarm, l2
     timeLabel.setVisible(True)
     timerAlarm=room.AddAlarm(l2,1,None,-1)
     frameIter=0
     
def Timer(m):
     global timeLabel, pause, frameIter, frameEnd, timerAlarm, StopTimer
     if pause==False:
          frameIter+=1
          rawsec=(frameEnd-frameIter)/30
          min=int(rawsec/60)
          sec=int(rawsec%60)
          if sec > 9:
               timeLabel.setCaption(str(min)+":"+str(sec))
          else:timeLabel.setCaption(str(min)+":0"+str(sec))
          
          if frameIter >= frameEnd:
               StopTimer()
               
def StopTimer(reload=True):
     global cs3
     room.RemoveAlarm(timerAlarm)
     timeLabel.setVisible(False)
     if reload:
          LoadCutscene(cs3)
     
cs1=[]
cs1.append( (v.FocusTo, -1, 0) )
cs1.append( (ScrollTo, (room.GetObjectByName("lex").id, 60), 1) )
cs1.append( (Wait, 10, 1) )
cs1.append( (SwitchLex, -1, 0) )
cs1.append( (Wait, 30, 1) )
cs1.append( (ScrollTo, (player.id, 60), 1) )
cs1.append( (v.FocusTo, player.id, 0) )
cs1.append( (ProgressLexSide, None, 0) )

cs2=[]
cs2.append( (v.FocusTo, -1, 0) )
cs2.append( (SetDialogue, ("","","Project Genesis\nLog #5 - 10/29/2016"), 1) )
cs2.append( (SetDialogue, ("","","Last Entry."), 1) )
cs2.append( (SetDialogue, ("","","The test results came in. They're gone."), 1) )
cs2.append( (SetDialogue, ("","","Absolutely gone."), 1) )
cs2.append( (SetDialogue, ("","","Scanner cannot trace any agents in the server."), 1) )
cs2.append( (SetDialogue, ("","","...Our fatal mistake was not keeping the server isolated."), 1) )
cs2.append( (SetDialogue, ("","","But I don't understand..."), 1) )
cs2.append( (SetDialogue, ("","","There is no code for the agents to exit..."), 1) )
cs2.append( (SetDialogue, ("","","Let alone disobey a terminate command."), 1) )
cs2.append( (SetDialogue, ("","","Then again there were a lot of unexpected things."), 1) )
cs2.append( (SetDialogue, ("","","So...Singularity failed. Project Genesis will be scrapped."), 1) )
cs2.append( (SetDialogue, ("","","Eventually, maybe a couple years or so, the agents will break down..."), 1) )
cs2.append( (SetDialogue, ("","","Be destroyed by an anti-virus somewhere...I hope."), 1) )
cs2.append( (SetDialogue, ("lex","Lex","Why are you two still here!"), 1) )
cs2.append( (SetDialogue, ("dexter","Dexter","Ahem, you're the one who locked us your 'playhouse'."), 1) )
cs2.append( (SetDialogue, ("lex","Lex","Ugh! I don't want to see you two ever again...I don't want to see anybody again!"), 1) )
cs2.append( (SetDialogue, ("lex","Lex","Heh...They'll see. I'll have more fun than they ever had!"), 1) )
cs2.append( (SetDialogue, ("dexter","Dexter","Man...someone flew over the cuckoo's nest..."), 1) )
cs2.append( (SetDialogue, ("may","May","Look out, Dex! I think he's..."), 1) )
cs2.append( (SetDialogue, ("may","May","Oh no! He's blowing the whole place up! You have to hurry!"), 1) )
cs2.append( (ScrollTo, (lex.id, 60), 1) )
cs2.append( (SetDialogue, ("may","May","You have to destroy Lex, but he's protected by that wall around him..."), 1) )
cs2.append( (ScrollTo, (room.GetObjectByName("lever1").id, 60), 1) )
cs2.append( (SetDialogue, ("may","May","You need to switch this lever. It will take off parts of the wall, so you can shoot him."), 1) )
cs2.append( (SetDialogue, ("may","May","There are three platforms you can use to get close to Lex."), 1) )
cs2.append( (ScrollToPos, (784-v.width*TILEWIDTH/2, 1192-v.height*TILEHEIGHT/2, 60), 1) )
cs2.append( (SetDialogue, ("may","May","One here..."), 1) )
cs2.append( (ScrollToPos, (1186-v.width*TILEWIDTH/2, 1490-v.height*TILEHEIGHT/2, 60), 1) )
cs2.append( (SetDialogue, ("may","May","Another here..."), 1) )
cs2.append( (ScrollToPos, (1590-v.width*TILEWIDTH/2, 1200-v.height*TILEHEIGHT/2, 60), 1) )
cs2.append( (SetDialogue, ("may","May","And finally here. Now go and destroy Lex!"), 1) )
cs2.append( (ScrollTo, (player.id, 60), 1) )
cs2.append( (v.FocusTo, player.id, 0) )
cs2.append( (PlayMusic, "five", 0) )
cs2.append( (StartTimer, None, 0) )

cs3=[]
cs3.append( (SetDialogue, ("lex","Lex","Ha ha ha!"), 1) )
cs3.append( (SetDialogue, ("may","May","No! Dex! Dex..."), 1) )
cs3.append( (s.stateList[s.currentState].ReloadLevel, None, 0) )

cs4=[]
cs4.append( (SetDialogue, ("may","May","Dex, you've already done that! Now go and finish Lex!"), 1) )

def HitLex(args):
     global lex
     lex.data["hit"]=True

cs5=[]
cs5.append( (v.FocusTo, -1, 0) )
cs5.append( (ScrollTo, (room.GetObjectByName("lex").id, 60), 1) )
cs5.append( (Wait, 10, 1) )
cs5.append( (SwitchLex, 3, 0) )
cs5.append( (Wait, 30, 1) )
cs5.append( (ScrollTo, (player.id, 60), 1) )
cs5.append( (v.FocusTo, player.id, 0) )
cs5.append( (HitLex, None, 0) )

def FadeLex(args):
     global lex
     lex.data["fade"]=True

cs8=[]
cs8.append( (v.FocusTo, -1, 0) )
cs8.append( (ScrollTo, (lex.id, 60), 1) )
cs8.append( (FadeLex, None, 0) )
cs8.append( (SetDialogue, ("lex","Lex","NOOOOO!"), 1) )
cs8.append( (SetDialogue, ("may","May","Good job, Dex! Come on, let's get out of here!"), 1) )
cs8.append( (SetDialogue, ("dexter","Dexter","Whew. That was close!"), 1) )
cs8.append( (s.stateList["room"].NextLevel, None, 0) )
cs8.append( (StopTimer, False, 0) )

cs7=[]
cs7.append( (SetDialogue, ("may","May","Dex! Pick up the journal first!"), 1) )

def PackageCutscene(m):
     global l, cs1, cs2, cs3, cs4, cs5, cs8, cs7, SwitchLex, lexSide, lexProgress, lex, lexProtected, lexHitCount
     if m.obj.name == "lever1":
          if room.GetObjectByName("pack1") != None:
               LoadCutscene(cs7,True)
          else:
               if lexProtected:
                    LoadCutscene(cs1,False)
               else:
                    LoadCutscene(cs4,True)
               
     elif m.obj.name == "droid1":
          room.AddAlarm(l,210,(1,m.obj.origX,m.obj.origY,"droid1"))
     elif m.obj.name == "droid2":
          room.AddAlarm(l,210,(1,m.obj.origX,m.obj.origY,"droid2"))
     elif m.obj.name == "droid3":
          room.AddAlarm(l,150,(1,m.obj.origX,m.obj.origY,"droid3"))
     elif m.obj.name == "droid4":
          room.AddAlarm(l,210,(1,m.obj.origX,m.obj.origY,"droid4"))
     elif m.obj.name == "sentry1":
          room.AddAlarm(l,210,(2,m.obj.origX,m.obj.origY,"sentry1"))
     elif m.obj.name == "pack1" and m.collision_type != COLLISION_WALL:
          if  m.obj2.name=="player":
               LoadCutscene(cs2)
     elif m.obj.name == "lex":
          if m.type == OBJECT_COLLISION:
               if m.collision_type != COLLISION_WALL:
                    if m.obj2.type.name == "bullet" and lex.data["hit"] and lex.data["HP"] > 0:
                         lexProgress.setValue(float(lex.data["HP"]))
                         lexHitCount+=1
                         if lexHitCount >= 5:
                              lexHitCount=0
                              lex.data["hit"]=False
                              LoadCutscene(cs5,False)
          
                    elif lex.data["HP"] == 0:
                         LoadCutscene(cs8,True)
                       
          
def PackageAlarm(m):
     if m.data[0]==1:
          id=room.AddObject("droid",m.data[1],m.data[2],m.data[3])
          o=room.GetObjectById(id)
          o.data["life"]=1
          o.AddSubscriber(l,OBJECT_DESTROYED)
     if m.data[0]==2:
          id=room.AddObject("sentry",m.data[1],m.data[2],m.data[3])
          o=room.GetObjectById(id)
          o.data["walk_list"]=["to:1330","to:2145"]
          o.AddSubscriber(l,OBJECT_DESTROYED)

l=Listener(PackageCutscene,PackageAlarm)
l2=Listener(Timer,Timer)
room.GetObjectByName("lever1").AddSubscriber(l,OBJECT_ACTION)
room.GetObjectByName("droid1").AddSubscriber(l,OBJECT_DESTROYED)
room.GetObjectByName("droid2").AddSubscriber(l,OBJECT_DESTROYED)
room.GetObjectByName("droid3").AddSubscriber(l,OBJECT_DESTROYED)
room.GetObjectByName("droid4").AddSubscriber(l,OBJECT_DESTROYED)
room.GetObjectByName("sentry1").AddSubscriber(l,OBJECT_DESTROYED)
room.GetObjectByName("pack1").AddSubscriber(l,OBJECT_COLLISION)
lex.AddSubscriber(l,MSG_ALL)

player.data["HP"]=5
player.data["currentHP"]=5
heartLabel.setCaption(str(player.data["currentHP"]))

lexProgress.setMax(float(lex.data["maxHP"]))
lexProgress.setValue(float(lex.data["HP"]))

global boss
boss=True