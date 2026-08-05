class OCC_16PFMC:
    def __init__(self, mb_cusp, mb_incline, mb_groove, ml_cusp, ml_incline, ml_groove, db_cusp, db_incline, db_groove, dl_cusp, dl_incline, dl_groove, threshold):
        self.mb_cusp = mb_cusp
        self.mb_incline = mb_incline
        self.mb_groove = mb_groove

        self.ml_cusp = ml_cusp
        self.ml_incline = ml_incline
        self.ml_groove = ml_groove

        self.db_cusp = db_cusp
        self.db_incline = db_incline
        self.db_groove = db_groove

        self.dl_cusp = dl_cusp
        self.dl_incline = dl_incline
        self.dl_groove = dl_groove

        self.threshold = threshold

        self.mdfinalscore, self.cusp_mdgrade, self.incline_mdgrade, self.groove_mdgrade = self.mb_calculator()
        self.mlfinalscore, self.cusp_mlgrade, self.incline_mlgrade, self.groove_mlgrade = self.ml_calculator()
        self.dbfinalscore, self.cusp_dbgrade, self.incline_dbgrade, self.groove_dbgrade = self.db_calculator()
        self.dlfinalscore, self.cusp_dlgrade, self.incline_dlgrade, self.groove_dlgrade = self.dl_calculator()

        self.final_score = self.finalscore(self.mdfinalscore, self.mlfinalscore, self.dbfinalscore, self.dlfinalscore)

    def mb_calculator(self):
        cusp  = self.mb_cusp
        incline = self.mb_incline
        groove = self.mb_groove
        threshold= self.threshold

        cusp_score = 0
        incline_score = 0
        groove_score = 0


        Amin  = threshold['A'][0]
        Amax = threshold['A'][1]
        Bmin = threshold['B'][0]
        Bmax = threshold['B'][1]
        Cmin = threshold['C'][0]
        Cmax = threshold['C'][1]

        cusp_grade = "N/A"
        incline_grade = "N/A"
        groove_grade = "N/A"

        if cusp >= Amin and cusp < Amax:
            cusp_grade = "A"
            cusp_score = 5
        elif cusp >= Bmin and cusp < Bmax:
            cusp_grade = "B"
            cusp_score = 4
        elif cusp >= Cmin and cusp < Cmax:
            cusp_grade = "C"
            cusp_score = 3
        else:
            cusp_grade = "F"
            cusp_score = 1.5

        if incline >= Amin and incline < Amax:
            incline_grade = "A"
            incline_score = 5
        elif incline >= Bmin and incline< Bmax:
            incline_grade = "B"
            incline_score = 4
        elif incline >= Cmin and incline < Cmax:
            incline_grade = "C"
            incline_score = 3
        else:
            incline_grade = "F"
            incline_score = 1.5

        if groove >= Amin and groove < Amax:
            groove_grade = "A"
            groove_score = 5
        elif incline >= Bmin and incline< Bmax:
            groove_grade = "B"
            groove_score = 4
        elif groove >= Cmin and groove < Cmax:
            groove_grade = "C"
            groove_score = 3
        else:
            groove_grade = "F"
            groove_score = 1.5

        finalscore = cusp_score + incline_score + groove_score


        return finalscore, cusp_grade, incline_grade, groove_grade

    def ml_calculator(self):
        cusp  = self.ml_cusp
        incline = self.ml_incline
        groove = self.ml_groove
        threshold= self.threshold
    
        cusp_score = 0
        incline_score = 0
        groove_score = 0
    
    
        Amin  = threshold['A'][0]
        Amax = threshold['A'][1]
        Bmin = threshold['B'][0]
        Bmax = threshold['B'][1]
        Cmin = threshold['C'][0]
        Cmax = threshold['C'][1]
    
        cusp_grade = "N/A"
        incline_grade = "N/A"
        groove_grade = "N/A"
    
        if cusp >= Amin and cusp < Amax:
            cusp_grade = "A"
            cusp_score = 5
        elif cusp >= Bmin and cusp < Bmax:
            cusp_grade = "B"
            cusp_score = 4
        elif cusp >= Cmin and cusp < Cmax:
            cusp_grade = "C"
            cusp_score = 3
        else:
            cusp_grade = "F"
            cusp_score = 1.5
    
        if incline >= Amin and incline < Amax:
            incline_grade = "A"
            incline_score = 5
        elif incline >= Bmin and incline< Bmax:
            incline_grade = "B"
            incline_score = 4
        elif incline >= Cmin and incline < Cmax:
            incline_grade = "C"
            incline_score = 3
        else:
            incline_grade = "F"
            incline_score = 1.5
    
        if groove >= Amin and groove < Amax:
            groove_grade = "A"
            groove_score = 5
        elif incline >= Bmin and incline< Bmax:
            groove_grade = "B"
            groove_score = 4
        elif groove >= Cmin and groove < Cmax:
            groove_grade = "C"
            groove_score = 3
        else:
            groove_grade = "F"
            groove_score = 1.5
    
        finalscore = cusp_score + incline_score + groove_score
    
    
        return finalscore, cusp_grade, incline_grade, groove_grade

    def db_calculator(self):
        cusp  = self.db_cusp
        incline = self.db_incline
        groove = self.db_groove
        threshold= self.threshold

        cusp_score = 0
        incline_score = 0
        groove_score = 0

        Amin  = threshold['A'][0]
        Amax = threshold['A'][1]
        Bmin = threshold['B'][0]
        Bmax = threshold['B'][1]
        Cmin = threshold['C'][0]
        Cmax = threshold['C'][1]

        cusp_grade = "N/A"
        incline_grade = "N/A"
        groove_grade = "N/A"

        if cusp >= Amin and cusp < Amax:
            cusp_grade = "A"
            cusp_score = 5
        elif cusp >= Bmin and cusp < Bmax:
            cusp_grade = "B"
            cusp_score = 4
        elif cusp >= Cmin and cusp < Cmax:
            cusp_grade = "C"
            cusp_score = 3
        else:
            cusp_grade = "F"
            cusp_score = 1.5

        if incline >= Amin and incline < Amax:
            incline_grade = "A"
            incline_score = 5
        elif incline >= Bmin and incline< Bmax:
            incline_grade = "B"
            incline_score = 4
        elif incline >= Cmin and incline < Cmax:
            incline_grade = "C"
            incline_score = 3
        else:
            incline_grade = "F"
            incline_score = 1.5

        if groove >= Amin and groove < Amax:
            groove_grade = "A"
            groove_score = 5
        elif incline >= Bmin and incline< Bmax:
            groove_grade = "B"
            groove_score = 4
        elif groove >= Cmin and groove < Cmax:
            groove_grade = "C"
            groove_score = 3
        else:
            groove_grade = "F"
            groove_score = 1.5

        finalscore = cusp_score + incline_score + groove_score


        return finalscore, cusp_grade, incline_grade, groove_grade

    def dl_calculator(self):
        cusp  = self.dl_cusp
        incline = self.dl_incline
        groove = self.dl_groove
        threshold= self.threshold

        cusp_score = 0
        incline_score = 0
        groove_score = 0

        Amin  = threshold['A'][0]
        Amax = threshold['A'][1]
        Bmin = threshold['B'][0]
        Bmax = threshold['B'][1]
        Cmin = threshold['C'][0]
        Cmax = threshold['C'][1]

        cusp_grade = "N/A"
        incline_grade = "N/A"
        groove_grade = "N/A"

        if cusp >= Amin and cusp < Amax:
            cusp_grade = "A"
            cusp_score = 5
        elif cusp >= Bmin and cusp < Bmax:
            cusp_grade = "B"
            cusp_score = 4
        elif cusp >= Cmin and cusp < Cmax:
            cusp_grade = "C"
            cusp_score = 3
        else:
            cusp_grade = "F"
            cusp_score = 1.5

        if incline >= Amin and incline < Amax:
            incline_grade = "A"
            incline_score = 5
        elif incline >= Bmin and incline< Bmax:
            incline_grade = "B"
            incline_score = 4
        elif incline >= Cmin and incline < Cmax:
            incline_grade = "C"
            incline_score = 3
        else:
            incline_grade = "F"
            incline_score = 1.5

        if groove >= Amin and groove < Amax:
            groove_grade = "A"
            groove_score = 5
        elif incline >= Bmin and incline< Bmax:
            groove_grade = "B"
            groove_score = 4
        elif groove >= Cmin and groove < Cmax:
            groove_grade = "C"
            groove_score = 3
        else:
            groove_grade = "F"
            groove_score = 1.5

        finalscore = cusp_score + incline_score + groove_score


        return finalscore, cusp_grade, incline_grade, groove_grade
    
    def finalscore(self, mb_score, ml_score, db_score, dl_score):
        finalscore = mb_score + ml_score + db_score + dl_score
        return finalscore   