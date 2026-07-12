import pandas as pd
class Proximal:
    
    def __init__(self, Mesial, Distal, filename, fixatrow, filenameDB, threshold):
        self.Mesial = Mesial
        self.Distal = Distal
        self.filename = filename
        self.fixatrow = fixatrow
        self.filenameDB = filenameDB
        self.threshold = threshold

        self.Grade_Mesial, self.score_Mesial = self.MesialCalculator()
        self.Grade_Distal, self.score_Distal = self.DistalCalculator()
        self.final_score = self.finalScore(self.score_Mesial, self.score_Distal)
    
    def MesialCalculator(self):
        Amin = self.threshold['A'][0]
        Amax = self.threshold['A'][1]
        Bmin = self.threshold['B'][0]
        Bmax = self.threshold['B'][1]
        Cmin = self.threshold['C'][0]
        Cmax = self.threshold['C'][1]
        Values = self.Mesial
        Grade_Mesial = "N/A"
        score_Mesial = 0
        if Values >= Amin and Values <= Amax:
            Grade_Mesial = "A"
            score_Mesial = 10
        elif Values > Bmin and Values <= Bmax:
            Grade_Mesial = "B"
            score_Mesial = 8
        elif Values > Cmin and Values <= Cmax:
            Grade_Mesial = "C"
            score_Mesial = 6
        else:
            Grade_Mesial = "F"
            score_Mesial = 3
        return Grade_Mesial, score_Mesial 
    
    def DistalCalculator(self):
        Amin = self.threshold['A'][0]
        Amax = self.threshold['A'][1]
        Bmin = self.threshold['B'][0]
        Bmax = self.threshold['B'][1]
        Cmin = self.threshold['C'][0]
        Cmax = self.threshold['C'][1]
        Values = self.Distal
        Grade_Distal = "N/A"
        score_Distal = 0
        if Values >= Amin and Values <= Amax:
            Grade_Distal = "A"
            score_Distal = 10
        elif Values > Bmin and Values <= Bmax:
            Grade_Distal = "B"
            score_Distal = 8
        elif Values > Cmin and Values <= Cmax:
            Grade_Distal = "C"
            score_Distal = 6
        else:
            Grade_Distal = "F"
            score_Distal = 3
        return Grade_Distal, score_Distal 
    
    def finalScore(self, score_Mesial, score_Distal):
        final_score = score_Mesial + score_Distal
        return final_score
    
   