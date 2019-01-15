#!/usr/bin/env python
import rospy
import random
from std_msgs.msg import UInt16

if __name__ == '__main__':
	rospy.init_node('generate_num')
	pub = rospy.Publisher('value',UInt16,queue_size=100)
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		a = random.randint(0,100)
		pub.publish(a)
		rate.sleep()
