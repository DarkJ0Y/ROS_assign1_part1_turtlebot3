#!/usr/bin/env python3

import rospy

from std_msgs.msg import String
from geometry_msgs.msg import Twist

class Commander:
    def __init__(self) -> None:
        rospy.init_node('commander', anonymous = True)
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 1)

        rospy.Subscriber('/sudipto_command', String, self.command_callback)

    def command_callback(self, data):
        rospy.loginfo("Command received : {}".format(data.data))

        velocity = Twist()

        # Separate integers and strings
        integers = ''.join(filter(str.isdigit, data.data))
        strings = ''.join(filter(str.isalpha, data.data))

        # Convert integers to int
        integers = int(integers)
        
        if strings.lower() == 'forward':
            velocity.linear.x = integers*0.1
        elif strings.lower() == 'backward':
            velocity.linear.x = -1*integers*0.1
        elif strings.lower() == 'left':
            velocity.angular.z = integers*0.1
        elif strings.lower() == 'right':
            velocity.linear.z = -1*integers*0.1

        self.pub.publish(velocity)

if __name__=='__main__':
    node = Commander()
    rospy.spin()