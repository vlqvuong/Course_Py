def turn_right():
    turn_left()
    turn_left()
    turn_left()

def step():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    step()
    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
