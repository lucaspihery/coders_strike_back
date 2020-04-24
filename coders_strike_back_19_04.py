import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

POD_RADIUS = 400
thrust = "100"
boost_status = 1
toggle_shield = 0
shield_timer = 0

def print_instructions(x, y, thrust):
    print(str(next_checkpoint_x) + " " + str(next_checkpoint_y) + " " + str(thrust))

def debug():
    print("Distance 1 : " + str(next_checkpoint_dist)+" Distance 2 : " + str(next_checkpoint_dist2)+" Angle : "+str(next_checkpoint_angle)+" Vitesse : "+str(thrust)
    +" Boost : "+str(boost_status), file=sys.stderr)
    print("Toggle Shield : " + str(toggle_shield)+" Shield Timer : "+str(shield_timer), file=sys.stderr)
    print("Delta X : " + str(delta_x)+" Delta Y : "+str(delta_y), file=sys.stderr)
# game loop
while True:
    # next_checkpoint_x: x position of the next check point
    # next_checkpoint_y: y position of the next check point
    # next_checkpoint_dist: distance to the next checkpoint
    # next_checkpoint_angle: angle between your pod orientation and the direction of the next checkpoint
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]
    
    delta_x1 = abs(next_checkpoint_x - x)
    delta_y1 = abs(next_checkpoint_y - y)
    
    delta_x2 = abs(next_checkpoint_x - opponent_x)
    delta_y2 = abs(next_checkpoint_y - opponent_y)
    
    delta_x = abs(x - opponent_x)
    delta_y = abs(y - opponent_y)
    
    next_checkpoint_dist2 = delta_x2 + delta_y2
    
    
    if boost_status == 0 and next_checkpoint_dist < 1700 and next_checkpoint_dist2 < 1700 and delta_x < 900 and delta_y < 900:
        toggle_shield = 1
    
    if toggle_shield == 1 and shield_timer != 2:
        thrust = "SHIELD"
        shield_timer += 1
    else:
        toggle_shield = 0
        shield_timer = 0
        if abs(next_checkpoint_angle) > 90:
            thrust = "0"
        else:
            if next_checkpoint_dist < 1000:
                thrust = "50"
                if next_checkpoint_dist < 500:
                    thrust = "30"        
            else:
                thrust = "100"
    
    if next_checkpoint_dist > 5000 and next_checkpoint_angle == 0 and boost_status == 1:
        thrust = "BOOST"
        boost_status = 0
        
        
    print_instructions(x, y, thrust)
    debug()
    