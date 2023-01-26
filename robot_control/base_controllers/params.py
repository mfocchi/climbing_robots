# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 09:47:07 2019

@author: student
"""

import numpy as np

robot_params = {}

robot_params['climbingrobot'] ={'dt': 0.001,
                       'kp': np.array([0 ,    0,    400,  100,    50,   50,    50, 30, 30]),
                       'kd':  np.array([0,    0,    10,   10,     10,   10,     4,   4, 4  ]),

                       'q_0':  np.array([ 0, 0, 8.0, 0,0,0, -1.57, 0.0, 0.0 ]),
                       'joint_names': ['mountain_wire_pitch', 'mountain_wire_roll',  'wire_base_prismatic',
                                       'wire_base_pitch', 'wire_base_roll','wire_base_yaw',
                                       'hip_pitch', 'hip_roll', 'knee'],
                       'ee_frame': 'foot',
                       'spawn_x' : 0.0,
                       'spawn_y' : 0.0,
                       'spawn_z' : 20.0, 
                       'buffer_size': 10000} # note the frames are all aligned with base for joints = 0



verbose = False
plotting = True


