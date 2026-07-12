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

        Grade_Buccal, score_Buccal = self.BuccalCalculator()
        Grade_Lingual, score_Lingual = self.LingualCalculator()
        Grade_Mesial, score_Mesial = self.MesialCalculator()
        Grade_Distal, score_Distal = self.DistalCalculator()
        final_score = self.Finalscore(score_Buccal, score_Lingual, score_Mesial, score_Distal)
        self.Writefile(Grade_Buccal, Grade_Lingual, Grade_Mesial, Grade_Distal, final_score)

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
            score_Buccal = 10
        elif Values > Bmin and Values <= Bmax:
            Grade_Buccal = "B"
            score_Buccal = 8
        elif Values > Cmin and Values <= Cmax:
            Grade_Buccal = "C"
            score_Buccal = 6
        else:
            Grade_Buccal = "F"
            score_Buccal = 3
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
            score_Lingual = 10
        elif Values > Bmin and Values <= Bmax:
            Grade_Lingual = "B"
            score_Lingual = 8
        elif Values > Cmin and Values <= Cmax:
            Grade_Lingual = "C"
            score_Lingual = 6
        else:
            Grade_Lingual = "F"
            score_Lingual = 3
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

    def Finalscore(self, score_Buccal, score_Lingual, score_Mesial, score_Distal):
        final_score = score_Buccal + score_Lingual + score_Mesial + score_Distal

        return final_score

    
    def Writefile(self, Grade_Buccal, Grade_Lingual, Grade_Mesial, Grade_Distal, final_score):
        df = pd.read_csv("results/" + self.filename, encoding="utf-8-sig")
        df.at[self.fixatrow, "FinishingLine_score"] = final_score
        df.at[self.fixatrow, "FinishingLine_Buccal_grade"] = Grade_Buccal
        df.at[self.fixatrow, "FinishingLine_Lingual_grade"] = Grade_Lingual
        df.at[self.fixatrow, "FinishingLine_Mesial_grade"] = Grade_Mesial
        df.at[self.fixatrow, "FinishingLine_Distal_grade"] = Grade_Distal
        df.to_csv("results/" + self.filename, encoding="utf-8-sig", index=False)

        df_enc = pd.read_csv("results_encrypt/" + self.filenameDB, encoding="utf-8-sig")
        df_enc.at[self.fixatrow, "FinishingLine_score"] = final_score
        df_enc.at[self.fixatrow, "FinishingLine_Buccal_grade"] = Grade_Buccal
        df_enc.at[self.fixatrow, "FinishingLine_Lingual_grade"] = Grade_Lingual
        df_enc.at[self.fixatrow, "FinishingLine_Mesial_grade"] = Grade_Mesial
        df_enc.at[self.fixatrow, "FinishingLine_Distal_grade"] = Grade_Distal
        df_enc.to_csv("results_encrypt/" + self.filenameDB, encoding="utf-8-sig", index=False)
        
        
    
        