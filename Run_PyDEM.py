# ---------------Name: PyDEM -------------------
# ----------Author: Chengshun Shang-------------
# ---------------Date: 04-01-2022---------------
# -------------License : BSD license------------

from PreProcess.getInitialParticleData import getInitialParticleData
from PostProcess.PostProcess import PostProcess

class TheMainProcess():

    def __init__(self) -> None:
        
        self.my2dData = getInitialParticleData()
        self.my2dPost = PostProcess()

        self.i_run_time = 0.0
        self.aim_run_time = 1.0
        self.time_step = 1e-5
        self.L = 5
        self.W = 10
        self.r = 0.1

    # running functions
    def run(self):

        self.my2dData.creat_disk(self.L, self.W, self.r)
        self.main_cicle()
        #self.plot_results()
        self.my2dPost.WriteOutParaview(self.my2dData)

    # cicle for force and information update
    def main_cicle(self):

        while self.i_run_time < self.aim_run_time:
            # traverse all the 
            for p_pram_dict in self.my2dData.p_pram_list:
                
                #force_cal(p_pram_dict["p_x"], p_pram_dict["p_y"], p_pram_dict["radius"], p_pram_dict["p_v_x"], p_pram_dict["p_v_y"])
                print("%s\t" % p_pram_dict)

            #self.i_run_time += self.time_step
            break

# TO DO: constitutive model
# def force_cal(p_x, p_y, radius, p_v_x, p_v_y):
    
if __name__ == "__main__":

    TestDEM = TheMainProcess()
    TestDEM.run()
