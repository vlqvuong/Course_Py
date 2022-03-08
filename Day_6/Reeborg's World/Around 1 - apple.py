move()
while not at_goal():
    if front_is_clear():
        if object_here("apple"):
            take("apple")
        else:
            move()
    else:
        turn_left()

    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
