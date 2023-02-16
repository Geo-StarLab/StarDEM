# ---------------Name: StarDEM -------------------
# ------------Author: Chengshun Shang-------------
# -----------------Date: 04-01-2022---------------
# ---------------License : BSD license------------

import random
import math
import numpy as np

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
        self.x0 = 0.0
        self.z0 = 0.0

        self.temp_circle_num = (2 * math.pi * (self.r_in + self.r_m)) // (2 * self.r_m)
        if (2 * self.r_m * self.temp_circle_num) < (2 * math.pi * (self.r_in + self.r_m)):
            self.r_m = (2 * math.pi * (self.r_in + self.r_m)) / (2 * (self.temp_circle_num + 1))
        
        self.x0 += (self.r_in + self.r_m)

        while self.i_layer <= ((self.H - 2 * self.r_m) / ( 1.732 * self.r_m) + 1):

            #in this case, y is the verticle direction
            self.p_y = self.r_m + (self.i_layer - 1) * ( 1.732 * self.r_m)

            for angle in np.arange(0, 180, (self.temp_circle_num + 1)):

                self.p_x = self.x0 + (self.r_in + self.r_m) * math.cos((angle + (self.i_layer - 1) * (180 / (self.temp_circle_num + 1))) * math.pi / 180)
                self.p_z = self.z0 + (self.r_in + self.r_m) * math.sin((angle + (self.i_layer - 1) * (180 / (self.temp_circle_num + 1))) * math.pi / 180)

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