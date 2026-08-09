class Finishing_line_46FMC:
    def __init__(self, mb, ml, db, dl, mesial, distal, threshold):
        self.mb = mb
        self.ml = ml
        self.db = db
        self.dl = dl
        self.mesial = mesial
        self.distal = distal
        self.threshold = threshold

        self.mb_grade, self.mb_score = self.mb_calculator()
        self.ml_grade, self.ml_score = self.ml_calculator()
        self.db_grade, self.db_score = self.db_calculator()
        self.dl_grade, self.dl_score = self.dl_calculator()
        self.mesial_grade, self.mesial_score = self.mesial_calculator()
        self.distal_grade, self.distal_score = self.distal_calculator()

        self.final_score = self.finalscore(self.mb_score, self.ml_score, self.db_score, self.dl_score, self.mesial_score, self.distal_score)
    
    def mb_calculator(self):
        threshold = self.threshold
        
        Amin = threshold['A'][0]
        Amax = threshold['A'][1]
        Bmin = threshold['B'][0]
        Bmax = threshold['B'][1]
        Cmin = threshold['C'][0]
        Cmax = threshold['C'][1]
        
        mb_grade = ""
        mb_score = 0
        
        if self.mb >= Amin and self.mb <= Amax:
            mb_grade = "A"
            mb_score = 10
        elif self.mb > Bmin and self.mb <= Bmax:
            mb_grade = "B"
            mb_score = 8
        elif self.mb > Cmin and self.mb <= Cmax:
            mb_grade = "C"
            mb_score = 6
        else:
            mb_grade = "F"
            mb_score = 3
        
        return mb_grade, mb_score

    def ml_calculator(self):
        threshold = self.threshold
        
        Amin = threshold['A'][0]
        Amax = threshold['A'][1]
        Bmin = threshold['B'][0]
        Bmax = threshold['B'][1]
        Cmin = threshold['C'][0]
        Cmax = threshold['C'][1]
        
        ml_grade = ""
        ml_score = 0
        
        if self.ml >= Amin and self.ml <= Amax:
            ml_grade = "A"
            ml_score = 10
        elif self.ml > Bmin and self.ml <= Bmax:
            ml_grade = "B"
            ml_score = 8
        elif self.ml > Cmin and self.ml <= Cmax:
            ml_grade = "C"
            ml_score = 6
        else:
            ml_grade = "F"
            ml_score = 3
        
        return ml_grade, ml_score

    def db_calculator(self):
        threshold = self.threshold
        
        Amin = threshold['A'][0]
        Amax = threshold['A'][1]
        Bmin = threshold['B'][0]
        Bmax = threshold['B'][1]
        Cmin = threshold['C'][0]
        Cmax = threshold['C'][1]
        
        db_grade = ""
        db_score = 0
        
        if self.db >= Amin and self.db <= Amax:
            db_grade = "A"
            db_score = 10
        elif self.db > Bmin and self.db <= Bmax:
            db_grade = "B"
            db_score = 8
        elif self.db > Cmin and self.db <= Cmax:
            db_grade = "C"
            db_score = 6
        else:
            db_grade = "F"
            db_score = 3
        
        return db_grade, db_score

    def dl_calculator(self):
        threshold = self.threshold
        
        Amin = threshold['A'][0]
        Amax = threshold['A'][1]
        Bmin = threshold['B'][0]
        Bmax = threshold['B'][1]
        Cmin = threshold['C'][0]
        Cmax = threshold['C'][1]
        
        dl_grade = ""
        dl_score = 0
        
        if self.dl >= Amin and self.dl <= Amax:
            dl_grade = "A"
            dl_score = 10
        elif self.dl > Bmin and self.dl <= Bmax:
            dl_grade = "B"
            dl_score = 8
        elif self.dl > Cmin and self.dl <= Cmax:
            dl_grade = "C"
            dl_score = 6
        else:
            dl_grade = "F"
            dl_score = 3
        
        return dl_grade, dl_score
    
    def mesial_calculator(self):
        threshold = self.threshold
        
        Amin = threshold['A'][0]
        Amax = threshold['A'][1]
        Bmin = threshold['B'][0]
        Bmax = threshold['B'][1]
        Cmin = threshold['C'][0]
        Cmax = threshold['C'][1]
        
        mesial_grade = ""
        mesial_score = 0
        
        if self.mesial >= Amin and self.mesial <= Amax:
            mesial_grade = "A"
            mesial_score = 10   
        elif self.mesial > Bmin and self.mesial <= Bmax:
            mesial_grade = "B"
            mesial_score = 8
        elif self.mesial > Cmin and self.mesial <= Cmax:
            mesial_grade = "C"
            mesial_score = 6
        else:
            mesial_grade = "F"
            mesial_score = 3
        
        return mesial_grade, mesial_score
    
    def distal_calculator(self):
        threshold = self.threshold
        
        Amin = threshold['A'][0]
        Amax = threshold['A'][1]
        Bmin = threshold['B'][0]
        Bmax = threshold['B'][1]
        Cmin = threshold['C'][0]
        Cmax = threshold['C'][1]
        
        distal_grade = ""
        distal_score = 0
        
        if self.distal >= Amin and self.distal <= Amax:
            distal_grade = "A"
            distal_score = 10
        elif self.distal > Bmin and self.distal <= Bmax:
            distal_grade = "B"
            distal_score = 8
        elif self.distal > Cmin and self.distal <= Cmax:
            distal_grade = "C"
            distal_score = 6
        else:
            distal_grade = "F"
            distal_score = 3
        
        return distal_grade, distal_score
    
    def finalscore(self, mb_score, ml_score, db_score, dl_score, mesial_score, distal_score):
        finalscore = mb_score + ml_score + db_score + dl_score + mesial_score + distal_score
        
        return finalscore