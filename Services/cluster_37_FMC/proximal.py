class Proximal_37FMC:
    def __init__(self, mesial, distal, threshold):
        self.mesial = mesial
        self.distal = distal
        self.threshold = threshold

        self.mesial_grade, self.mesial_score = self.mesial_calculator()
        self.distal_grade, self.distal_score = self.distal_calculator()
        self.final_score = self.finalscore(self.mesial_score, self.distal_score)
    
    def mesial_calculator(self):
        threshold = self.threshold
        
        Amin = threshold['A'][0]
        Amax = threshold['A'][1]
        Bmin = threshold['B'][0]
        Bmax = threshold['B'][1]
        Cmin = threshold['C'][0]
        Cmax = threshold['C'][1]
        
        mesial_grade = ""
        mesial_score = 0
        
        if self.mesial >= Amin and self.mesial <= Amax:
            mesial_grade = "A"
            mesial_score = 30
        elif self.mesial > Bmin and self.mesial <= Bmax:
            mesial_grade = "B"
            mesial_score = 24
        elif self.mesial > Cmin and self.mesial <= Cmax:
            mesial_grade = "C"
            mesial_score = 18
        else:
            mesial_grade = "F"
            mesial_score = 9
        
        return mesial_grade, mesial_score

    def distal_calculator(self):
        threshold = self.threshold
        
        Amin = threshold['A'][0]
        Amax = threshold['A'][1]
        Bmin = threshold['B'][0]
        Bmax = threshold['B'][1]
        Cmin = threshold['C'][0]
        Cmax = threshold['C'][1]
        
        distal_grade = ""
        distal_score = 0
        
        if self.distal >= Amin and self.distal <= Amax:
            distal_grade = "A"
            distal_score = 30
        elif self.distal > Bmin and self.distal <= Bmax:
            distal_grade = "B"
            distal_score = 24
        elif self.distal > Cmin and self.distal <= Cmax:
            distal_grade = "C"
            distal_score = 18
        else:
            distal_grade = "F"
            distal_score = 9
        
        return distal_grade, distal_score
    
    def finalscore(self, mesial_score, distal_score):
        finalscore = mesial_score + distal_score
        
        return finalscore