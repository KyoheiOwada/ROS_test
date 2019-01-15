#!/usr/bin/env python 
import rospy
import RPi.GPIO as GPIO
from std_msgs.msg import UInt16
OUTPUT = 2
PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN,GPIO.OUT)
pwm = GPIO.PWM(PIN,1000)
pwm.start(0.0)

def callback(message):
	pwm.ChangeDutyCycle(message.data)

if __name__ == '__main__':
	rospy.init_node('pwm_led')
	sub = rospy.Subscriber('value',UInt16,callback)
	rospy.spin()
	GPIO.cleanup()
	pwm.stop()
