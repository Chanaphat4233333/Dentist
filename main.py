from Services.cluster_35_PFMC.occ import C35Occ

def loadConfig():
    
if __name__ == "__main__":
    
    test = C35Occ(central= 2.2, Bfunc=0, L_of_B=0, L_non=0, B_incline=0)
    # my_data_list = test.OccCalculator()
    
    # current_grade = test.OccA_function(my_data_list)
    
    # final_score = test.FinalScore(my_data_list)
    print(test.score_OCc_Central_Groove)