import turtle

scr = turtle.Screen()
board_state = [[0 for x in range(6)] for y in range(7)]
turn = 0
turtle.title("connect four")
turtle.bgcolor("black")
turtle.speed(360)

turtle.penup()
turtle.goto(-250,-250)
turtle.pendown()

turtle.color("blue")
turtle.begin_fill()
turtle.forward(490)
turtle.left(90)
turtle.forward(420)
turtle.left(90)
turtle.forward(490)
turtle.left(90)
turtle.forward(420)
turtle.end_fill()


def draw_circle(whichsqure, fillcolor):
    turtle.penup()
    turtle.setx(70*whichsqure[0] -250)
    turtle.sety(70*whichsqure[1]-215)
    turtle.pendown()
    turtle.color(fillcolor)
    turtle.begin_fill()
    turtle.circle(35)
    turtle.end_fill()
    turtle.hideturtle()


for i in range(42):
    whichsqure = i//6,i%6
    draw_circle(whichsqure, "black")



def apply_gravity(corr):
  global board_state
  for i in range(6):
    if board_state[corr[0]][i] == 0:
      return corr[0],i



def update_board(corr, turn):
  global board_state
  if turn%2 == 0:
    board_state[corr[0]][corr[1]] = 1
  elif turn%2==1:
    board_state[corr[0]][corr[1]] =2
    

  
  return board_state


def check_win(board_state):

  for i in range(6):
    for j in range(3):
      try:
        if board_state[i][j] == board_state[i][j+1] == board_state[i][j+2] == board_state[i][j+3] == 1:
          print(board_state)
          return 1
      except:
        pass
      try:  
        if board_state[i][j] == board_state[i][j+1] == board_state[i][j+2] == board_state[i][j+3] == 2:
          print(board_state)
          return 2
      except:
        pass
        
  for i in range(4):
    for j in range(4):
      try:
        if board_state[i][j] == board_state[i+1][j] == board_state[i+2][j] == board_state[i+3][j] == 1:
          print(board_state)
          return 1
      except:
        pass
      try:
        if board_state[i][j] == board_state[i+1][j] == board_state[i+2][j] == board_state[i+3][j] == 2:
          print(board_state)
          return 2
      except:
        pass
  for i in range(3):
    for j in range(3):
      try:
        if board_state[i][j] == board_state[i+1][j+1] == board_state[i+2][j+2] == board_state[i+3][j+3] == 1:
          return 1
      except:
        pass
      try:
        if board_state[i][j] == board_state[i+1][j+1] == board_state[i+2][j+2] == board_state[i+3][j+3] == 2:
          return 2
      except:
        pass
  return False


def play_turn(x, y):
  global turn, board_state
  won = check_win(board_state)
  if not won:
      turn += 1
      turtle.penup()
      turtle.goto(x, y)
      turtle.pendown()
      turtle.color("white")
      corr = int((x + 250)//70), int((y + 250)//70)
      if corr[0] not in range(7) or corr[1] not in range(6):
            turtle.write("Play a legal move" , font=("Arial", 20, "normal"), align="center")
            #turn -= 1
      else:
          corr = apply_gravity(corr)
          update_board(corr, turn)
          print(turn)
          if turn%2 == 0:
            draw_circle(corr, "yellow")
          elif turn%2== 1:
            draw_circle(corr, "red")


  else:
    turtle.color("white")
    turtle.write("GAME OVER Player "+str(won) +" WON" , font=("Arial", 20, "normal"), align="center")
    turtle.done()
    turtle.bye()


scr.onclick(play_turn)
scr.mainloop()
