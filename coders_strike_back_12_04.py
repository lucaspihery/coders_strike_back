import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


# game loop
while True:
    # next_checkpoint_x: x position of the next check point
    # next_checkpoint_y: y position of the next check point
    # next_checkpoint_dist: distance to the next checkpoint
    # next_checkpoint_angle: angle between your pod orientation and the direction of the next checkpoint
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]
    
    
    
    #angle
    if abs(next_checkpoint_angle) > 90:
        thrust = "0"
    else:
        thrust = "100"
        if next_checkpoint_dist > 7000 and next_checkpoint_angle == 0:
            thrust = "BOOST"
        
    print(str(next_checkpoint_x) + " " + str(next_checkpoint_y) + " " + str(thrust))
    print("Distance : " + str(next_checkpoint_dist)+ " Angle : "+str(next_checkpoint_angle)+" Vitesse : "+str(thrust), file=sys.stderr)