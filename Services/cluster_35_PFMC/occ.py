import pandas as pd

class Occ:
    def __init__(self, id, name, central, Bfunc, L_of_B, L_non, B_incline, theshold, filename, fixatrow):
        self.id = id
        self.name = name
        self.central = central
        self.Bfunc = Bfunc
        self.L_of_B = L_of_B
        self.L_non = L_non
        self.B_incline = B_incline 
        self.theshold = theshold
        self.filename = filename
        self.fixatrow = fixatrow

        list_OCc = self.OccCalculator()
        Grade_Occ_B, score_Occ_B = self.OccB_function(list_OCc)
        Grade_Cental_groove, score_Cental_groove = self.OccCental_function(list_OCc)
        Grade_L_of_B, score_L_of_B = self.OccLofB_function(list_OCc)
        Grade_Lnon, score_Lnon = self.OccLnon_function(list_OCc)
        Grade_BofL, score_BofL = self.OccBofL_function(list_OCc)
        final_score = self.FinalScore(score_Occ_B, score_Cental_groove, score_L_of_B, score_Lnon, score_BofL)
        
        self.WriteFileCsv(Grade_Occ_B, Grade_Cental_groove, Grade_L_of_B, Grade_Lnon, Grade_BofL, final_score)

    def OccCalculator(self):
        OccB = self.Bfunc 
        OccLInclineOfB = self.L_of_B 
        OccL_non = self.L_non 
        OccCental = self.central 
        OccBIncline = self.B_incline 
        Amin = self.theshold['A'][0]
        Amax = self.theshold['A'][1]
        Bmin = self.theshold['B'][0]
        Bmax = self.theshold['B'][1]
        Cmin = self.theshold['C'][0]
        Cmax = self.theshold['C'][1]
        FileName = self.filename
        Grade = "N/A" 

        list_OCc = [OccB, OccLInclineOfB, OccL_non, OccCental, OccBIncline, Amin, Amax, Bmin, Bmax, Cmin, Cmax, FileName, Grade]
        return list_OCc

    # เพิ่ม self เข้าไปเป็น parameter แรกของทุกฟังก์ชัน
    def OccB_function(self, list_OCc):
        Amin, Amax = list_OCc[5], list_OCc[6]
        Bmin, Bmax = list_OCc[7], list_OCc[8]
        Cmin, Cmax = list_OCc[9], list_OCc[10]
        Values = list_OCc[0]
        Grade_Occ_B = list_OCc[12]
        score_Occ_B = 0
        if Values >= Amin and Values <= Amax:
            Grade_Occ_B = "A"
            score_Occ_B = 10
        elif Values > Bmin and Values <= Bmax:
            Grade_Occ_B = "B"
            score_Occ_B = 8
        elif Values > Cmin and Values <= Cmax:
            Grade_Occ_B = "C"
            score_Occ_B = 6
        else:
            Grade_Occ_B = "F"
            score_Occ_B = 3
        return Grade_Occ_B, score_Occ_B

    def OccCental_function(self, list_OCc):
        Amin, Amax = list_OCc[5], list_OCc[6]
        Bmin, Bmax = list_OCc[7], list_OCc[8]
        Cmin, Cmax = list_OCc[9], list_OCc[10]
        Values = list_OCc[3]
        Grade_Cental_groove = list_OCc[12]
        score_Cental_groove = 0
        if Values >= Amin and Values <= Amax:
            Grade_Cental_groove = "A"
            score_Cental_groove = 10
        elif Values > Bmin and Values <= Bmax:
            Grade_Cental_groove = "B"
            score_Cental_groove = 8
        elif Values > Cmin and Values <= Cmax:
            Grade_Cental_groove = "C"
            score_Cental_groove = 6
        else:
            Grade_Cental_groove = "F"
            score_Cental_groove = 3
        return Grade_Cental_groove, score_Cental_groove
    
    def OccLofB_function(self, list_OCc):
        Amin, Amax = list_OCc[5], list_OCc[6]
        Bmin, Bmax = list_OCc[7], list_OCc[8]
        Cmin, Cmax = list_OCc[9], list_OCc[10]
        Values = list_OCc[1]
        Grade_L_of_B = list_OCc[12]
        score_L_of_B = 0
        if Values >= Amin and Values <= Amax:
            Grade_L_of_B = "A"
            score_L_of_B = 10
        elif Values > Bmin and Values <= Bmax:
            Grade_L_of_B = "B"
            score_L_of_B = 8
        elif Values > Cmin and Values <= Cmax:
            Grade_L_of_B = "C"
            score_L_of_B = 6
        else:
            Grade_L_of_B = "F"
            score_L_of_B = 3
        return Grade_L_of_B, score_L_of_B
    
    def OccLnon_function(self, list_OCc):
        Amin = 1
        Amax = list_OCc[6]
        Bmin, Bmax = list_OCc[7], list_OCc[8]
        Cmin, Cmax = list_OCc[9], list_OCc[10]
        Values = list_OCc[2]
        Grade_Lnon = list_OCc[12]
        score_Lnon = 0
        if Values >= Amin and Values <= Amax:
            Grade_Lnon = "A"
            score_Lnon = 10
        elif Values > Bmin and Values <= Bmax:
            Grade_Lnon = "B"
            score_Lnon = 8
        elif Values > Cmin and Values <= Cmax:
            Grade_Lnon = "C"
            score_Lnon = 6
        else:
            Grade_Lnon = "F"
            score_Lnon = 3
        return Grade_Lnon, score_Lnon

    def OccBofL_function(self, list_OCc):
        Amin = 1
        Amax = list_OCc[6]
        Bmin, Bmax = list_OCc[7], list_OCc[8]
        Cmin, Cmax = list_OCc[9], list_OCc[10]
        Values = list_OCc[4]
        Grade_BofL = list_OCc[12]
        score_BofL = 0
        if Values >= Amin and Values <= Amax:
            Grade_BofL = "A"
            score_BofL = 10
        elif Values > Bmin and Values <= Bmax:
            Grade_BofL = "B"
            score_BofL = 8
        elif Values > Cmin and Values <= Cmax:
            Grade_BofL = "C"
            score_BofL = 6
        else:
            Grade_BofL = "F"
            score_BofL = 3
        return Grade_BofL, score_BofL

    def FinalScore(self, score_Occ_B, score_Cental_groove, score_L_of_B, score_Lnon, score_BofL):
        final_score = score_Occ_B + score_Cental_groove + score_L_of_B + score_Lnon + score_BofL
        return final_score

    def WriteFileCsv(self, Grade_Occ_B, Grade_Cental_groove, Grade_L_of_B, Grade_Lnon, Grade_BofL, final_score):
        df = pd.read_csv(self.filename, encoding="utf-8-sig")
        
        df.at[self.fixatrow, "ID"] = self.id
        df.at[self.fixatrow, "Name"] = self.name
        df.at[self.fixatrow, "OCC_score"] = final_score
        
        df.at[self.fixatrow, "OCC_central-groove_grade"] = Grade_Cental_groove
        df.at[self.fixatrow, "OCC_B-func_grade"] = Grade_Occ_B
        df.at[self.fixatrow, "OCC_L-incline of B cusp_grade"] = Grade_L_of_B
        df.at[self.fixatrow, "OCC_L nonfunc_grade"] = Grade_Lnon
        df.at[self.fixatrow, "OCC_B incline of L cusp_grade"] = Grade_BofL
        
        df.to_csv(self.filename, index=False, encoding="utf-8-sig")