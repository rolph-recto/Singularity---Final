#!/usr/bin/env python

cs3=[]
cs3.append( (v.FocusTo, -1, 0) )
cs3.append( (ScrollTo, (room.GetObjectByName("gate1").id, 40), 1) )
cs3.append( (Wait, 30, 1) )
cs3.append( (ScrollTo, (player.id, 40), 1) )
cs3.append( (v.FocusTo, (player.id), 0) )

def PackageCutscene(m):
     global cs2, s, cs3
     if m.obj.name == "gate1" or m.obj.name == "lever2":
          LoadCutscene(cs3,False)
     if m.obj.name == "pack1" and m.collision_type != COLLISION_WALL:
          if  m.obj2.name=="player":
               LoadCutscene(cs2)

cs1=[]
cs1.append( (SetDialogue, ("dexter","Dexter","Did he just say we're in his playhouse?"), 1) )
cs1.append( (SetDialogue, ("may","May","I don't know, Dex. He could be bluffing."), 1) )
cs1.append( (SetDialogue, ("dexter","Dexter","Well, considering we couldn't leave through the entrance..."), 1) )
cs1.append( (SetDialogue, ("may","May","There has to be an exit somewhere."), 1) )
cs1.append( (SetDialogue, ("dexter","Dexter","Only way to find out is to look, right?"), 1) )
cs1.append( (SetDialogue, ("may","May","I guess. Oh this isn't good Dex...Look what you've done..."), 1) )
cs1.append( (SetDialogue, ("dexter","Dexter","Hey, chill out alright? We found that journal, didn't we? So since we're stuck here, we might as well look for other entries. I bet you Project Genesis has something to do with crime."), 1) )
cs1.append( (SetDialogue, ("may","May","I don't care, Dex. I just want to get out of here."), 1) )
cs1.append( (ScrollTo, (room.GetObjectByName("pack1").id, 40), 1) )
cs1.append( (SetDialogue, ("may","May","There's another journal entry here. Maybe that person will talk to us again if we get it."), 1) )
cs1.append( (SetDialogue, ("dexter","Dexter","Alright then, let's roll!"), 1) )
cs1.append( (ScrollTo, (player.id, 40), 1) )
cs1.append( (v.FocusTo, (player.id), 0) )

cs2=[]
cs2.append( (SetDialogue, ("","","Project Genesis\nLog #2 - 11/11/2015"), 1) )
cs2.append( (SetDialogue, ("","","Agents displayed rudimentary self-awareness. Able to discern self-image in interaction, but higher level mental faculties still not developed."), 1) )
cs2.append( (SetDialogue, ("","","Agents were implanted in virtual 'bodies'. They were able to use basic motor functions, such as crawling and climbing steps."), 1) )
cs2.append( (SetDialogue, ("","","Child-like emotions planned to be implemented in next software update. Neural network capacity tripled to accomodate for more complex behavior."), 1) )
cs2.append( (SetDialogue, ("dexter","Dexter","Man...it sounds like this Project Genesis has created something..."), 1) )
cs2.append( (SetDialogue, ("","","Ah yes, Project Genesis...The pinnacle of human hubris."), 1) )
cs2.append( (SetDialogue, ("may","May","You again! Why don't you show yourself?"), 1) )
cs2.append( (SetDialogue, ("","","Patience, my dear. I don't like to be interrupted."), 1) )
cs2.append( (SetDialogue, ("may","May","Hmph!"), 1) )
cs2.append( (SetDialogue, ("","","Anyways, where was I...Oh yes. Project Genesis and its failed attempt to create intelligence."), 1) )
cs2.append( (SetDialogue, ("","","It's funny, don't you think? A sentient species thinks it can create something that resembles itself, while controlling it. How vein, this dream of Singularity..."), 1) )
cs2.append( (SetDialogue, ("dexter","Dexter","What is singularity?"), 1) )
cs2.append( (SetDialogue, ("","","I just told you! The dream of creating and controlling an entity of human-level intelligence. Oh, you should have seen how they gushed about it years ago."), 1) )
cs2.append( (SetDialogue, ("dexter","Dexter","...And did they succeed?"), 1) )
cs2.append( (SetDialogue, ("","","To save you some guess, yes. Yes they did. In fact, they created entities that surpassed human intelligence."), 1) )
cs2.append( (SetDialogue, ("dexter","Dexter","Where are they then? How come no one knows about this?"), 1) )
cs2.append( (SetDialogue, ("","","Ha! Very good question. No one knows because the entities...oh, let's say got a little out of hand."), 1) )
cs2.append( (SetDialogue, ("","","And if you're wondering where are they, look no further. You are talking to one right now."), 1) )
cs2.append( (s.stateList["room"].NextLevel, None, 0) )

l=Listener(PackageCutscene)

room.GetObjectByName("pack1").AddSubscriber(l,OBJECT_COLLISION)
room.GetObjectByName("gate1").AddSubscriber(l,OBJECT_ACTION)

PlayMusic("two")
v.FocusTo(-1)
LoadCutscene(cs1)