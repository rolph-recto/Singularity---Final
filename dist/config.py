config["TITLE"]="Singularity"
config["ICON_TITLE"]="ZE3"
config["ICON"]="zero.bmp"
config["DISPLAY_FLAGS"]=0
config["SCREEN_WIDTH"]=512
config["SCREEN_HEIGHT"]=416
config["FONT_FILE"]="LiberationMono-Regular.ttf"
config["FONT_SIZE"]=12
config["FONT_COLOR"]=Color(255,255,255)
config["FONT_SPACING"]=2
config["VIEW_WIDTH"]=16
config["VIEW_HEIGHT"]=11
config["VIEW_POSX"]=0
config["VIEW_POSY"]=32
config["DATABASE"]="resource.txt"
config["TILE_TEMPLATE"]="main2"
config["LEVELS"]=["A","D","C","B","E"]
config["KEYREPEAT_DELAY"]=100
config["KEYREPEAT_INTERVAL"]=10
config["PARTICLE_TEMPLATES"]=[]
config["GUNRECOIL_X"]=0
config["GUNRECOIL_Y"]=0
config["RELOAD_TIME"]=15
config["OFFSET_FACTOR"]=4

diamond=Polygon([[0,-10], [-10,0], [0,10], [10,0]], 0, 0)
pt=ParticleTemplate("diamond",diamond)
pt.life=20
pt.gravity=1.0
pt.fall=False
pt.color=Color(0,128,255,255)
pt.decay=Color(0,-5,-10,0)
pt.fill=False
config["PARTICLE_TEMPLATES"].append(pt)
     
pt5=ParticleTemplate("diamond2",diamond)
pt5.life=20
pt5.gravity=1.0
pt5.fall=False
pt5.color=Color(255,0,0,255)
pt5.decay=Color(5,-15,0,0)
pt5.fill=False
config["PARTICLE_TEMPLATES"].append(pt5)

circle=Circle(0,0,4)
pt2=ParticleTemplate("circle",circle)
pt2.life=20
pt2.gravity=1.0
pt2.fall=False
pt2.color=Color(255,230,230,255)
pt2.decay=Color(0,30,50,0)
pt2.fill=True
config["PARTICLE_TEMPLATES"].append(pt2)
          
circle=Circle(0,0,10)
pt3=ParticleTemplate("circle2",circle)
pt3.life=45
pt3.gravity=1.0
pt3.fall=False
pt3.color=Color(0,255,255,255)
pt3.decay=Color(0,10,20,0)
pt3.fill=False
config["PARTICLE_TEMPLATES"].append(pt3)
          
circle=Circle(0,0,8)
pt4=ParticleTemplate("circle3",circle)
pt4.life=45
pt4.gravity=1.0
pt4.fall=True
pt4.color=Color(255,0,0,255)
pt4.decay=Color(0,10,20,0)
pt4.fill=False
config["PARTICLE_TEMPLATES"].append(pt4)

circle=Circle(0,0,20)
pt6=ParticleTemplate("circle4",circle)
pt6.life=60
pt6.gravity=1.0
pt6.fall=False
pt6.color=Color(255,255,255,255)
pt6.decay=Color(10,10,10,0)
pt6.fill=False
config["PARTICLE_TEMPLATES"].append(pt6)

circle=Circle(0,0,8)
pt7=ParticleTemplate("circle5",circle)
pt7.life=45
pt7.gravity=1.0
pt7.fall=False
pt7.color=Color(150,150,150,255)
pt7.decay=Color(10,10,10,0)
pt7.fill=False
config["PARTICLE_TEMPLATES"].append(pt7)

circle=Circle(0,0,8)
pt8=ParticleTemplate("circle6",circle)
pt8.life=45
pt8.gravity=1.0
pt8.fall=False
pt8.color=Color(0,255,0,255)
pt8.decay=Color(0,0,-10,0)
pt8.fill=False
config["PARTICLE_TEMPLATES"].append(pt8)

circle=Circle(0,0,8)
pt9=ParticleTemplate("circle7",circle)
pt9.life=20
pt9.gravity=1.0
pt9.fall=False
pt9.color=Color(0,255,150,255)
pt9.decay=Color(0,10,10,0)
pt9.fill=False
config["PARTICLE_TEMPLATES"].append(pt9)

circle=Circle(0,0,6)
pt10=ParticleTemplate("circle8",circle)
pt10.life=20
pt10.gravity=1.0
pt10.fall=False
pt10.color=Color(0,150,50,255)
pt10.decay=Color(0,5,3,0)
pt10.fill=True
config["PARTICLE_TEMPLATES"].append(pt10)

circle=Circle(0,0,6)
pt11=ParticleTemplate("circle9",circle)
pt11.life=20
pt11.gravity=1.0
pt11.fall=False
pt11.color=Color(0,150,200,255)
pt11.decay=Color(0,3,5,0)
pt11.fill=True
config["PARTICLE_TEMPLATES"].append(pt11)

config["SPLASH_DIALOGUE"]=[]
config["SPLASH_DIALOGUE"].append("Last Entry.")
config["SPLASH_DIALOGUE"].append("The test results came in. They're gone.")
config["SPLASH_DIALOGUE"].append("Absolutely gone.")
config["SPLASH_DIALOGUE"].append("Scanner cannot trace any agents in the server.")
config["SPLASH_DIALOGUE"].append("...Our fatal mistake was not keeping the server isolated.")
config["SPLASH_DIALOGUE"].append("But I don't understand...")
config["SPLASH_DIALOGUE"].append("There is no code for the agents to exit...")
config["SPLASH_DIALOGUE"].append("Let alone disobey a terminate command.")
config["SPLASH_DIALOGUE"].append("Then again there were a lot of unexpected things.")
config["SPLASH_DIALOGUE"].append("So...Singularity failed. Project Genesis will be scrapped.")
config["SPLASH_DIALOGUE"].append("Eventually, maybe a couple years or so, the agents will break down...")
config["SPLASH_DIALOGUE"].append("Be destroyed by an anti-virus somewhere...I hope.")

config["END_DIALOGUE"]=[]
config["END_DIALOGUE"].append("Lex went down with his playhouse.")
config["END_DIALOGUE"].append("Unfortunately, there are still a lot of agents out in the Network...")
config["END_DIALOGUE"].append("I know we have to stop them, but...they're essentially people.")
config["END_DIALOGUE"].append("People with no bodies, only minds...")
config["END_DIALOGUE"].append("I know now that we cannot create intelligence.")
config["END_DIALOGUE"].append("Because even if we can, we can't control them.")
config["END_DIALOGUE"].append("I'm just glad we made it through this alive.")
config["END_DIALOGUE"].append("We'll go down to the department tomorrow and tell them everthing.")
config["END_DIALOGUE"].append("...they'll might not believe us though.")
config["END_DIALOGUE"].append("Then again, who would believe you when you tell them that software,")
config["END_DIALOGUE"].append("An endless string of 1s and 0s, can be human?")