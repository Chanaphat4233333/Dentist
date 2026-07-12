import pandas as pd
from pkg.crypto import encrypt_aes256, decrypt_aes256

class Buccal:
    def __init__(self, Bplane1, Bplane2, threshold, filename, fixatrow, filenameDB):
        self.Bplane1 = Bplane1
        self.Bplane2 = Bplane2
        self.threshold = threshold
        self.filename = filename
        self.fixatrow = fixatrow
        self.filenameDB = filenameDB

        Grade_Buccal_Bplane1, score_Buccal_Bplane1 = self.Bplane1Calculator()
        Grade_Buccal_Bplane2, score_Buccal_Bplane2 = self.Bplane2Calculator()
        final_score = self.finalScore(score_Buccal_Bplane1, score_Buccal_Bplane2)
        
        self.WriteFileCsv(Grade_Buccal_Bplane1, Grade_Buccal_Bplane2, final_score)
        self.WriteFileDB(Grade_Buccal_Bplane1, Grade_Buccal_Bplane2, final_score)

    def Bplane1Calculator(self):
        grade = "N/A"
        
        Amin = float(self.threshold['A'][0])
        Amax = float(self.threshold['A'][1])
        Bmin = float(self.threshold['B'][0])
        Bmax = float(self.threshold['B'][1])
        Cmin = float(self.threshold['C'][0])
        Cmax = float(self.threshold['C'][1])
        Values = self.Bplane1
        Grade_Bplane1 = grade
        score_Bplane1 = 0
        if Values >= Amin and Values <= Amax:
            Grade_Bplane1 = "A"
            score_Bplane1 = 10
        elif Values > Bmin and Values <= Bmax:
            Grade_Bplane1 = "B"
            score_Bplane1 = 8
        elif Values > Cmin and Values <= Cmax:
            Grade_Bplane1 = "C"
            score_Bplane1 = 6
        else:
            Grade_Bplane1 = "F"
            score_Bplane1 = 3
        return Grade_Bplane1, score_Bplane1 
    def Bplane2Calculator(self):
        grade = "N/A"

        Amin = float(self.threshold['A'][0])
        Amax = float(self.threshold['A'][1])
        Bmin = float(self.threshold['B'][0])
        Bmax = float(self.threshold['B'][1])
        Cmin = float(self.threshold['C'][0])
        Cmax = float(self.threshold['C'][1])
        Values = self.Bplane2
        Grade_Bplane2 = grade
        score_Bplane2 = 0
        if Values >= Amin and Values <= Amax:
            Grade_Bplane2 = "A"
            score_Bplane2 = 10
        elif Values > Bmin and Values <= Bmax:
            Grade_Bplane2 = "B"
            score_Bplane2 = 8
        elif Values > Cmin and Values <= Cmax:
            Grade_Bplane2 = "C"
            score_Bplane2 = 6
        else:
            Grade_Bplane2 = "F"
            score_Bplane2 = 3
        return Grade_Bplane2, score_Bplane2 
    
    def finalScore(self, score_Bplane1, score_Bplane2):
        final_score = score_Bplane1 + score_Bplane2

        return final_score

    def WriteFileCsv(self, Grade_Bplane1, Grade_Bplane2, finalscore):
        df = pd.read_csv("results/" + self.filename, encoding="utf-8-sig")
        df.at[self.fixatrow, "Buccal_score"] = finalscore
        df.at[self.fixatrow, "Buccal_B plane1_grade"] = Grade_Bplane1
        df.at[self.fixatrow, "Buccal_B plane2_grade"] = Grade_Bplane2
        df.to_csv("results/" + self.filename, encoding="utf-8-sig", index=False)
        
    def WriteFileDB(self, Grade_Bplane1, Grade_Bplane2, finalscore):
        df = pd.read_csv("results_encrypt/" + self.filenameDB, encoding="utf-8-sig")
        df.at[self.fixatrow, "Buccal_score"] = finalscore
        df.at[self.fixatrow, "Buccal_B plane1_grade"] = Grade_Bplane1
        df.at[self.fixatrow, "Buccal_B plane2_grade"] = Grade_Bplane2
        df.to_csv("results_encrypt/" + self.filenameDB, encoding="utf-8-sig", index=False)
        
        
        
        
    
