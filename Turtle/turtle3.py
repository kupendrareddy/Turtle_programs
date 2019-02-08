import turtle
screen = turtle.Screen()
screen.bgcolor('green')
tr=turtle.Turtle()
tr.shape('turtle')
tr.color('blue')
def sq():
  for i in range(4):
    tr.forward(50)
    tr.left(90)

def sp():
  for i in range(18):
    sq()
    tr.right(20)
#n=int(input('enter no of sides:'))
#=int(input('enter a value:'))
sp()
