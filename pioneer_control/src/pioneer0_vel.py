#!/usr/bin/env python

# imports
import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3

# parameters
pioneer0_cmd_vel = '/pioneer_0/RosAria/cmd_vel'
#pioneer1_cmd_vel = '/pioneer_1/RosAria/cmd_vel'
update_interval = 0.1 # [s]
pioneer0_vel_lin = 0.3 # [m/s]
pioneer0_vel_ang = 0.6 # [rad/s]
#pioneer1_vel_lin = 0.3 # [m/s]
#pioneer1_vel_ang = 0.0 # [rad/s]

# launch node and create a publisher
rospy.init_node('cmd_vel_test')
pioneer0_pub = rospy.Publisher(pioneer0_cmd_vel, Twist)
#pioneer1_pub = rospy.Publisher(pioneer1_cmd_vel, Twist)

# loop until shutdown
while not rospy.is_shutdown():

	# publish the defined linear and angular velocity
	pioneer0_pub.publish(Twist(Vector3(pioneer0_vel_lin, 0, 0), Vector3(0, 0, pioneer0_vel_ang)))
	
	# sleep the defined interval
	rospy.sleep(update_interval)
