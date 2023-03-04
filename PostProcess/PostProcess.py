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
            f.write("Begin ModelPartData \n //  VARIABLE_NAME value \n End ModelPartData \n \n Begin Properties 0 \n End Properties \n \n")
            f.write("Begin Nodes\n")
            for p_pram_dict in self.myDEMData.p_pram_list:
                f.write(str(p_pram_dict["id"]) + ' ' + str(p_pram_dict["p_x"]) + ' ' + str(p_pram_dict["p_y"]) + ' ' + str(p_pram_dict["p_z"]) + '\n')
            f.write("End Nodes \n \n")

            f.write("Begin Elements SphericContinuumParticle3D// GUI group identifier: Body \n")
            for p_pram_dict in self.myDEMData.p_pram_list:
                f.write(str(p_pram_dict["p_ele_id"]) + ' ' + ' 0 ' + str(p_pram_dict["id"]) + '\n')
            f.write("End Elements \n \n")

            f.write("Begin NodalData RADIUS // GUI group identifier: Body \n")
            for p_pram_dict in self.myDEMData.p_pram_list:
                f.write(str(p_pram_dict["id"]) + ' ' + ' 0 ' + str(p_pram_dict["radius"]) + '\n')
            f.write("End NodalData \n \n")

            f.write("Begin NodalData COHESIVE_GROUP // GUI group identifier: Body \n")
            for p_pram_dict in self.myDEMData.p_pram_list:
                f.write(str(p_pram_dict["id"]) + ' ' + ' 0 ' + " 1 " + '\n')
            f.write("End NodalData \n \n")

            f.write("Begin NodalData SKIN_SPHERE \n End NodalData \n \n")

            f.write("Begin SubModelPart DEMParts_Body // Group Body // Subtree DEMParts \n Begin SubModelPartNodes \n")
            for p_pram_dict in self.myDEMData.p_pram_list:
                if p_pram_dict["p_group_id"] == 0:
                    f.write(str(p_pram_dict["id"]) + '\n')
            f.write("End SubModelPartNodes \n Begin SubModelPartElements \n ")
            self.myDEMData.p_pram_list = sorted(self.myDEMData.p_pram_list, key=lambda d: d['p_ele_id'])
            for p_pram_dict in self.myDEMData.p_pram_list:
                if p_pram_dict["p_group_id"] == 0:
                    f.write(str(p_pram_dict["p_ele_id"]) + '\n')
            f.write("End SubModelPartElements \n")
            f.write("Begin SubModelPartConditions \n End SubModelPartConditions \n End SubModelPart \n \n")

            #write out joint group
            for p_pram_dict in self.myDEMData.p_pram_list:
                if p_pram_dict["p_group_id"] == 1:
                    joint_exist = True

            if joint_exist:
                f.write("Begin SubModelPart DEMParts_Joint // Group Joint // Subtree DEMParts \n Begin SubModelPartNodes \n")
                self.myDEMData.p_pram_list = sorted(self.myDEMData.p_pram_list, key=lambda d: d['id'])
                for p_pram_dict in self.myDEMData.p_pram_list:
                    if p_pram_dict["p_group_id"] == 1:
                        f.write(str(p_pram_dict["id"]) + '\n')
                f.write("End SubModelPartNodes \n Begin SubModelPartElements \n ")
                self.myDEMData.p_pram_list = sorted(self.myDEMData.p_pram_list, key=lambda d: d['p_ele_id'])
                for p_pram_dict in self.myDEMData.p_pram_list:
                    if p_pram_dict["p_group_id"] == 1:
                        f.write(str(p_pram_dict["p_ele_id"]) + '\n')
                f.write("End SubModelPartElements \n")
                f.write("Begin SubModelPartConditions \n End SubModelPartConditions \n End SubModelPart \n")

            f.close()

        print("Successfully write out GID DEM.mdpa file!")