import turtle
turtle.pen(fillcolor="black", pencolor="red", pensize=10)
turtle.pen()
{'pensize': 10, 'shown': True, 'resizemode': 'auto', 'outline': 1,
'pencolor': 'red', 'pendown': True, 'fillcolor': 'black',
'stretchfactor': (1,1), 'speed': 3, 'shearfactor': 0.0}
penstate=turtle.pen()
turtle.color("yellow","")
turtle.penup()
turtle.pen()
{'pensize': 10, 'shown': True, 'resizemode': 'auto', 'outline': 1,
'pencolor': 'yellow', 'pendown': False, 'fillcolor': '',
'stretchfactor': (1,1), 'speed': 3, 'shearfactor': 0.0}
turtle.pen(penstate, fillcolor="green")
turtle.pen()
{'pensize': 10, 'shown': True, 'resizemode': 'auto', 'outline': 1,
'pencolor': 'red', 'pendown': True, 'fillcolor': 'green',
'stretchfactor': (1,1), 'speed': 3, 'shearfactor': 0.0}
