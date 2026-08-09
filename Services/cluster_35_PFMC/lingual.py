import pandas as pd
class Lingual:
    def __init__(self, Lplane1, Lplane2, threshold, filename, fixatrow, filenameDB):
        self.Lplane1 = Lplane1
        self.Lplane2 = Lplane2
        self.threshold = threshold
        self.filename = filename
        self.fixatrow = fixatrow
        self.filenameDB = filenameDB  

        self.Grade_Lplane1, self.score_Lplane1 = self.Lplane1Calculator()
        self.Grade_Lplane2, self.score_Lplane2 = self.Lplane2Calculator()
        self.final_score = self.finalScore(self.score_Lplane1, self.score_Lplane2)

    def Lplane1Calculator(self):
        Amin  = self.threshold['A'][1]
        Amax = self.threshold['A'][0]
        Bmin = self.threshold['B'][1]
        Bmax = self.threshold['B'][0]
        Cmin = self.threshold['C'][1]
        Cmax = self.threshold['C'][0]
        Values = self.Lplane1
        Grade_Lplane1 = "N/A"
        score_Lplane1 = 0
        if Values >= Amin and Values <= Amax:
            Grade_Lplane1 = "A"
            score_Lplane1 = 30
        elif Values > Bmin and Values <= Bmax:
            Grade_Lplane1 = "B"
            score_Lplane1 = 24
        elif Values > Cmin and Values <= Cmax:
            Grade_Lplane1 = "C"
            score_Lplane1 = 18
        else:
            Grade_Lplane1 = "F"
            score_Lplane1 = 9
        return Grade_Lplane1, score_Lplane1 
    

    def Lplane2Calculator(self):
        Amin  = self.threshold['A'][1]
        Amax = self.threshold['A'][0]
        Bmin = self.threshold['B'][1]
        Bmax = self.threshold['B'][0]
        Cmin = self.threshold['C'][1]
        Cmax = self.threshold['C'][0]
        Values = self.Lplane2
        Grade_Lplane2 = "N/A"
        score_Lplane2 = 0
        if Values >= Amin and Values <= Amax:
            Grade_Lplane2 = "A"
            score_Lplane2 = 30
        elif Values > Bmin and Values <= Bmax:
            Grade_Lplane2 = "B"
            score_Lplane2 = 24
        elif Values > Cmin and Values <= Cmax:
            Grade_Lplane2 = "C"
            score_Lplane2 = 18
        else:
            Grade_Lplane2 = "F"
            score_Lplane2 = 9
        return Grade_Lplane2, score_Lplane2 

    def finalScore(self, score_Lplane1, score_Lplane2):
        final_score = score_Lplane1 + score_Lplane2
        return final_score

    
