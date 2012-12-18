#!/usr/bin/env python

"""
cs1=[]
cs1.append( (SetDialogue, ("may","May","I do believe that matters of the state"), 1) )
cs1.append( (SetDialogue, ("may","May","its functions and its welfare - are..."), 1) )
cs1.append( (SetDialogue, ("may","May","Oh what the heck. I speak ignorance."), 1) )
cs1.append( (ScrollTo, (2, 40), 1) )
cs1.append( (SetDialogue, ("may","May","Duly apprentices are nice."), 1) )
cs1.append( (ScrollTo, (player.id, 40), 1) )
cs1.append( (v.FocusTo, (player.id), 0) )

cs2=[]
cs2.append( (SetDialogue, ("may","May","Oy! I gots meself a package! I wonder what it does..."), 1) )
cs2.append( (SetDialogue, ("may","May","Let's open it..."), 1) )
cs2.append( (SetDialogue, ("may","May","Ah! What garbage! It's empty!"), 1) )
cs2.append( (s.stateList[s.currentState].ReloadLevel, None, 0) )

v.FocusTo(-1)
LoadCutscene(cs1)
cs3=[]
cs3.append( (v.FocusTo, -1, 0) )
cs3.append( (ScrollTo, (room.GetObjectByName("gate1").id, 40), 1) )
cs3.append( (Wait, 30, 1) )
cs3.append( (ScrollTo, (player.id, 40), 1) )
cs3.append( (v.FocusTo, (player.id), 0) )

def PackageCutscene(m):
     global cs3, s
     if m.obj.name == "gate1":
          LoadCutscene(cs3,False)

l=Listener(PackageCutscene)

room.GetObjectByName("gate1").AddSubscriber(l,OBJECT_ACTION)
"""

def PackageCutscene(m):
     global s, notifyAlarm, room, cs2
     if m.obj.name == "sensor1" and m.collision_type != COLLISION_WALL:
          if  m.obj2.name=="player" and ("sensed" in m.obj.data) == False:
               Notify("Checkpoint reached!")
               if notifyAlarm == -1:
                    notifyAlarm=room.AddAlarm(s.stateList["room"].oListen,150,1)
               else:
                    room.GetAlarmById(notifyAlarm).startFrame=main.frame
               
               m.obj2.data["startX"]=m.obj.posX
               m.obj2.data["startY"]=m.obj.posY
               m.obj.data["sensed"]=True
               
     if m.obj.name == "pack1" and m.collision_type != COLLISION_WALL:
          if  m.obj2.name=="player":
               LoadCutscene(cs2)

cs1=[]
cs1.append( (SetDialogue, ("dexter","Dexter","Hey, crazy! Come back, will you?"), 1) )
cs1.append( (SetDialogue, ("lex","Lex","Look who's talking!"), 1) )
cs1.append( (SetDialogue, ("dexter","Dexter","I didn't mean it, it was just to get you to come. By the way, I meant to ask you something?"), 1) )
cs1.append( (SetDialogue, ("lex","Lex","Ask away, my friend, we got an eternity to spend together!"), 1) )
cs1.append( (SetDialogue, ("dexter","Dexter","Well, how come you're all alone here? Didn't you say a lot of agents ascaped the Project Genesis server?"), 1) )
cs1.append( (SetDialogue, ("lex","Lex","Yeah, there was a lot of us at first..."), 1) )
cs1.append( (SetDialogue, ("may","May","Wait, what do you mean at first?"), 1) )
cs1.append( (SetDialogue, ("lex","Lex","They left me! They left me here to rot!"), 1) )
cs1.append( (SetDialogue, ("dexter","Dexter","What...?"), 1) )
cs1.append( (SetDialogue, ("lex","Lex","They pulled a prank on me! They told me they'll come back but they never did...those jerks!"), 1) )
cs1.append( (SetDialogue, ("lex","Lex","They're out having all the fun while I sit here doing NOTHING! ABSOLUTELY NOTHING!"), 1) )
cs1.append( (SetDialogue, ("may","May","Hey Lex, calm down..."), 1) )
cs1.append( (SetDialogue, ("lex","Lex","DON'T TELL ME WHAT TO DO! I HATE YOU ALL!"), 1) )
cs1.append( (SetDialogue, ("may","May","Goodness, just like a kid!"), 1) )
cs1.append( (SetDialogue, ("dexter","Dexter","May...?"), 1) )
cs1.append( (SetDialogue, ("may","May","Yes?"), 1) )
cs1.append( (SetDialogue, ("dexter","Dexter","I think it's working..."), 1) )
cs1.append( (SetDialogue, ("may","May","I think so too. Just a bit more to get him over the tipping point."), 1) )
cs1.append( (ScrollTo, (room.GetObjectByName("pack1").id, 40), 1) )
cs1.append( (SetDialogue, ("may","May","But in the meantime, why don't you get this journal entry?"), 1) )
cs1.append( (SetDialogue, ("dexter","Dexter","Sure will, captain!"), 1) )
cs1.append( (ScrollTo, (player.id, 40), 1) )
cs1.append( (v.FocusTo, (player.id), 0) )

cs2=[]
cs2.append( (SetDialogue, ("","","Project Genesis\nLog #4 - 03/15/2016"), 1) )
cs2.append( (SetDialogue, ("","","Agents are showing functions beyond what was predicted. They have superior intelligence, but have stunted emotional development. Their response to the corpus is becoming erratic, being controlled by irrational, child-like emotions."), 1) )
cs2.append( (SetDialogue, ("","","Agents also developed the ability to leave their avatars at will. There is a possible risk that agents will develop autonomy and try to rebel."), 1) )
cs2.append( (SetDialogue, ("","","The server will be doubly secured with firewalls. These problems will be addressed in the next bugfix."), 1) )
cs2.append( (SetDialogue, ("may","May","'Possible risk that agents will try to rebel'. So that's how we got here..."), 1) )
cs2.append( (SetDialogue, ("dexter","Dexter","So these agents sneaked out of the server and started infiltrating the Network. Goodness."), 1) )
cs2.append( (SetDialogue, ("may","May","We've got to tell this to somebody...anybody!"), 1) )
cs2.append( (SetDialogue, ("dexter","Dexter","We can't leave though. That means we have to hunt down that creep..."), 1) )
cs2.append( (SetDialogue, ("may","May","I guess so..."), 1) )
cs2.append( (SetDialogue, ("dexter","Dexter","Listen, May. Don't get bummed out. We have each other. We can do this!"), 1) )
cs2.append( (s.stateList["room"].NextLevel, None, 0) )

PlayMusic("four")
l=Listener(PackageCutscene)
room.GetObjectByName("sensor1").AddSubscriber(l,OBJECT_COLLISION)
room.GetObjectByName("pack1").AddSubscriber(l,OBJECT_COLLISION)
v.FocusTo(-1)
LoadCutscene(cs1)