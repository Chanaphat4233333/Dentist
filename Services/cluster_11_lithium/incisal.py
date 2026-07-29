class Incisal:
    def __init__(self, incisal, threshold):
        self.incisal = incisal
        self.threshold = threshold
        
        self.incisal_grade, self.incisal_score = self.incisal_calculator()
        self.final_score = self.incisal_final_score(self.incisal_grade, self.incisal_score)
    
    
    
    def incisal_calculator(self):
        
        Amin = self.threshold['A'][0]
        Amax = self.threshold['A'][1]
        Bmin = self.threshold['B'][0]
        Bmax = self.threshold['B'][1]
        Cmin = self.threshold['C'][0]
        Cmax = self.threshold['C'][1]
        
        incisal = self.incisal
        incisal_garde = ""
        incisal_score = 0

        if incisal >= Amin and incisal <= Amax:
            incisal_garde = "A"
            incisal_score = 60
        elif incisal > Bmin and incisal <= Bmax:
            incisal_garde = "B"
            incisal_score = 48
        elif incisal > Cmin and incisal <= Cmax:
            incisal_garde = "C"
            incisal_score = 36
        else:
            incisal_garde = "F"
            incisal_score  = 18
        
        return incisal_garde, incisal_score
    
    
    def incisal_final_score(self, incisal_garde, incisal_score):
        return incisal_score