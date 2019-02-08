import turtle
def sq(n,a):
  screen = turtle.Screen()
  screen.bgcolor('green')
  tr=turtle.Turtle()
  tr.shape('turtle')
  tr.color('blue')
  for i in range(20):
    for i in range(n):
      tr.forward(50)
      tr.left(a)


n=int(input('enter no of sides:'))
a=int(input('enter a value:'))
sq(n,a)
      
