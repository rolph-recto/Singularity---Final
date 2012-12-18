#!/usr/bin/env python

def PackageCutscene(m):
     global s, notifyAlarm, room, cs2, cs3
     if m.obj.name == "sensor1" and m.collision_type != COLLISION_WALL:
          if  m.obj2.name=="player" and ("sensed" in m.obj.data) == False:
               Notify("Checkpoint reached!")
               if notifyAlarm == -1:
                    notifyAlarm=room.AddAlarm(s.stateList["room"].oListen,150,1)
               else:
                    room.GetAlarmById(notifyAlarm).startFrame=main.frame
               
               m.obj2.data["startX"]=608
               m.obj2.data["startY"]=1216
               m.obj.data["sensed"]=True
               
     if m.obj.name == "pack1" and m.collision_type != COLLISION_WALL:
          if  m.obj2.name=="player":
               LoadCutscene(cs2)
               
     if m.obj.name == "blue1" and m.collision_type != COLLISION_WALL:
          if  m.obj2.name=="player":
               LoadCutscene(cs3)


               
frameIter=0
frameEnd=12600
timerAlarm=-1

def StartTimer(args=()):
     global timeLabel, room, frameIter, timerAlarm, l2
     timeLabel.setVisible(True)
     timerAlarm=room.AddAlarm(l2,1,None,-1)
     frameIter=0
     
def Timer(m):
     global timeLabel,pause, frameIter, frameEnd, cs4, room, timerAlarm, StopTimer
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
     room.RemoveAlarm(timerAlarm)
     timeLabel.setVisible(False)
     if reload:
          LoadCutscene(cs4)
               
cs2=[]
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
cs2.append( (PlayMusic, "five", 0) )
cs2.append( (StartTimer, None, 0) )

cs3=[]
cs3.append( (SetDialogue, ("may","May","You made it Dex! Come on, let's get out of here!"), 1) )
cs3.append( (SetDialogue, ("dexter","Dexter","Whew. That was close!"), 1) )
cs3.append( (s.stateList["room"].NextLevel, None, 0) )
cs3.append( (StopTimer, False, 0) )

cs4=[]
cs4.append( (SetDialogue, ("lex","Lex","Ha ha ha!"), 1) )
cs4.append( (SetDialogue, ("may","May","No! Dex! Dex..."), 1) )
cs4.append( (s.stateList[s.currentState].ReloadLevel, None, 0) )

l=Listener(PackageCutscene)
l2=Listener(Timer)
room.GetObjectByName("sensor1").AddSubscriber(l,OBJECT_COLLISION)
room.GetObjectByName("pack1").AddSubscriber(l,OBJECT_COLLISION)
room.GetObjectByName("blue1").AddSubscriber(l,OBJECT_COLLISION)