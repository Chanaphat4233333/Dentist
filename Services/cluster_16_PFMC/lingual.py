class Lingual_16PFMC:
    def __init__(self, mlp1, mlp2, dlp1, dlp2, threshold):
        self.mlp1 = mlp1
        self.mlp2 = mlp2
        self.dlp1 = dlp1
        self.dlp2 = dlp2
        self.threshold = threshold
        if self.mlp1 == 0:
            self.mlp1_grade, self.mlp1_score = self.mlp1_calculator()
            self.mlp2_grade = self.mlp1_grade
            self.mlp2_score = 0
        elif self.mlp2 == 0:
            self.mlp2_grade, self.mlp2_score = self.mlp2_calculator()
            self.mlp1_grade = self.mlp2_grade
            self.mlp1_score = 0
        else:
            self.mlp1_grade, self.mlp1_score = self.mlp1_calculator()
            self.mlp2_grade, self.mlp2_score = self.mlp2_calculator()
        
        if self.dlp1 == 0:
            self.dlp1_grade, self.dlp1_score = self.dlp1_calculator()
            self.dlp2_grade = self.dlp1_grade
            self.dlp2_score = 0
        elif self.dlp2 == 0:
            self.dlp2_grade, self.dlp2_score = self.dlp2_calculator()
            self.dlp1_grade = self.dlp2_grade
            self.dlp1_score = 0
        else:
            self.dlp1_grade, self.dlp1_score = self.dlp1_calculator()
            self.dlp2_grade, self.dlp2_score = self.dlp2_calculator()
        self.final_score = self.finalscore(self.mlp1_score, self.mlp2_score, self.dlp1_score, self.dlp2_score)

    def mlp1_calculator(self):
        threshold = self.threshold
        mutiscore = 1
        if self.mlp1 == 0:
            self.mlp1 = self.mlp2
            mutiscore = 2
        
        
        Amin = threshold['A'][0]
        Amax = threshold['A'][1]
        Bmin = threshold['B'][0]
        Bmax = threshold['B'][1]
        Cmin = threshold['C'][0]
        Cmax = threshold['C'][1]
        
        mlp1_grade = ""
        mlp1_score = 0
        
        if self.mlp1 >= Amin and self.mlp1 <= Amax:
            mlp1_grade = "A"
            mlp1_score = 15
        elif self.mlp1 > Bmin and self.mlp1 <= Bmax:
            mlp1_grade = "B"
            mlp1_score = 12
        elif self.mlp1 > Cmin and self.mlp1 <= Cmax:
            mlp1_grade = "C"
            mlp1_score = 9
        else:
            mlp1_grade = "F"
            mlp1_score = 4.5
        
        return mlp1_grade, mlp1_score * mutiscore

    def mlp2_calculator(self):
        threshold = self.threshold
        mutiscore = 1
        if self.mlp2 == 0:
            self.mlp2 = self.mlp1
            mutiscore = 2
       
        Amin = threshold['A'][0]
        Amax = threshold['A'][1]
        Bmin = threshold['B'][0]
        Bmax = threshold['B'][1]
        Cmin = threshold['C'][0]
        Cmax = threshold['C'][1]
        
        mlp2_grade = ""
        mlp2_score = 0
        
        if self.mlp2 >= Amin and self.mlp2 <= Amax:
            mlp2_grade = "A"
            mlp2_score = 15
        elif self.mlp2 > Bmin and self.mlp2 <= Bmax:
            mlp2_grade = "B"
            mlp2_score = 12
        elif self.mlp2 > Cmin and self.mlp2 <= Cmax:
            mlp2_grade = "C"
            mlp2_score = 9
        else:
            mlp2_grade = "F"
            mlp2_score = 4.5
        
        return mlp2_grade, mlp2_score * mutiscore

    def dlp1_calculator(self):
        threshold = self.threshold
        mutiscore = 1
        if self.dlp1 == 0:
            self.dlp1 = self.dlp2
            mutiscore = 2
        
        Amin = threshold['A'][0]
        Amax = threshold['A'][1]
        Bmin = threshold['B'][0]
        Bmax = threshold['B'][1]
        Cmin = threshold['C'][0]
        Cmax = threshold['C'][1]
        
        dlp1_grade = ""
        dlp1_score = 0
        
        if self.dlp1 >= Amin and self.dlp1 <= Amax:
            dlp1_grade = "A"
            dlp1_score = 15
        elif self.dlp1 > Bmin and self.dlp1 <= Bmax:
            dlp1_grade = "B"
            dlp1_score = 12
        elif self.dlp1 > Cmin and self.dlp1 <= Cmax:
            dlp1_grade = "C"
            dlp1_score = 9
        else:
            dlp1_grade = "F"
            dlp1_score = 4.5
        
        return dlp1_grade, dlp1_score * mutiscore

    def dlp2_calculator(self):
        threshold = self.threshold
        mutiscore = 1
        if self.dlp2 == 0:
            self.dlp2 = self.dlp1
            mutiscore = 2
        
        
        Amin = threshold['A'][0]
        Amax = threshold['A'][1]
        Bmin = threshold['B'][0]
        Bmax = threshold['B'][1]
        Cmin = threshold['C'][0]
        Cmax = threshold['C'][1]
        
        dlp2_grade = ""
        dlp2_score = 0
        
        if self.dlp2 >= Amin and self.dlp2 <= Amax:
            dlp2_grade = "A"
            dlp2_score = 15
        elif self.dlp2 > Bmin and self.dlp2 <= Bmax:
            dlp2_grade = "B"
            dlp2_score = 12
        elif self.dlp2 > Cmin and self.dlp2 <= Cmax:
            dlp2_grade = "C"
            dlp2_score = 9
        else:
            dlp2_grade = "F"
            dlp2_score = 4.5
        
        return dlp2_grade, dlp2_score * mutiscore

    def finalscore(self, mlp1_score, mlp2_score, dlp1_score, dlp2_score):
        finalscore = mlp1_score + mlp2_score + dlp1_score + dlp2_score
        
        return finalscore
    