import pandas as pd
from pkg.crypto import encrypt_aes256, decrypt_aes256
class Occ:
    def __init__(self, id, name, central, Bfunc, L_of_B, L_non, B_incline, theshold, filename, fixatrow, secretkey, filenameDB):
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
        self.secretkey = secretkey
        self.filenameDB = filenameDB

        list_OCc = self.OccCalculator()
        self.Grade_Occ_B, self.score_Occ_B = self.OccB_function(list_OCc)
        self.Grade_Cental_groove, self.score_Cental_groove = self.OccCental_function(list_OCc)
        self.Grade_L_of_B, self.score_L_of_B = self.OccLofB_function(list_OCc)
        self.Grade_Lnon, self.score_Lnon = self.OccLnon_function(list_OCc)
        self.Grade_BofL, self.score_BofL = self.OccBofL_function(list_OCc)
        self.final_score = self.FinalScore(self.score_Occ_B, self.score_Cental_groove, self.score_L_of_B, self.score_Lnon, self.score_BofL)
        # final_score, overallgrade = self.FinalScore(score_Occ_B, score_Cental_groove, score_L_of_B, score_Lnon, score_BofL)
        
    def OccCalculator(self):
        OccB = self.Bfunc 
        OccLInclineOfB = self.L_of_B 
        OccL_non = self.L_non 
        OccCental = self.central 
        OccBIncline = self.B_incline 
        Amin = float(self.theshold['A'][0])
        Amax = float(self.theshold['A'][1])
        Bmin = float(self.theshold['B'][0])
        Bmax = float(self.theshold['B'][1])
        Cmin = float(self.theshold['C'][0])
        Cmax = float(self.theshold['C'][1])
        FileName = self.filename
        Grade = "N/A" 

        list_OCc = [float(OccB), float(OccLInclineOfB), float(OccL_non), float(OccCental), float(OccBIncline), Amin, Amax, Bmin, Bmax, Cmin, Cmax, FileName, Grade]
        return list_OCc

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
        Amin = float(1.0)
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
        Amin = float(1.0)
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
        overall_grade = "N/A"

        ## imprement overall_garde
        # if final_score >= 45 and final_score <= 50:
        #     overall_grade = "A"
        # elif final_score >= 40 and final_score <= 44:
        #     overall_grade = "B"
        # elif final_score >= 35 and final_score <= 39:
        #     overall_grade = "C"
        # else:
        #     overall_grade = "F"



        # return final_score, overall_grade
        return final_score

    