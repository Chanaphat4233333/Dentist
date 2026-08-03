class TOC_16PFMC:
    def __init__(self, md, bl, threshold):
        self.md = md
        self.bl = bl
        self.threshold = threshold
        self.md_grade, self.md_score = self.md_calculator()
        self.bl_grade, self.bl_score = self.bl_calculator()
        self.final_score = self.finalscore(self.md_score, self.bl_score)
    
    def md_calculator(self):
        threshold = self.threshold
        Amin = threshold['A'][0]
        Amax = threshold['A'][1]
        Bmin = threshold['B'][0]
        Bmax = threshold['B'][1]
        Cmin = threshold['C'][0]
        Cmax = threshold['C'][1]
        
        md_grade = ""
        md_score = 0
        
        if self.md >= Amin and self.md <= Amax:
            md_grade = "A"
            md_score = 30
        elif self.md > Bmin and self.md <= Bmax:
            md_grade = "B"
            md_score = 24
        elif self.md > Cmin and self.md <= Cmax:
            md_grade = "C"
            md_score = 18
        else:
            md_grade = "F"
            md_score = 9
        
        return md_grade, md_score

    def bl_calculator(self):
        threshold = self.threshold
        Amin = threshold['A'][0]
        Amax = threshold['A'][1]
        Bmin = threshold['B'][0]
        Bmax = threshold['B'][1]
        Cmin = threshold['C'][0]
        Cmax = threshold['C'][1]
        
        bl_grade = ""
        bl_score = 0
        
        if self.bl >= Amin and self.bl <= Amax:
            bl_grade = "A"
            bl_score = 30
        elif self.bl > Bmin and self.bl <= Bmax:
            bl_grade = "B"
            bl_score = 24
        elif self.bl > Cmin and self.bl <= Cmax:
            bl_grade = "C"
            bl_score = 15
        else:
            bl_grade = "F"
            bl_score = 9
        
        return bl_grade, bl_score
    
    def finalscore(self, md_score, bl_score):
        finalscore = md_score + bl_score
        
        return finalscore