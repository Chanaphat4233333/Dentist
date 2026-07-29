class Lingual_11:
    def __init__(self, L1, L2, threshold):
        self.L1 = L1
        self.L2 = L2
        self.threshold= threshold
    
    
        self.L1_grade, self.L1_score = self.L1calculator()
        self.L2_grade, self.L2_score = self.L2calculator()
        self.final_score = self.final_score(self.L1_score, self.L2_score)
    
    def L1calculator(self):
        threshold = self.threshold
        Amin = threshold['A'][0]
        Amax = threshold['A'][1]
        Bmin = threshold['B'][0]
        Bmax = threshold['B'][1]
        Cmin = threshold['C'][0]
        Cmax = threshold['C'][1]

        L1 = self.L1
        L1_grade = ""
        L1_score = 0

        if L1 >= Amin and L1 <= Amax:
            L1_grade = "A"
            L1_score = 30
        elif L1 > Bmin and L1 <= Bmax:
            L1_grade = "B"
            L1_score = 24
        elif L1 > Cmin and L1 <= Cmax:
            L1_grade = "C"
            L1_score = 18
        else:
            L1_grade = "F"
            L1_score = 9
        
        return L1_grade, L1_score
    
    def L2calculator(self):
        threshold = self.threshold
        Amin = threshold['A'][0]
        Amax = threshold['A'][1]
        Bmin = threshold['B'][0]
        Bmax = threshold['B'][1]
        Cmin = threshold['C'][0]
        Cmax = threshold['C'][1]

        L2 = self.L2
        L2_grade = ""
        L2_score = 0

        if L2 >= Amin and L2 <= Amax:
            L2_grade = "A"
            L2_score = 30
        elif L2 > Bmin and L2 <= Bmax:
            L2_grade = "B"
            L2_score = 24
        elif L2 > Cmin and L2 <= Cmax:
            L2_grade = "C"
            L2_score = 18
        else:
            L2_grade = "F"
            L2_score = 9
        
        return L2_grade, L2_score

    def final_score(self, L1_score, L2_score):
        final_score = L1_score + L2_score
        final_grade = "N/A"
        
        return final_score