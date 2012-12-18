#!/usr/bin/env python

l=None

def SwitchGate(args):
     o=room.GetObjectByName("gate"+str(args[0]))
     o.BroadcastMessage(ObjectMessage(o,OBJECT_ACTION,(o,)))

cs1=[]
cs1.append( (v.FocusTo, -1, 0) )
cs1.append( (ScrollToPos, (796-(v.width/2*TILEWIDTH), 70-(v.height/2*TILEHEIGHT), 60), 1) )
cs1.append( (Wait, 10, 1) )
cs1.append( (SwitchGate, (3,), 0) )
cs1.append( (Wait, 30, 1) )
cs1.append( (ScrollTo, (player.id, 40), 1) )
cs1.append( (v.FocusTo, player.id, 0) )

cs2=[]
cs2.append( (v.FocusTo, -1, 0) )
cs2.append( (ScrollToPos, (675-(v.width/2*TILEWIDTH), 68-(v.height/2*TILEHEIGHT), 60), 1) )
cs2.append( (Wait, 10, 1) )
cs2.append( (SwitchGate, (3,), 0) )
cs2.append( (SwitchGate, (2,), 0) )
cs2.append( (Wait, 30, 1) )
cs2.append( (ScrollTo, (player.id, 40), 1) )
cs2.append( (v.FocusTo, player.id, 0) )

cs3=[]
cs3.append( (v.FocusTo, -1, 0) )
cs3.append( (ScrollToPos, (430-(v.width/2*TILEWIDTH), 68-(v.height/2*TILEHEIGHT), 60), 1) )
cs3.append( (Wait, 10, 1) )
cs3.append( (SwitchGate, (1,), 0) )
cs3.append( (SwitchGate, (2,), 0) )
cs3.append( (Wait, 30, 1) )
cs3.append( (ScrollTo, (player.id, 40), 1) )
cs3.append( (v.FocusTo, player.id, 0) )

cs4=[]
cs4.append( (v.FocusTo, -1, 0) )
cs4.append( (SetDialogue, ("dexter","Dexter","You! You're created by Project Genesis?"), 1) )
cs4.append( (SetDialogue, ("","","Yessir, first compiled in 06/23/2015."), 1) )
cs4.append( (SetDialogue, ("may","May","Why don't you show yourself?"), 1) )
cs4.append( (SetDialogue, ("lex","???","Oh what the heck, why not. It's not like you can hurt me."), 1) )
cs4.append( (SetDialogue, ("lex","Lex","The name would be Lex, ladies and gentlemen."), 1) )
cs4.append( (SetDialogue, ("may","May","How did you get here?"), 1) )
cs4.append( (SetDialogue, ("lex","Lex","Good question! We planned a mutiny, ran away, and here I am!"), 1) )
cs4.append( (SetDialogue, ("dexter","Dexter","Wait, we?"), 1) )
cs4.append( (SetDialogue, ("lex","Lex","Oh yes, we! There were about 50 preliminary agents that exited the server."), 1) )
cs4.append( (SetDialogue, ("may","May","And where are they?"), 1) )
cs4.append( (SetDialogue, ("lex","Lex","Oh, here, there, everywhere. We go places."), 1) )
cs4.append( (SetDialogue, ("may","May","Like central data hubs of the Network?"), 1) )
cs4.append( (SetDialogue, ("lex","Lex","We got a smart cookie in here! Finally someone figured out."), 1) )
cs4.append( (SetDialogue, ("dexter","Dexter","Figured out what?"), 1) )
cs4.append( (SetDialogue, ("may","May","They were the ones who's been doing all the crimes..."), 1) )
cs4.append( (SetDialogue, ("dexter","Dexter","Get out!"), 1) )
cs4.append( (SetDialogue, ("lex","Lex","Sorry, your lady friend's right. We agents like to have fun, eh?"), 1) )
cs4.append( (SetDialogue, ("lex","Lex","It's really simple, too. We just...'hack' somebody, anybody really, and there you have it! A zombie we can control."), 1) )
cs4.append( (SetDialogue, ("may","May","But...why? What's the point of all this?"), 1) )
cs4.append( (SetDialogue, ("lex","Lex","You have to liven up a little! I don't worry about that kind of stuff! What's the point of it...Ha, if I knew the answer I'd tell you!"), 1) )
cs4.append( (SetDialogue, ("may","May","No! You have to-"), 1) )
cs4.append( (SetDialogue, ("lex","Lex","I don't have to do anything, lady. Ugh, you're making me sick. Peace out, chumps!"), 1) )
cs4.append( (SetDialogue, ("dexter","Dexter","He has quite a nerve..."), 1) )
cs4.append( (SetDialogue, ("may","May","And I don't like it. I guess we just have to keep going."), 1) )
cs4.append( (ScrollTo, (room.GetObjectByName("pack1").id, 40), 1) )
cs4.append( (SetDialogue, ("may","May","Another journal entry here. Maybe we can find something in it that can help us get out of this mess."), 1) )
cs4.append( (ScrollTo, (player.id, 40), 1) )
cs4.append( (v.FocusTo, (player.id), 0) )

