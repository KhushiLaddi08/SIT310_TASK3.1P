#!/usr/bin/env python3

# Import Dependencies
import rospy 
from geometry_msgs.msg import Twist 
import time 

def move_turtle_square(): 
    rospy.init_node('turtlesim_square_node', anonymous=True)
    
    # Init publisher
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10) 
    rospy.loginfo("Turtles are great at drawing squares!")

    ########## YOUR CODE GOES HERE ##########

    # Create Twist objects for different movements
    Move_forward = Twist()
    Move_forward.linear.x = 1

    Move_left = Twist()
    Move_left.angular.z = 1

    Move_backward = Twist()
    Move_backward.linear.x = -1

    Move_right = Twist()
    Move_right.angular.z = -1

    # Move in a square pattern
    for _ in range(4):
        # Move forward for 2 seconds
        velocity_publisher.publish(Move_forward)
        time.sleep(2)

        # Stop the turtlebot
        velocity_publisher.publish(Twist())
        time.sleep(1)

        # Turn left for 1 second
        velocity_publisher.publish(Move_left)
        time.sleep(1)

        # Stop the turtlebot
        velocity_publisher.publish(Twist())
        time.sleep(1)

    ###########################################

if __name__ == '__main__': 
    try: 
        move_turtle_square() 
    except rospy.ROSInterruptException: 
        pass
