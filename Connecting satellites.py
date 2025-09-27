import pgzrun
import random
from time import time

WIDTH = 700
HEIGHT = 500

sats=[]
lines=[]
next = 0
start = time()
gameover = False
win = False

for i in range(10):
    satellite = Actor("satellite")
    satellite.x = random.randint(10,680)
    satellite.y = random.randint(10,480)
    sats.append(satellite)
def draw():
    global total
    global win
    screen.blit("background",(0,0))
    number=1
    for i in sats:
        i.draw()
        screen.draw.text(str(number),(i.x,i.y+15),color ="red")
        number+=1
    for l in lines:
        screen.draw.line(l[0],l[1],"blue")
    if next < 10:
        total = time()-start
        total = round(total,1)
        screen.draw.text(str(total),(20,20))
    else:
        screen.draw.text(str(total),(20,20))
        if total<25:
            win = True
    if gameover == True:
        screen.fill("red")
        screen.draw.text("GAME OVER",(350,250),color="black", fontsize=70)
    if win == True:
        screen.fill("green")
        screen.draw.text("YOU WIN",(350,250),color="pink",fontsize=70)

def update():
    pass

def on_mouse_down(pos):
    global next, lines
    if sats[next].collidepoint(pos):
        if next > 0:
            lines.append((sats[next-1].pos,sats[next].pos))
        next+=1
    else:
        lines=[]
        next=0

def timeup():
    global gameover
    gameover = True
clock.schedule(timeup,25)

pgzrun.go()