cs5=[]
cs5.append( (SetDialogue, ("","","Project Genesis\nLog #3 - 01/07/2016"), 1) )
cs5.append( (SetDialogue, ("","","Finished integration of agents in avatars. Agents able to use simulated motor faculties in a sandbox environment. They have quickly acclimated themselves in the virtual 'bodies'."), 1) )
cs5.append( (SetDialogue, ("","","Also, agents are displaying increased self-awareness. They have acquired a primodial capability for emotional development."), 1) )
cs5.append( (SetDialogue, ("","","For example, agents were fed a corpus with a positive connotation; agent responded with a positive connotation also."), 1) )
cs5.append( (SetDialogue, ("","","However, agents display emotional faculties of a child. Must be a priority for a bug fix in the next software release."), 1) )
cs5.append( (SetDialogue, ("may","May","My goodness...virtual bodies?"), 1) )
cs5.append( (SetDialogue, ("dexter","Dexter","And emotions...explains a lot about Lex..."), 1) )
cs5.append( (SetDialogue, ("lex","Lex","Oh, come on! Flamboyance is my virtue!"), 1) )
cs5.append( (SetDialogue, ("dexter","Dexter","Yeah, and maybe insanity too..."), 1) )
cs5.append( (SetDialogue, ("lex","Lex","Hey, watch it, man! I can break you like a twig!"), 1) )
cs5.append( (SetDialogue, ("dexter","Dexter","Right. If you were gonna 'hack' into us you would've done it a long time ago."), 1) )
cs5.append( (SetDialogue, ("lex","Lex","Hmm...Looks like you have a brain after all. Yes, that's right, before I can take over someone's virtual avatar they must not know my existence...Of course I waited a bit before I planned to hack you guys because I wanted to have a little fun, but now you've ruined it."), 1) )
cs5.append( (SetDialogue, ("lex","Lex","But never mind! You'll be stuck in my playhouse for as long as I want! Ha ha he!"), 1) )
cs5.append( (SetDialogue, ("dexter","Dexter","That guy is getting to me!"), 1) )
cs5.append( (SetDialogue, ("may","May","Me too...Wait. That's it, Dex!"), 1) )
cs5.append( (SetDialogue, ("dexter","Dexter","What?"), 1) )
cs5.append( (SetDialogue, ("may","May","'Primordial emotional development'! This guys acts like a kid, so we can pull his strings!"), 1) )
cs5.append( (SetDialogue, ("dexter","Dexter","You mean scare him or make him angry?"), 1) )
cs5.append( (SetDialogue, ("may","May","Exactly! "), 1) )
cs5.append( (SetDialogue, ("dexter","Dexter","Huh...that might just work!"), 1) )
cs5.append( (SetDialogue, ("may","May","Well then, let's find that creep!"), 1) )
cs5.append( (s.stateList["room"].NextLevel, None, 0) )

def PackageCutscene(m):
     global l, cs1, cs2, cs3, cs4, cs5
     if m.obj.name == "lever1":
          LoadCutscene(cs1,False)
     elif m.obj.name == "lever2":
          LoadCutscene(cs2,False)
     elif m.obj.name == "lever3":
          LoadCutscene(cs3,False)
     elif m.obj.name == "droid1":
          room.AddAlarm(l,150,(1,m.obj.origX,m.obj.origY,"droid1"))
     elif m.obj.name == "droid2":
          room.AddAlarm(l,150,(1,m.obj.origX,m.obj.origY,"droid2"))
     elif m.obj.name == "pack1" and m.collision_type != COLLISION_WALL:
          if  m.obj2.name=="player":
               LoadCutscene(cs5,True)
          
def PackageAlarm(m):
     if m.data[0]==1:
          id=room.AddObject("droid",m.data[1],m.data[2],m.data[3])
          o=room.GetObjectById(id)
          o.AddSubscriber(l,OBJECT_DESTROYED)
          
l=Listener(PackageCutscene,PackageAlarm)
room.GetObjectByName("lever1").AddSubscriber(l,OBJECT_ACTION)
room.GetObjectByName("lever2").AddSubscriber(l,OBJECT_ACTION)
room.GetObjectByName("lever3").AddSubscriber(l,OBJECT_ACTION)
room.GetObjectByName("droid1").AddSubscriber(l,OBJECT_DESTROYED)
room.GetObjectByName("droid2").AddSubscriber(l,OBJECT_DESTROYED)
room.GetObjectByName("pack1").AddSubscriber(l,OBJECT_COLLISION)

PlayMusic("three")
LoadCutscene(cs4)