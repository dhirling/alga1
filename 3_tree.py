from turtle import *
  
speed('fastest')
  
# felfele nézzünk
rt(-90)
  
# elfordulási szög az alaphoz képest
angle = 30
  
# Y alakú elágazás rajzolása l hosszal, 'level' mélységgel
def y(l, level):   
  
    if level > 0:
        colormode(255)
          
        # rgb skála szétosztása
        pencolor(0, 255//level, 0)
          
        # alap rajzolása
        fd(l)
  
        rt(angle)
  
        # jobb "részfa" megrajzolása
        y(0.8 * l, level-1)
          
        pencolor(0, 255//level, 0)
          
        lt( 2 * angle )
  
        # bal "részfa" megrajzolása
        y(0.8 * l, level-1)
          
        pencolor(0, 255//level, 0)
          
        rt(angle)
        fd(-l)
           
w = Screen()
y(70, 7)
w.exitonclick()