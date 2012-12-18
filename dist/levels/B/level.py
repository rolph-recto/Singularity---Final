#!/usr/bin/env python
#LEVEL FOUR
l=None

def OpenTrap(args):
     index=room.map.GetTemplateIdByName("SP")
     room.map.base[1][2]=index
     room.map.base[2][2]=index
     room.map.base[3][2]=index

cs1=[]
cs1.append( (OpenTrap, None, 0) )
cs1_done=False

cs2=[]
cs2.append( (v.FocusTo, -1, 0) )
cs2.append( (ScrollTo, (room.GetObjectByName("gate1").id, 60), 1) )
cs2.append( (Wait, 30, 1) )
cs2.append( (ScrollTo, (player.id, 60), 1) )
cs2.append( (v.FocusTo, player.id, 0) )

cs3=[]
cs3.append( (v.FocusTo, -1, 0) )
cs3.append( (ScrollTo, (room.GetObjectByName("gate2").id, 30), 1) )
cs3.append( (Wait, 30, 1) )
cs3.append( (ScrollTo, (player.id, 30), 1) )
cs3.append( (v.FocusTo, player.id, 0) )

cs4=[]
cs4.append( (v.FocusTo, -1, 0) )
cs4.append( (SetDialogue, ("dexter","Dexter","Hey, crazy! Come back, will you?"), 1) )
cs4.append( (SetDialogue, ("lex","Lex","Look who's talking!"), 1) )
cs4.append( (SetDialogue, ("dexter","Dexter","I didn't mean it, it was just to get you to come. By the way, I meant to ask you something?"), 1) )
cs4.append( (SetDialogue, ("lex","Lex","Ask away, my friend, we got an eternity to spend together!"), 1) )
cs4.append( (SetDialogue, ("dexter","Dexter","Well, how come you're all alone here? Didn't you say a lot of agents ascaped the Project Genesis server?"), 1) )
cs4.append( (SetDialogue, ("lex","Lex","Yeah, there was a lot of us at first..."), 1) )
cs4.append( (SetDialogue, ("may","May","Wait, what do you mean at first?"), 1) )
cs4.append( (SetDialogue, ("lex","Lex","They left me! They left me here to rot!"), 1) )
cs4.append( (SetDialogue, ("dexter","Dexter","What...?"), 1) )
cs4.append( (SetDialogue, ("lex","Lex","They pulled a prank on me! They told me they'll come back but they never did...those jerks!"), 1) )
cs4.append( (SetDialogue, ("lex","Lex","They're out having all the fun while I sit here doing NOTHING! ABSOLUTELY NOTHING!"), 1) )
cs4.append( (SetDialogue, ("may","May","Hey Lex, calm down..."), 1) )
cs4.append( (SetDialogue, ("lex","Lex","DON'T TELL ME WHAT TO DO! I HATE YOU ALL!"), 1) )
cs4.append( (SetDialogue, ("may","May","Goodness, just like a kid!"), 1) )
cs4.append( (SetDialogue, ("dexter","Dexter","May...?"), 1) )
cs4.append( (SetDialogue, ("may","May","Yes?"), 1) )
cs4.append( (SetDialogue, ("dexter","Dexter","I think it's working..."), 1) )
cs4.append( (SetDialogue, ("may","May","I think so too. Just a bit more to get him over the tipping point."), 1) )
cs4.append( (ScrollTo, (room.GetObjectByName("pack1").id, 40), 1) )
cs4.append( (SetDialogue, ("may","May","But in the meantime, why don't you get this journal entry?"), 1) )
cs4.append( (SetDialogue, ("dexter","Dexter","Sure will, captain!"), 1) )
cs4.append( (ScrollToPos, (726-(v.width/2*TILEWIDTH), 420-(v.height/2*TILEHEIGHT), 60), 1) )
cs4.append( (SetDialogue, ("may","May","Oh, and by the way, I noticed these crates here. I don't think they're there for a reason, but maybe you can use them somehow..."), 1) )
cs4.append( (ScrollTo, (player.id, 40), 1) )
cs4.append( (v.FocusTo, (player.id), 0) )

cs5=[]
cs5.append( (SetDialogue, ("","","Project Genesis\nLog #4 - 03/15/2016"), 1) )
cs5.append( (SetDialogue, ("","","Agents are showing functions beyond what was predicted. They have superior intelligence, but have stunted emotional development. Their response to the corpus is becoming erratic, being controlled by irrational, child-like emotions."), 1) )
cs5.append( (SetDialogue, ("","","Agents also developed the ability to leave their avatars at will. There is a possible risk that agents will develop autonomy and try to rebel."), 1) )
cs5.append( (SetDialogue, ("","","The server will be doubly secured with firewalls. These problems will be addressed in the next bugfix."), 1) )
cs5.append( (SetDialogue, ("may","May","'Possible risk that agents will try to rebel'. So that's how we got here..."), 1) )
cs5.append( (SetDialogue, ("dexter","Dexter","So these agents sneaked out of the server and started infiltrating the Network. Goodness."), 1) )
cs5.append( (SetDialogue, ("may","May","We've got to tell this to somebody...anybody!"), 1) )
cs5.append( (SetDialogue, ("dexter","Dexter","We can't leave though. That means we have to hunt down that creep..."), 1) )
cs5.append( (SetDialogue, ("may","May","I guess so..."), 1) )
cs5.append( (SetDialogue, ("dexter","Dexter","Listen, May. Don't get bummed out. We have each other. We can do this!"), 1) )
cs5.append( (s.stateList["room"].NextLevel, None, 0) )

def PackageCutscene(m):
     global cs2, s, cs1, cs1_done, cs2, cs3, cs4, cs5
     if m.obj.name == "lever1" and cs1_done == False:
          cs1_done=True
          LoadCutscene(cs1,False)
     elif m.obj.name == "lever2":
          LoadCutscene(cs2,False)
     elif m.obj.name == "lever3":
          LoadCutscene(cs3,False)
     if m.obj.name == "pack1" and m.collision_type != COLLISION_WALL:
          if  m.obj2.name=="player":
               LoadCutscene(cs5,True)
          
          
l=Listener(PackageCutscene)
room.GetObjectByName("lever1").AddSubscriber(l,OBJECT_ACTION)
room.GetObjectByName("lever2").AddSubscriber(l,OBJECT_ACTION)
room.GetObjectByName("lever3").AddSubscriber(l,OBJECT_ACTION)
room.GetObjectByName("pack1").AddSubscriber(l,OBJECT_COLLISION)

PlayMusic("four")
LoadCutscene(cs4,True)