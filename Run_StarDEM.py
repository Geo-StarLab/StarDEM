# ---------------Name: StarDEM -------------------
# ------------Author: Chengshun Shang-------------
# -----------------Date: 04-01-2022---------------
# ---------------License : BSD license------------

from PreProcess.getInitialParticleData import getInitialParticleData
from PostProcess.PostProcess import PostProcess

class TheMainProcess():

    def __init__(self) -> None:
        
        self.myDEMData = getInitialParticleData()
        self.myDEMPost = PostProcess()

        self.i_run_time = 0.0
        self.aim_run_time = 1.0
        self.time_step = 1e-5
        self.L = 220
        self.W = 20
        self.T = 20
        self.r = 10
        self.is_round = False   #you should be careful when you set this parameters :)

        #for creating membrane layer
        self.H = 0.05
        self.r_in = 0.0125
        self.r_m = 0.0015
        self.p_id_ini = 3000

        #for reading mdpa file
        self.aim_mdpa_file_name = 'G-TriaxialDEM.mdpa'

        #for set particle group ID
        self.sample_height = 0.108
        self.sample_width  = 0.054
        self.joint_angle   = 45
        self.joint_width_1 = 0.006  # this is the joint width
        self.joint_width_2 = 0.010  # this is the main rock width

    # running functions
    def run(self):

        #self.myDEMData.creat_disk(self.L, self.W, self.r, self.is_round)
        #self.myDEMData.creat_sphere(self.L, self.W, self.T, self.r, self.is_round)
        #self.myDEMData.creat_membrane(self.H, self.r_in, self.r_m, self.p_id_ini)
        self.myDEMData.getParticleDataFromMdpa(self.aim_mdpa_file_name)
        #self.myDEMData.setParticleGroupID(self.sample_height, self.sample_width, self.joint_angle, self.joint_width_1, self.joint_width_2, self.myDEMData.p_pram_list)
        self.myDEMData.setParticleGroupIDSingle(self.sample_height, self.joint_angle, self.joint_width_1, self.myDEMData.p_pram_list)
        self.main_cicle()
        #self.plot_results()
        self.myDEMPost.WriteOutParaview(self.myDEMData)
        self.myDEMPost.WriteOutGIDData(self.myDEMData)

    # cicle for force and information update
    def main_cicle(self):

        while self.i_run_time < self.aim_run_time:
            # traverse all the 
            for p_pram_dict in self.myDEMData.p_pram_list:
                
                #force_cal(p_pram_dict["p_x"], p_pram_dict["p_y"], p_pram_dict["radius"], p_pram_dict["p_v_x"], p_pram_dict["p_v_y"])
                print("%s\t" % p_pram_dict)

            #self.i_run_time += self.time_step
            break

# TO DO: constitutive model
# def force_cal(p_x, p_y, radius, p_v_x, p_v_y):
    
if __name__ == "__main__":

    TestDEM = TheMainProcess()
    TestDEM.run()
