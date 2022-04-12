# ---------------Name: StarDEM -------------------
# ------------Author: Chengshun Shang-------------
# -----------------Date: 04-01-2022---------------
# ---------------License : BSD license------------

import random

class getInitialParticleData():

    def __init__(self) -> None:
        
        self.p_pram_list = []

    def creat_disk(self, L, W, r):
        self.p_id = 1
        self.i_row = 1
        self.i_col = 1
        self.L = L
        self.W = W
        self.r = r
        while self.i_row <= self.L/(2*self.r):
            while self.i_col <= self.W/(2*self.r):
                self.p_x = (2*self.i_row-1)*self.r
                self.p_y = (2*self.i_col-1)*self.r
                self.p_pram_dict = {
                    "id" : self.p_id,
                    "p_x" : self.p_x,
                    "p_y" : self.p_y,
                    # "radius" : self.r * random.randint(1, 10) / 10,
                    "radius" : self.r,
                    "p_v_x" : 0.0,
                    "p_v_y" : 0.0
                    }
                self.p_pram_list.append(self.p_pram_dict)
                self.p_id = self.p_id + 1
                self.i_col += 1
                print("**%s  " % self.i_col)
            self.i_row += 1
            self.i_col = 1
            print(self.i_row)
        print("Creat disk finished!\t")