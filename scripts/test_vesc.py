#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
from vesc_msgs.msg import VescStateStamped

def callback(data):
  print "Duty: " + str(data.state.duty_cycle) + ", RPM: " + str(data.state.speed)

sense_topic = rospy.get_param('sense_topic', 'sensors/core')
duty_topic = rospy.get_param('duty_topic', 'commands/motor/duty_cycle')
rpm_topic = rospy.get_param('rpm_topic', 'commands/motor/speed')

print sense_topic, duty_topic, rpm_topic

pub_duty = rospy.Publisher(duty_topic, Float64, queue_size=10)
pub_rpm = rospy.Publisher(rpm_topic, Float64, queue_size=10)
rospy.Subscriber(sense_topic, VescStateStamped, callback)

rospy.init_node('test_vesc')

while not rospy.is_shutdown():
  pub_duty.publish(1.0)
  pub_rpm.publish(1000)
  rospy.sleep(1.0)

