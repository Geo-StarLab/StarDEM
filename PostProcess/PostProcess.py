# ---------------Name: StarDEM -------------------
# ------------Author: Chengshun Shang-------------
# -----------------Date: 04-01-2022---------------
# ---------------License : BSD license------------

import os
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

class PostProcess():

    def __init__(self) -> None:
        pass

    # show results in pyplot
    def plot_results(self):

        self.plot_p_x = []
        self.plot_p_y = []
        self.plot_p_r = []

        for p_pram_dict in self.my2dData.p_pram_list:

            self.plot_p_x.append(p_pram_dict["p_x"])
            self.plot_p_y.append(p_pram_dict["p_y"])
            self.plot_p_r.append(p_pram_dict["radius"])

        plt.figure(figsize=(self.L,self.W))
        plt.scatter(self.plot_p_x, self.plot_p_y, s = self.plot_p_r)
        plt.xlim((0, self.L))
        plt.ylim((0, self.W))

        plt.show()
    
    #write out data for Paraview analysis
    def WriteOutParaview(self, my2dData):

        self.my2dData = my2dData

        self.outName = './ResultsOutput/results.csv'

        # clean the exsisted file first
        if os.path.isfile(self.outName):
            os.remove(self.outName)
        
        with open(self.outName,'a') as f:
            # write the particle information
            f.write("\"x\", \"y\", \"z\", \"r scale\" \n")
            for p_pram_dict in self.my2dData.p_pram_list:
                f.write(str(p_pram_dict["p_x"]) + ', ' + str(p_pram_dict["p_y"]) + ', 0, ' + str(p_pram_dict["radius"]) + '\n')
            f.close()
        print("Successfully write out CSV file!")