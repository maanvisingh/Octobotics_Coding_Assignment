#! /usr/bin/env python3

import rospy
import rospkg
import sys
from inverted_pendulum_sim.srv import SetParams, SetParamsRequest

rospy.init_node('task1_client')
rospy.wait_for_service('/inverted_pendulum/set_params')
set_params_service = rospy.ServiceProxy('/inverted_pendulum/set_params', SetParams)
set_params_object = SetParamsRequest()
set_params_object.pendulum_mass = 2.0
set_params_object.pendulum_length = 300
set_params_object.cart_mass = 0.5
set_params_object.theta_0 = 0.0
set_params_object.theta_dot_0 = 0.0
set_params_object.theta_dot_dot_0 = 0.0
set_params_object.cart_x_0 = 0.0
set_params_object.cart_x_dot_0 = 0.0
set_params_object.cart_x_dot_dot_0 = 0.0
result = set_params_service(set_params_object)
print(result)
