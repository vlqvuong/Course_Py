def turn_right():
    turn_left()
    turn_left()
    turn_left()

def step():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if not front_is_clear():
        step()
    else:
        move()
    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
