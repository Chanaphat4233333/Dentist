import pandas as pd
class FinishingLine:
    def __init__(self, Buccal, Lingual, Mesial, Distal, BTheshold, LTheshold, filename, filenameDB, fixatrow):
        self.Buccal = Buccal
        self.Lingual = Lingual
        self.Mesial = Mesial
        self.Distal = Distal
        self.BTheshold = BTheshold
        self.LTheshold = LTheshold
        self.filename = filename
        self.filenameDB = filenameDB
        self.fixatrow = fixatrow

        self.Grade_Buccal, self.score_Buccal = self.BuccalCalculator()
        self.Grade_Lingual, self.score_Lingual = self.LingualCalculator()
        self.Grade_Mesial, self.score_Mesial = self.MesialCalculator()
        self.Grade_Distal, self.score_Distal = self.DistalCalculator()
        self.final_score = self.Finalscore(self.score_Buccal, self.score_Lingual, self.score_Mesial, self.score_Distal)

    def BuccalCalculator(self):
        Amin = float(self.BTheshold['A'][0])
        Amax = float(self.BTheshold['A'][1])
        Bmin = float(self.BTheshold['B'][0])
        Bmax = float(self.BTheshold['B'][1])
        Cmin = float(self.BTheshold['C'][0])
        Cmax = float(self.BTheshold['C'][1])
        Values = self.Buccal
        Grade_Buccal = "N/A"
        score_Buccal = 0
        if Values >= Amin and Values <= Amax:
            Grade_Buccal = "A"
            score_Buccal = 15
        elif Values > Bmin and Values <= Bmax:
            Grade_Buccal = "B"
            score_Buccal = 12
        elif Values > Cmin and Values <= Cmax:
            Grade_Buccal = "C"
            score_Buccal = 9
        else:
            Grade_Buccal = "F"
            score_Buccal = 4.5
        return Grade_Buccal, score_Buccal
    
    def LingualCalculator(self):
        Amin = float(self.LTheshold['A'][0])
        Amax = float(self.LTheshold['A'][1])
        Bmin = float(self.LTheshold['B'][0])
        Bmax = float(self.LTheshold['B'][1])
        Cmin = float(self.LTheshold['C'][0])
        Cmax = float(self.LTheshold['C'][1])
        Values = self.Lingual
        Grade_Lingual = "N/A"
        score_Lingual = 0
        if Values >= Amin and Values <= Amax:
            Grade_Lingual = "A"
            score_Lingual = 15
        elif Values > Bmin and Values <= Bmax:
            Grade_Lingual = "B"
            score_Lingual = 12
        elif Values > Cmin and Values <= Cmax:
            Grade_Lingual = "C"
            score_Lingual = 9
        else:
            Grade_Lingual = "F"
            score_Lingual = 4.5
        return Grade_Lingual, score_Lingual

    def MesialCalculator(self):
        Amin = float(self.LTheshold['A'][0])
        Amax = float(self.LTheshold['A'][1])
        Bmin = float(self.LTheshold['B'][0])
        Bmax = float(self.LTheshold['B'][1])
        Cmin = float(self.LTheshold['C'][0])
        Cmax = float(self.LTheshold['C'][1])
        Values = self.Mesial
        Grade_Mesial = "N/A"
        score_Mesial = 0
        if Values >= Amin and Values <= Amax:
            Grade_Mesial = "A"
            score_Mesial = 15
        elif Values > Bmin and Values <= Bmax:
            Grade_Mesial = "B"
            score_Mesial = 12
        elif Values > Cmin and Values <= Cmax:
            Grade_Mesial = "C"
            score_Mesial = 9
        else:
            Grade_Mesial = "F"
            score_Mesial = 4.5
        return Grade_Mesial, score_Mesial
    
    def DistalCalculator(self):
        Amin = float(self.LTheshold['A'][0])
        Amax = float(self.LTheshold['A'][1])
        Bmin = float(self.LTheshold['B'][0])
        Bmax = float(self.LTheshold['B'][1])
        Cmin = float(self.LTheshold['C'][0])
        Cmax = float(self.LTheshold['C'][1])
        Values = self.Distal
        Grade_Distal = "N/A"
        score_Distal = 0
        if Values >= Amin and Values <= Amax:
            Grade_Distal = "A"
            score_Distal = 15
        elif Values > Bmin and Values <= Bmax:
            Grade_Distal = "B"
            score_Distal = 12
        elif Values > Cmin and Values <= Cmax:
            Grade_Distal = "C"
            score_Distal = 9
        else:
            Grade_Distal = "F"
            score_Distal = 4.5
        return Grade_Distal, score_Distal

    def Finalscore(self, score_Buccal, score_Lingual, score_Mesial, score_Distal):
        final_score = score_Buccal + score_Lingual + score_Mesial + score_Distal

        return final_score

    
   
        
        
    
        