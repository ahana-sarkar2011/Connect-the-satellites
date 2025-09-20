import pgzrun
import random

WIDTH = 700
HEIGHT = 500

sats=[]
lines=[]
next = 0

for i in range(10):
    satellite = Actor("satellite")
    satellite.x = random.randint(10,680)
    satellite.y = random.randint(10,480)
    sats.append(satellite)
def draw():
    screen.blit("background",(0,0))
    number=1
    for i in sats:
        i.draw()
        screen.draw.text(str(number),(i.x,i.y+15),color ="red")
        number+=1
    for l in lines:
        screen.draw.line(l[0],l[1],"blue")

def on_mouse_down(pos):
    global next, lines
    if sats[next].collidepoint(pos):
        if next > 0:
            lines.append((sats[next-1].pos,sats[next].pos))
        next+=1
    else:
        lines=[]
        next=0

pgzrun.go()