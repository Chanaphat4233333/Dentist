class Occ:
    def __init__(self, central, Bfunc, L_of_B, L_non, B_incline):
        self.central = central
        self.Bfunc = Bfunc
        self.L_of_B = L_of_B
        self.L_non = L_non
        self.B_incline = B_incline  

    def OccCalculator(self):
        OccB = self.Bfunc #คอลัมE
        OccLInclineOfB = self.L_of_B #คอลัม F
        OccL_non = self.L_non #คอลัมg
        OccCental = self.central #คอลัมh
        OccBIncline = self.B_incline #คอลัมI
        Grade = "N/A" #คอลัมJ

        list_OCc = [OccB, OccLInclineOfB,OccL_non,OccCental,OccBIncline,OccCental,Grade]
        return list_OCc


    def OccA_function(list_OCc):
        Values = []
        Values = list_OCc
        if Values[3] >= 1.5 and Values[3] <= 2:
            Values[6] = "A"
        elif Values[3] > 2 and Values[3] <= 2.3:
            Values[6] = "B"
        elif Values[3] > 2.3 and Values[3] <= 2.6:
            Values[6] = "C"
        else :
            Values[6] = "F"
        return Values[6]

    def FinalScore(Values):
        score_OCc_Central_Groove = 0
        if Values[6] == "A":
            score_OCc_Central_Groove = 10
        elif Values[6] == "B":
            score_OCc_Central_Groove = 8
        elif Values[6] == "C":
            score_OCc_Central_Groove = 6
        elif Values[6] == "F":
            score_OCc_Central_Groove = 3
        print("final_score_OCC_Central_Groove-->",score_OCc_Central_Groove)
        print("Grade-->",Values[6])

        return score_OCc_Central_Groove





    