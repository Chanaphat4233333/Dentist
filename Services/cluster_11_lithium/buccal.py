class Buccal_11:
    def __init__(self, md1, md2, threshold):
        self.md1 = md1
        self.md2 = md2
        self.threshold = threshold
        
        self.Grade_md1, self.score_md1 = self.md1calculator()
        self.Grade_md2, self.score_md2 = self.md2calculator()
        self.final_score = self.finalscore(self.score_md1, self.score_md2)
        
    def md1calculator(self):
        Amin = float(self.threshold['A'][0])
        Amax = float(self.threshold['A'][1])
        Bmin = float(self.threshold['B'][0])
        Bmax = float(self.threshold['B'][1])
        Cmin = float(self.threshold['C'][0])
        Cmax = float(self.threshold['C'][1])
        
        Grade_md1 = "N/A"
        score_md1 = 0

        if self.md1 >= Amin and self.md1 <= Amax:
            Grade_md1 = "A"
            score_md1 = 30
        elif self.md1 > Bmin and self.md1 <= Bmax:
            Grade_md1 = "B"
            score_md1 = 24
        elif self.md1 > Cmin and self.md1 <= Cmax:
            Grade_md1 = "C"
            score_md1 = 18
        else:
            Grade_md1 = "F"
            score_md1 = 9
        
        return Grade_md1, score_md1
    
    def md2calculator(self):
        Amin = float(self.threshold['A'][0])
        Amax = float(self.threshold['A'][1])
        Bmin = float(self.threshold['B'][0])
        Bmax = float(self.threshold['B'][1])
        Cmin = float(self.threshold['C'][0])
        Cmax = float(self.threshold['C'][1])
        
        Grade_md2 = "N/A"
        score_md2 = 0

        if self.md2 >= Amin and self.md2 <= Amax:
            Grade_md2 = "A"
            score_md2 = 30
        elif self.md2 > Bmin and self.md2 <= Bmax:
            Grade_md2 = "B"
            score_md2 = 24
        elif self.md2 > Cmin and self.md2 <= Cmax:
            Grade_md2 = "C"
            score_md2 = 18
        else:
            Grade_md2 = "F"
            score_md2 = 9
        
        return Grade_md2, score_md2
    
    def finalscore(self, score_md1, score_md2):
        
        finalscore = score_md1 + score_md2
        
        return finalscore