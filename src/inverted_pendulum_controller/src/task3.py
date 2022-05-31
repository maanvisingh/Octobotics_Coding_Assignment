#!/usr/bin/env python3

import rospy
import rospkg
import sys
from inverted_pendulum_sim.msg import CurrentState
from inverted_pendulum_sim.msg import ControlForce
from simple_pid import PID
from math import pi
from inverted_pendulum_sim.srv import SetParams, SetParamsRequest

rospy.wait_for_service('/inverted_pendulum/set_params')
set_params_service = rospy.ServiceProxy('/inverted_pendulum/set_params', SetParams)
set_params_object = SetParamsRequest()
set_params_object.pendulum_mass = 2.0
set_params_object.pendulum_length = 300
set_params_object.cart_mass = 0.5
set_params_object.theta_0 = 3
set_params_object.theta_dot_0 = 0.0
set_params_object.theta_dot_dot_0 = 0.0
set_params_object.cart_x_0 = 0.0
set_params_object.cart_x_dot_0 = 0.0
set_params_object.cart_x_dot_dot_0 = 0.0
result = set_params_service(set_params_object)

rospy.init_node("task3", anonymous=True)
pub = rospy.Publisher('/inverted_pendulum/control_force', ControlForce , queue_size=10)

rate = rospy.Rate(100)              
force_obj = ControlForce()  
pid = PID(80, 20, 25, setpoint = 3.14)
pid.output_limits = (-10, 10)
theta = pi
cur_theta = 0       
 
def callback(msg):
    cur_theta = msg.curr_theta
    if cur_theta < 0.0:
        cur_theta = 2*theta + cur_theta
    force_obj.force = pid(cur_theta)
    pub.publish(force_obj)

sub = rospy.Subscriber('/inverted_pendulum/current_state', CurrentState, callback)          
rospy.spin()



