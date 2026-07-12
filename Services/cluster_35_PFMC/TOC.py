import pandas as pd

class TOC:
    def __init__(self, MD, UndercutMD, BL, UndercutBL, threshold, filename, filenameDB, fixatrow):
        self.MD = MD
        self.UndercutMD = UndercutMD
        self.BL = BL
        self.UndercutBL = UndercutBL
        self.threshold = threshold
        self.filename = filename
        self.filenameDB = filenameDB
        self.fixatrow = fixatrow
        
        self.score_MD, self.Grade_MD = self.MDCalculator()
        self.score_BL, self.Grade_BL = self.BLCalculator()
        self.final_score = self.Finalscore(self.score_MD, self.score_BL)

    def MDCalculator(self):
        IsUndercut = True
        MDValue = self.MD
        if self.UndercutMD == "no":
            IsUndercut = False
        Amax = float(self.threshold['A'][1])
        Amin = float(self.threshold['A'][0])
        Bmax = float(self.threshold['B'][1])
        Bmin = float(self.threshold['B'][0])
        Cmax = float(self.threshold['C'][1])
        Cmin = float(self.threshold['C'][0])
        Grade_MD = "N/A"
        score_MD = 0
        if not IsUndercut:
            if MDValue >= Amin and MDValue <=10:
                score_MD = 10
                Grade_MD = "A"
            elif MDValue >Bmin and MDValue <=Bmax:
                score_MD = 8
                Grade_MD = "B"
            elif MDValue > Cmin and MDValue <= Cmax:
                score_MD = 6
                Grade_MD = "C"
            else:
                score_MD = 3
                Grade_MD = "F"
        else:
            score_MD = 3
            Grade_MD = "F"
        
        return score_MD, Grade_MD
    
    def BLCalculator(self):
        IsUndercut = True
        BLValue = self.BL
        if self.UndercutBL == "no":
            IsUndercut = False
        Amax = float(self.threshold['A'][1])
        Amin = float(self.threshold['A'][0])
        Bmax = float(self.threshold['B'][1])
        Bmin = float(self.threshold['B'][0])
        Cmax = float(self.threshold['C'][1])
        Cmin = float(self.threshold['C'][0])
        Grade_BL = "N/A"
        score_BL = 0
        if not IsUndercut:
            if BLValue >= Amin and BLValue <=10:
                score_BL = 10
                Grade_BL = "A"
            elif BLValue >Bmin and BLValue <=Bmax:
                score_BL = 8
                Grade_BL = "B"
            elif BLValue > Cmin and BLValue <= Cmax:
                score_BL = 6
                Grade_BL = "C"
            else:
                score_BL = 3
                Grade_BL = "F"
        else:
            score_BL = 3
            Grade_BL = "F"
        
        return score_BL, Grade_BL
    
    def Finalscore(self, score_MD, score_BL):
        final_score = score_MD + score_BL
        return final_score
    
    
            
            
