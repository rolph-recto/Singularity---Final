#!/usr/bin/env python

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

l=Listener(PackageCutscene)

cs1=[]
cs1.append( (SetDialogue, ("dexter","Dexter","Look at this place, May! It's so..."), 1) )
cs1.append( (SetDialogue, ("may","May","Creepy?"), 1) )
cs1.append( (SetDialogue, ("dexter","Dexter","Well, not the word I was looking for, but I guess that fits..."), 1) )
cs1.append( (SetDialogue, ("may","May","Seriously, Dex, you don't have to do this."), 1) )
cs1.append( (SetDialogue, ("dexter","Dexter","But I have to! I have a feeling we can find clues here. I mean, crime lurks in the darkness, right?"), 1) )
cs1.append( (SetDialogue, ("may","May","You're off-duty, Dex. OFF-duty. We can do this later. Finding out why the crime rate's skyrocketing is not my cup of tea."), 1) )
cs1.append( (SetDialogue, ("dexter","Dexter","No, no, we're here already. And besides, it's my time to use, who cares?"), 1) )
cs1.append( (SetDialogue, ("may","May","It's my time too..."), 1) )
cs1.append( (SetDialogue, ("dexter","Dexter","Hey! You said you want to tag along!"), 1) )
cs1.append( (SetDialogue, ("may","May","Right, I didn't say I want to snoop around a place in the Network no one's been to in years. I mean, look at this place..."), 1) )
cs1.append( (SetDialogue, ("dexter","Dexter","Alright already! If you want to, stay behind. I'll go by myself."), 1) )
cs1.append( (SetDialogue, ("may","May","Fine, you go on this suicide mission. I value my life, thank you very much."), 1) )
cs1.append( (SetDialogue, ("dexter","Dexter","Well can you tell me at least what's around here?"), 1) )
cs1.append( (SetDialogue, ("may","May","Ugh. So stubborn..."), 1) )
cs1.append( (ScrollTo, (room.GetObjectByName("pack1").id, 40), 1) )
cs1.append( (SetDialogue, ("may","May","I detected this...entity here. Could be anything."), 1) )
cs1.append( (SetDialogue, ("dexter","Dexter","Great! It could be a clue. Something about Project Genesis."), 1) )
cs1.append( (SetDialogue, ("may","May","Or a bomb. Look, just be careful, alright? There's a lot of traps in here. Looks like the place is littered with hostile agents."), 1) )
cs1.append( (SetDialogue, ("may","May","Weird, their timestamps show they've been here a while. It's an old server in the Network...Probably one of the first ones."), 1) )
cs1.append( (SetDialogue, ("dexter","Dexter","Oh sheesh, just a bunch of old hostiles? Cake!"), 1) )
cs1.append( (ScrollTo, (player.id, 40), 1) )
cs1.append( (v.FocusTo, (player.id), 0) )

cs2=[]
cs2.append( (SetDialogue, ("","","Project Genesis\nLog #1 - 04/21/2015"), 1) )
cs2.append( (SetDialogue, ("","","Agents showed higher intelligence than predicted. Neural network was fed only half of complete corpus, yet lingual and mathematical abilities are excellent. Passed Turing test with flying colors."), 1) )
cs2.append( (SetDialogue, ("","","Despite surpassed expectations, agents do not exhibit self-awareness. Also, agents acted very infantile - speech patterns are similar to that of a prebubescent boy."), 1) )
cs2.append( (SetDialogue, ("","","Considering posibility of implanting agents into a body, an avatar of sorts."), 1) )
cs2.append( (SetDialogue, ("","","Will proceed with further testing in the next few months. Singularity expected ahead of schedule."), 1) )
cs2.append( (SetDialogue, ("dexter","Dexter","Look at this May. Project Genesis! It's here again!"), 1) )
cs2.append( (SetDialogue, ("may","May","Goodness...It's about 20 years old!"), 1) )
cs2.append( (SetDialogue, ("dexter","Dexter","Wow I didn't know that Project was that old...Then again, I don't know anything about the Project."), 1) )
cs2.append( (SetDialogue, ("may","May","Seems like from this log entry that its purpose was to make artificial intelligence..."), 1) )
cs2.append( (SetDialogue, ("dexter","Dexter","It does, but no one's ever actually created a fully functioning AI. All known attempts have failed, you know?"), 1) )
cs2.append( (SetDialogue, ("may","May","Of course...It's probably one of the ones that failed."), 1) )
cs2.append( (SetDialogue, ("dexter","Dexter","I don't know, maybe they were successful."), 1) )
cs2.append( (SetDialogue, ("may","May","Oh come on! If they did, everyone in the whole world would know it! And AI agents would be everwhere in the Network!"), 1) )
cs2.append( (SetDialogue, ("may","May","AI is just a crackpot's dream, Dex! It'll never happen!"), 1) )
cs2.append( (SetDialogue, ("","","Never happen, eh?"), 1) )
cs2.append( (SetDialogue, ("dexter","Dexter","Who's that?"), 1) )
cs2.append( (SetDialogue, ("","","Maybe you should dig a bit deeper, missy..."), 1) )
cs2.append( (SetDialogue, ("","","Either way, I give you no choice. You're going to be in my playhouse for a while. Ha!"), 1) )
cs2.append( (s.stateList["room"].NextLevel, None, 0) )

#PlayMusic("one")
#v.FocusTo(-1)
#LoadCutscene(cs1)
room.GetObjectByName("sensor1").AddSubscriber(l,OBJECT_COLLISION)
room.GetObjectByName("pack1").AddSubscriber(l,OBJECT_COLLISION)