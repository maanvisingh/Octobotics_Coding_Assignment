#! /usr/bin/env python3

import rospy                             
from inverted_pendulum_sim.msg import ControlForce        
from math import sin, pi

rospy.init_node('task2_pub')         
pub = rospy.Publisher('/inverted_pendulum/control_force', ControlForce, queue_size=10)                              

rate = rospy.Rate(100)              
force_obj = ControlForce()                            
force_obj.force = 0
frequency = 10   
amplitude = 30                 
t = 0

while not rospy.is_shutdown():             
  pub.publish(force_obj)
  t += 0.001
  force_obj.force = amplitude*sin(2*pi*frequency*t)   # y(t) = Asin(2πft+φ)
  rate.sleep()        
 
                    