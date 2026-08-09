class Buccal_46FMC:
    def __init__(self, mbp1, mbp2, dbp1, dbp2, threshold):
        self.mbp1 = mbp1
        self.mbp2 = mbp2
        self.dbp1 = dbp1
        self.dbp2 = dbp2
        self.threshold = threshold
        
        self.mbp1_grade, self.mbp1_score = self.mbp1_calculator()
        self.mbp2_grade, self.mbp2_score = self.mbp2_calculator()
            
        
        self.dbp1_grade, self.dbp1_score = self.dbp1_calculator()
        self.dbp2_grade, self.dbp2_score = self.dbp2_calculator()
            
        self.final_score = self.finalscore(self.mbp1_score, self.mbp2_score, self.dbp1_score, self.dbp2_score)
    
    def mbp1_calculator(self):
        threshold = self.threshold
        mutiscore = 1
        
        
        Amin = threshold['A'][0]
        Amax = threshold['A'][1]
        Bmin = threshold['B'][0]
        Bmax = threshold['B'][1]
        Cmin = threshold['C'][0]
        Cmax = threshold['C'][1]
        
        mbp1_grade = ""
        mbp1_score = 0
        
        if self.mbp1 >= Amin and self.mbp1 <= Amax:
            mbp1_grade = "A"
            mbp1_score = 15
        elif self.mbp1 > Bmin and self.mbp1 <= Bmax:
            mbp1_grade = "B"
            mbp1_score = 12
        elif self.mbp1 > Cmin and self.mbp1 <= Cmax:
            mbp1_grade = "C"
            mbp1_score = 9
        else:
            mbp1_grade = "F"
            mbp1_score = 4.5
        
        mbp1_finalscore = mutiscore * mbp1_score
        
        return mbp1_grade, mbp1_finalscore
    
    def mbp2_calculator(self):
        threshold = self.threshold
        mutiscore = 1
        
            
        Amin = threshold['A'][0]
        Amax = threshold['A'][1]
        Bmin = threshold['B'][0]
        Bmax = threshold['B'][1]
        Cmin = threshold['C'][0]
        Cmax = threshold['C'][1]
        
        mbp2_grade = ""
        mbp2_score = 0
        
        if self.mbp2 >= Amin and self.mbp2 <= Amax:
            mbp2_grade = "A"
            mbp2_score = 15
        elif self.mbp2 > Bmin and self.mbp2 <= Bmax:
            mbp2_grade = "B"
            mbp2_score = 12
        elif self.mbp2 > Cmin and self.mbp2 <= Cmax:
            mbp2_grade = "C"
            mbp2_score = 9
        else:
            mbp2_grade = "F"
            mbp2_score = 4.5
            
        mbp2_finalscore = mutiscore * mbp2_score
        
        return mbp2_grade, mbp2_finalscore
    
    def dbp1_calculator(self):
        threshold = self.threshold
        mutiscore = 1
        
        
        Amin = threshold['A'][0]
        Amax = threshold['A'][1]
        Bmin = threshold['B'][0]
        Bmax = threshold['B'][1]
        Cmin = threshold['C'][0]
        Cmax = threshold['C'][1]
        
        dbp1_grade = ""
        dbp1_score = 0
        
        if self.dbp1 >= Amin and self.dbp1 <= Amax:
            dbp1_grade = "A"
            dbp1_score = 15
        elif self.dbp1 > Bmin and self.dbp1 <= Bmax:
            dbp1_grade = "B"
            dbp1_score = 12
        elif self.dbp1 > Cmin and self.dbp1 <= Cmax:
            dbp1_grade = "C"
            dbp1_score = 9
        else:
            dbp1_grade = "F"
            dbp1_score = 4.5
        
        return dbp1_grade, dbp1_score * mutiscore
    
    def dbp2_calculator(self):
        threshold = self.threshold
        mutiscore = 1
        
        Amin = threshold['A'][0]
        Amax = threshold['A'][1]
        Bmin = threshold['B'][0]
        Bmax = threshold['B'][1]
        Cmin = threshold['C'][0]
        Cmax = threshold['C'][1]
        
        dbp2_grade = ""
        dbp2_score = 0
        
        if self.dbp2 >= Amin and self.dbp2 <= Amax:
            dbp2_grade = "A"
            dbp2_score = 15
        elif self.dbp2 > Bmin and self.dbp2 <= Bmax:
            dbp2_grade = "B"
            dbp2_score = 12
        elif self.dbp2 > Cmin and self.dbp2 <= Cmax:
            dbp2_grade = "C"
            dbp2_score = 9
        else:
            dbp2_grade = "F"
            dbp2_score = 4.5
        
        return dbp2_grade, dbp2_score * mutiscore
    
    def finalscore(self, mbp1_score, mbp2_score, dbp1_score, dbp2_score):
        finalscore = mbp1_score + mbp2_score + dbp1_score + dbp2_score
        return finalscore    