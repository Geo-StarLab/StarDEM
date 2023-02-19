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

        for p_pram_dict in self.myDEMData.p_pram_list:

            self.plot_p_x.append(p_pram_dict["p_x"])
            self.plot_p_y.append(p_pram_dict["p_y"])
            self.plot_p_r.append(p_pram_dict["radius"])

        plt.figure(figsize=(self.L,self.W))
        plt.scatter(self.plot_p_x, self.plot_p_y, s = self.plot_p_r)
        plt.xlim((0, self.L))
        plt.ylim((0, self.W))

        plt.show()
    
    #write out data for Paraview analysis
    def WriteOutParaview(self, myDEMData):

        self.myDEMData = myDEMData

        self.outName = './ResultsOutput/results.csv'

        # clean the exsisted file first
        if os.path.isfile(self.outName):
            os.remove(self.outName)
        
        with open(self.outName,'a') as f:
            # write the particle information
            f.write("\"x\", \"y\", \"z\", \"r scale\" \n")
            for p_pram_dict in self.myDEMData.p_pram_list:
                f.write(str(p_pram_dict["p_x"]) + ', ' + str(p_pram_dict["p_y"]) + ', ' + str(p_pram_dict["p_z"]) + ', ' + str(p_pram_dict["radius"]) + '\n')
            f.close()
        print("Successfully write out CSV file!")

    def WriteOutGIDData(self, myDEMData):
        
        self.myDEMData = myDEMData

        self.outName = './ResultsOutput/G-TriaxialDEM.mdpa'

        # clean the exsisted file first
        if os.path.isfile(self.outName):
            os.remove(self.outName)
        
        with open(self.outName,'a') as f:
            # write the particle information
            #f.write("Begin ModelPartData \n //  VARIABLE_NAME value \n End ModelPartData \n \n Begin Properties 0 \n End Properties \n \n Begin Nodes\n")
            #f.write("Begin Nodes\n")
            for p_pram_dict in self.myDEMData.p_pram_list:
                f.write(str(p_pram_dict["id"]) + ' ' + str(p_pram_dict["p_x"]) + ' ' + str(p_pram_dict["p_y"]) + ' ' + str(p_pram_dict["p_z"]) + '\n')
            #f.write("End Nodes \n \n")

            f.write("Begin Elements SphericContinuumParticle3D// GUI group identifier: Membrane \n")
            for p_pram_dict in self.myDEMData.p_pram_list:
                f.write(str(p_pram_dict["id"] - 647) + ' ' + ' 0 ' + str(p_pram_dict["id"]) + '\n')
            f.write("End Elements \n \n")

            f.write("Begin NodalData RADIUS // GUI group identifier: Membrane \n")
            for p_pram_dict in self.myDEMData.p_pram_list:
                f.write(str(p_pram_dict["id"]) + ' ' + ' 0 ' + str(p_pram_dict["radius"]) + '\n')
            f.write("End NodalData \n \n")

            f.write("Begin NodalData COHESIVE_GROUP // GUI group identifier: Membrane \n")
            for p_pram_dict in self.myDEMData.p_pram_list:
                f.write(str(p_pram_dict["id"]) + ' ' + ' 0 ' + " 2 " + '\n')
            f.write("End NodalData \n \n")

            #f.write("Begin NodalData SKIN_SPHERE \n End NodalData \n \n")

            f.write("Begin SubModelPart DEMParts_Membrane // Group Membrane // Subtree DEMParts \n Begin SubModelPartNodes \n")
            for p_pram_dict in self.myDEMData.p_pram_list:
                f.write(str(p_pram_dict["id"]) + '\n')
            f.write("End SubModelPartNodes \n Begin SubModelPartElements \n ")
            for p_pram_dict in self.myDEMData.p_pram_list:
                f.write(str(p_pram_dict["id"] - 647) + '\n')
            f.write("End SubModelPartElements \n")
            f.write("Begin SubModelPartConditions \n End SubModelPartConditions \n End SubModelPart \n")

            f.close()

        print("Successfully write out GID DEM.mdpa file!")