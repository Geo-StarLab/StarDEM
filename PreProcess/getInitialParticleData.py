# ---------------Name: StarDEM -------------------
# ------------Author: Chengshun Shang-------------
# -----------------Date: 04-01-2022---------------
# ---------------License : BSD license------------

import random
import math
import numpy as np
import matplotlib.pyplot as plt
import os

class getInitialParticleData():

    def __init__(self) -> None:
        
        self.p_pram_list = []

    def creat_disk(self, L, W, r, is_round):
        self.p_id = 1
        self.i_row = 1
        self.i_col = 1
        self.L = L
        self.W = W
        self.r = r
        self.is_round = is_round
        while self.i_row <= self.L / ( 2 * self.r):
            while self.i_col <= self.W / ( 2 * self.r):
                if self.is_round:
                    self.p_x = round(((2 * self.i_row - 1) * self.r), 2)
                    self.p_y = round(((2 * self.i_col - 1) * self.r), 2)
                else:
                    self.p_x = (2 * self.i_row - 1) * self.r
                    self.p_y = (2 * self.i_col - 1) * self.r
                self.p_pram_dict = {
                    "id" : self.p_id,
                    "p_x" : self.p_x,
                    "p_y" : self.p_y,
                    "p_z" : 0.0,
                    # "radius" : self.r * random.randint(1, 10) / 10,
                    "radius" : self.r,
                    "p_v_x" : 0.0,
                    "p_v_y" : 0.0,
                    "p_v_z" : 0.0,
                    }
                self.p_pram_list.append(self.p_pram_dict)
                self.p_id = self.p_id + 1
                self.i_col += 1
                #print("**%s  " % self.i_col)
            self.i_row += 1
            self.i_col = 1
            #print(self.i_row)
        print("Creat disk finished!\t")
    
    def creat_sphere(self, L, W, T, r, is_round):
        self.p_id = 1
        self.i_row = 1
        self.i_col = 1
        self.i_thick = 1
        self.L = L
        self.W = W
        self.T = T
        self.r = r
        self.is_round = is_round
        while self.i_row <= self.L / ( 2 * self.r):
            while self.i_col <= self.W / ( 2 * self.r):
                while self.i_thick <= self.T / ( 2 * self.r):
                    if self.is_round:
                        self.p_x = round(((2.0 * self.i_row - 1.0) * self.r), 2)
                        self.p_y = round(((2.0 * self.i_col - 1.0) * self.r), 2)
                        self.p_z = round(((2.0 * self.i_thick - 1.0) * self.r), 2)
                    else:
                        self.p_x = (2.0 * self.i_row - 1.0) * self.r
                        self.p_y = (2.0 * self.i_col - 1.0) * self.r
                        self.p_z = (2.0 * self.i_thick - 1.0) * self.r
                    self.p_pram_dict = {
                        "id" : self.p_id,
                        "p_x" : self.p_x,
                        "p_y" : self.p_y,
                        "p_z" : self.p_z,
                        # "radius" : self.r * random.randint(1, 10) / 10,
                        "radius" : self.r,
                        "p_v_x" : 0.0,
                        "p_v_y" : 0.0,
                        "p_v_z" : 0.0
                        }
                    self.p_pram_list.append(self.p_pram_dict)
                    self.p_id = self.p_id + 1
                    self.i_thick += 1
                self.i_col += 1
                self.i_thick = 1
            self.i_row += 1
            self.i_col = 1
        print("Creat spheres finished!\t")


    def creat_membrane(self, H, r_in, r_m, p_id_ini):
        self.p_id = p_id_ini
        self.i_layer = 1
        self.H = H
        self.r_in = r_in
        self.r_m = r_m
        self.m_x_0 = 0.0
        self.m_z_0 = 0.0

        self.temp_circle_num = (2 * math.pi * (self.r_in + self.r_m)) // (2 * self.r_m)
        if (2 * self.r_m * self.temp_circle_num) < (2 * math.pi * (self.r_in + self.r_m)):
            self.r_m = (2 * math.pi * (self.r_in + self.r_m)) / (2 * (self.temp_circle_num + 1))

        while self.i_layer <= ((self.H - 2 * self.r_m) / ( 1.732 * self.r_m) + 1):

            #in this case, y is the verticle direction
            self.p_y = self.r_m + (self.i_layer - 1) * ( 1.732 * self.r_m)

            for angle in np.arange(0, 360, (360 / (self.temp_circle_num + 1))):
                
                self.p_x = self.m_x_0 + (self.r_in + self.r_m) * math.cos((angle + (self.i_layer - 1) * (180 / (self.temp_circle_num + 1))) * math.pi / 180)
                self.p_z = self.m_z_0 + (self.r_in + self.r_m) * math.sin((angle + (self.i_layer - 1) * (180 / (self.temp_circle_num + 1))) * math.pi / 180)

                self.p_pram_dict = {
                    "id" : self.p_id,
                    "p_x" : self.p_x,
                    "p_y" : self.p_y,
                    "p_z" : self.p_z,
                    # "radius" : self.r * random.randint(1, 10) / 10,
                    "radius" : self.r_m,
                    "p_v_x" : 0.0,
                    "p_v_y" : 0.0,
                    "p_v_z" : 0.0
                    }

                self.p_pram_list.append(self.p_pram_dict)
                self.p_id = self.p_id + 1

            self.i_layer += 1
        print("Creat spheres finished!\t")

    def getParticleDataFromMdpa(self, aim_mdpa_file_name):
        
        self.p_id = 1
        self.p_record_nodes = False
        self.p_record_elements = False
        self.p_record_radius = False

        if os.path.isfile(aim_mdpa_file_name):
            
            with open(aim_mdpa_file_name, 'r') as mdpa_data:

                for line in mdpa_data:

                    self.p_pram_dict = {
                    "id" : 0,
                    "p_x" : 0.0,
                    "p_y" : 0.0,
                    "p_z" : 0.0,
                    "radius" : 0.0,
                    "p_v_x" : 0.0,
                    "p_v_y" : 0.0,
                    "p_v_z" : 0.0,
                    "p_ele_id": 0,
                    "p_group_id": 0
                    }
                            
                    values = [str(s) for s in line.split()]

                    if len(values) > 1:
                        if values[0] == 'Begin' and values[1] == 'Nodes':
                            self.p_record_nodes = True
                            continue
                        elif values[0] == 'End' and values[1] == 'Nodes':
                            self.p_record_nodes = False

                        if values[0] == 'Begin' and values[1] == 'Elements':
                            self.p_record_elements = True
                            continue
                        elif values[0] == 'End' and values[1] == 'Elements':
                            self.p_record_elements = False

                    if len(values) > 2:
                        if values[0] == 'Begin' and values[2] == 'RADIUS':
                            self.p_record_radius = True
                            continue
                    if len(values) > 1:
                        if values[0] == 'End' and values[1] == 'NodalData' and self.p_record_radius == True:
                            self.p_record_radius = False

                    if self.p_record_nodes:
                        self.p_pram_dict["id"] = int(values[0])
                        self.p_pram_dict["p_x"] = float(values[1])
                        self.p_pram_dict["p_y"] = float(values[2])
                        self.p_pram_dict["p_z"] = float(values[3])

                    if self.p_record_elements:
                        #only modify the values, not add new one
                        temp_p_pram_dict = next(old_p_pram_dict for old_p_pram_dict in self.p_pram_list if old_p_pram_dict['id'] == int(values[2]))
                        temp_p_pram_dict["p_ele_id"] = int(values[0])

                    if self.p_record_radius:
                        #only modify the values, not add new one
                        temp_p_pram_dict = next(old_p_pram_dict for old_p_pram_dict in self.p_pram_list if old_p_pram_dict['id'] == int(values[0]))
                        temp_p_pram_dict["radius"] = float(values[2])

                    if not (self.p_record_elements and self.p_record_radius):
                        if self.p_record_nodes:
                            self.p_pram_list.append(self.p_pram_dict)
                            self.p_id = self.p_id + 1

        self.p_pram_list = sorted(self.p_pram_list, key=lambda d: d['id'])

        print("Read mdpa file finished!\t")

    def setParticleGroupID(self, sample_height, sample_width, joint_angle, joint_width_1, joint_width_2, p_pram_list):
        
        # usually, we set the sample base at 0,0,0

        if joint_angle != 90:

            joint_k = math.tan(joint_angle * math.pi / 180)
            intercept_add_joint_1 =  joint_width_1 / math.cos(joint_angle * math.pi / 180)

            for p_pram_dict in p_pram_list:

                intercept_b = -0.5 * sample_height
            
                while intercept_b < (1.5 * sample_height):
                    
                    if p_pram_dict["p_y"] > (p_pram_dict["p_x"] * joint_k + intercept_b) \
                        and p_pram_dict["p_y"] < (p_pram_dict["p_x"] * joint_k + intercept_b + intercept_add_joint_1):
                        
                        p_pram_dict["p_group_id"] = 1
                        break

                    intercept_b += (joint_width_1 + joint_width_2) / math.cos(joint_angle * math.pi / 180)

        else:

            step_x_add_joint_1 = joint_width_1

            for p_pram_dict in p_pram_list:

                step_x = -1.0 * sample_width
            
                while step_x < sample_width:
                    
                    if p_pram_dict["p_x"] > step_x and p_pram_dict["p_x"] < (step_x + step_x_add_joint_1):
                        
                        p_pram_dict["p_group_id"] = 1
                        break

                    step_x += (joint_width_1 + joint_width_2)

        print("Set group ID finished!\t")

    def setParticleGroupIDSingle(self, sample_height, joint_angle, joint_width_1, p_pram_list):
        
        # usually, we set the sample base at 0,0,0

        if joint_angle != 90:

            joint_k = math.tan(joint_angle * math.pi / 180)
            intercept_add_joint_1 =  joint_width_1 / math.cos(joint_angle * math.pi / 180)

            for p_pram_dict in p_pram_list:

                intercept_b = 0.5 * sample_height - 0.5 * intercept_add_joint_1
                    
                if p_pram_dict["p_y"] > (p_pram_dict["p_x"] * joint_k + intercept_b) \
                    and p_pram_dict["p_y"] < (p_pram_dict["p_x"] * joint_k + intercept_b + intercept_add_joint_1):
                    
                    p_pram_dict["p_group_id"] = 1

        else:

            step_x_add_joint_1 = joint_width_1

            for p_pram_dict in p_pram_list:

                step_x = -0.5 * joint_width_1
                    
                if p_pram_dict["p_x"] > step_x and p_pram_dict["p_x"] < (step_x + step_x_add_joint_1):
                    
                    p_pram_dict["p_group_id"] = 1

        print("Set group ID finished!\t")