class FinishingLine_11:
    def __init__(self, b,l,mesial,distal,threshold):
        self.b = b
        self.l = l
        self.mesial = mesial
        self.distal = distal
        self.threshold = threshold

        self.b_grade, self.b_score = self.b_calculator()
        self.l_grade, self.l_score = self.l_calculator()
        self.mesial_grade, self.mesial_score = self.mesial_calculator()
        self.distal_grade, self.distal_score = self.distal_calculator()
        self.final_score = self.finalscore(self.b_score, self.l_score, self.mesial_score, self.distal_score)
        
    def b_calculator(self):
        b = self.b
        threshold = self.threshold
        
        Amin = threshold['A'][0]
        Amax = threshold['A'][1]
        Bmin = threshold['B'][0]
        Bmax = threshold['B'][1]
        Cmin = threshold['C'][0]
        Cmax = threshold['C'][1]
        
        b_grade = ""
        b_score =  0
        
        if b >= Amin and b <= Amax:
            b_grade = "A"
            b_score = 15
        elif b > Bmin and b <= Bmax:
            b_grade = "B"
            b_score = 12
        elif b > Cmin and b <= Cmax:
            b_grade = "C"
            b_score = 9
        else:
            b_grade = "F"
            b_score = 4.5
        
        return b_grade, b_score
    
    def l_calculator(self):
        l = self.l
        threshold = self.threshold
        
        Amin = threshold['A'][0]
        Amax = threshold['A'][1]
        Bmin = threshold['B'][0]
        Bmax = threshold['B'][1]
        Cmin = threshold['C'][0]
        Cmax = threshold['C'][1]
        
        l_grade = ""
        l_score =  0
        
        if l >= Amin and l <= Amax:
            l_grade = "A"
            l_score = 15
        elif l > Bmin and l <= Bmax:
            l_grade = "B"
            l_score = 12
        elif l > Cmin and l <= Cmax:
            l_grade = "C"
            l_score = 9
        else:
            l_grade = "F"
            l_score = 4.5
        
        return l_grade, l_score
    
    def mesial_calculator(self):
        mesial = self.mesial
        threshold = self.threshold
        
        Amin = threshold['A'][0]
        Amax = threshold['A'][1]
        Bmin = threshold['B'][0]
        Bmax = threshold['B'][1]
        Cmin = threshold['C'][0]
        Cmax = threshold['C'][1]
        
        mesial_grade = ""
        mesial_score =  0
        
        if mesial >= Amin and mesial <= Amax:
            mesial_grade = "A"
            mesial_score = 15
        elif mesial > Bmin and mesial <= Bmax:
            mesial_grade = "B"
            mesial_score = 12
        elif mesial > Cmin and mesial <= Cmax:
            mesial_grade = "C"
            mesial_score = 9
        else:
            mesial_grade = "F"
            mesial_score = 4.5
        
        return mesial_grade, mesial_score
    
    def distal_calculator(self):
        distal = self.distal
        threshold = self.threshold
        
        Amin = threshold['A'][0]
        Amax = threshold['A'][1]
        Bmin = threshold['B'][0]
        Bmax = threshold['B'][1]
        Cmin = threshold['C'][0]
        Cmax = threshold['C'][1]
        
        distal_grade = ""
        distal_score =  0
        
        if distal >= Amin and distal <= Amax:
            distal_grade = "A"
            distal_score = 15
        elif distal > Bmin and distal <= Bmax:
            distal_grade = "B"
            distal_score = 12
        elif distal > Cmin and distal <= Cmax:
            distal_grade = "C"
            distal_score = 9
        else:
            distal_grade = "F"
            distal_score = 4.5
        return distal_grade, distal_score
    
    def finalscore(self, bscore, lscore, mesialscore, distalscore):
        final_score = bscore + lscore + mesialscore + distalscore
        return final_score