import turtle
colors=['red','green','yellow','orange','blue','purple']
t=turtle.Pen()
for x in range(50):
    t.pencolor(colors[x%6])
    t.forward(x)
    t.left(59)
