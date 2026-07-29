class Toc_11:
    def __init__(self, bl, md, threshold):
        self.bl = bl
        self.md = md
        self.threshold = threshold
        
        self.bl_garde, self.bl_score = self.bl_calculator()
        self.md_garde, self.md_score = self.md_calculator()
        self.final_score = self.finalscore(self.bl_score, self.md_score)
    
    def bl_calculator(self):
        bl = self.bl
        threshold = self.threshold
        
        Amin = threshold['A'][0]
        Amax = threshold['A'][1]
        Bmin = threshold['B'][0]
        Bmax = threshold['B'][1]
        Cmin = threshold['C'][0]
        Cmax = threshold['C'][1]
        
        bl_garde = ""
        bl_score = 0
        
        if bl >= Amin and bl <= Amax:
            bl_garde = "A"
            bl_score = 30
        elif bl > Bmin and bl <= Bmax:
            bl_garde = "B"
            bl_score = 24
        elif bl > Cmin and bl <= Cmax:
            bl_garde = "C"
            bl_score = 18
        else:
            bl_garde = "F"
            bl_score = 9
        
        return bl_garde, bl_score
    
    def md_calculator(self):
        md = self.md
        threshold = self.threshold
        
        Amin = threshold['A'][0]
        Amax = threshold['A'][1]
        Bmin = threshold['B'][0]
        Bmax = threshold['B'][1]
        Cmin = threshold['C'][0]
        Cmax = threshold['C'][1]
        
        md_garde = ""
        md_score = 0
        
        if md >= Amin and md <= Amax:
            md_garde = "A"
            md_score = 30
        elif md > Bmin and md <= Bmax:
            md_garde = "B"
            md_score = 24
        elif md > Cmin and md <= Cmax:
            md_garde = "C"
            md_score = 18
        else:
            md_garde = "F"
            md_score = 9
        
        return md_garde, md_score
    
    def finalscore(self, bl_score, md_score):
        final_score = bl_score + md_score
        return final_score
        