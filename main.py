import yaml
import pandas as pd
import os
from datetime import datetime
from fastapi import FastAPI, HTTPException
from pkg.crypto import encrypt_aes256
import uvicorn
from Services.cluster_35_PFMC.occ import Occ
from Services.cluster_35_PFMC.buccal import Buccal
from Services.cluster_35_PFMC.lingual import Lingual
from Services.cluster_35_PFMC.proximal import Proximal
from Services.cluster_35_PFMC.finishing_line import FinishingLine
from Services.cluster_35_PFMC.TOC import TOC

from Services.cluster_11_lithium.incisal import Incisal
from Services.cluster_11_lithium.buccal import Buccal_11
from Services.cluster_11_lithium.lingual import Lingual_11
from Services.cluster_11_lithium.proximal import Proximal_11
from Services.cluster_11_lithium.finishing_line import FinishingLine_11
from Services.cluster_11_lithium.toc import Toc_11

from Services.cluster_16_PFMC.occ import OCC_16PFMC
from Services.cluster_16_PFMC.buccal import Buccal_16PFMC
from Services.cluster_16_PFMC.lingual import Lingual_16PFMC
from Services.cluster_16_PFMC.proximal import Proximal_16PFMC
from Services.cluster_16_PFMC.finishing_line import Finishing_line_16PFMC
from Services.cluster_16_PFMC.toc import TOC_16PFMC


def loadConfig():
    with open("config.yml", "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)
    return config
def loadDataSet(path):
    data = pd.read_csv(path)
    data_range = len(data) - 3
    
    return data, data_range
    

def cluster_35_PFMC(config, data, data_range):
    config35PFMC = config['cluster_35_PFMC']
    OCC_theshold = config35PFMC['OCC_theshold']
    Buccal_theshold = config35PFMC['Buccal_theshold']
    Lingual_theshold = config35PFMC['Lingual_theshold']
    Proximal_theshold = config35PFMC['Proximal_theshold']
    FinishinglineB_theshold = config35PFMC['FinishingLineB_theshold']
    FinishinglineL_theshold = config35PFMC['FinishingLineL-Distal_theshold']
    TOC_theshold = config35PFMC['TOC_theshold']

    time_stamp = datetime.now().strftime("%Y-%m-%d")
    file_name = f"cluster_35_PFMC_{time_stamp}.csv"
    file_name_db = f"cluster_35_PFMC_{time_stamp}_encrypt.csv"

    file_header = config35PFMC['Header_Format']
    folder_name_result = "results"
    folder_name_encrypt = "results_encrypt"
    
    if not os.path.exists(folder_name_result):
        os.makedirs(folder_name_result)
    if not os.path.exists(folder_name_encrypt):
        os.makedirs(folder_name_encrypt)
    
    file_path_result = os.path.join(folder_name_result, file_name)
    file_path_encrypt = os.path.join(folder_name_encrypt, file_name_db)
    df = pd.DataFrame(columns=file_header)

    df.to_csv(file_path_result, index=False, encoding="utf-8-sig")
    df_enc = pd.DataFrame(columns=file_header)
    df_enc.to_csv(file_path_encrypt, index=False, encoding="utf-8-sig")

    all_results = []
    all_results_encrypt = []
    crypto_config = config['Encrypt']
    secretkey = crypto_config['secret']
    for i in range (data_range) :
        OCC_method = Occ(
            id  = data.iloc[i+2,0],
            name = data.iloc[i+2,2],
            central = float(data.iloc[i+2,3]),
            Bfunc = float(data.iloc[i+2,4]),
            L_of_B = float(data.iloc[i+2,5]),
            L_non = float(data.iloc[i+2,6]),
            B_incline = float(data.iloc[i+2,7]),
            theshold=OCC_theshold,
            filename = file_name,
            fixatrow = i+1,
            secretkey = secretkey,
            filenameDB = file_name_db
            )
        Buccal_method = Buccal(
            Bplane1 = float(data.iloc[i+2,8]),
            Bplane2 = float(data.iloc[i+2,9]),
            threshold = Buccal_theshold,
            filename = file_name,
            fixatrow = i+1,
            filenameDB = file_name_db
        )

        Lingual_method = Lingual(
            Lplane1 = float(data.iloc[i+2,10]),
            Lplane2 = float(data.iloc[i+2,11]),
            threshold = Lingual_theshold,
            filename = file_name,
            fixatrow = i+1,
            filenameDB = file_name_db
        )
        Proximal_method = Proximal(
            Mesial = float(data.iloc[i+2,12]),
            Distal = float(data.iloc[i+2,13]),
            threshold = Proximal_theshold,
            filename = file_name,
            fixatrow = i+1,
            filenameDB = file_name_db
        )
        Finishingline_method = FinishingLine(
            Buccal = float(data.iloc[i+2,14]),
            Lingual = float(data.iloc[i+2,15]),
            Mesial = float(data.iloc[i+2, 16]),
            Distal = float(data.iloc[i+2, 17]),
            BTheshold = FinishinglineB_theshold,
            LTheshold = FinishinglineL_theshold,
            filename = file_name,
            fixatrow = i+1,
            filenameDB = file_name_db
        )
        TOC_method = TOC(
            MD = float(data.iloc[i+2, 18]),
            UndercutMD = str(data.iloc[i+2, 19]),
            BL = float(data.iloc[i+2, 20]),
            UndercutBL = str(data.iloc[i+2, 21]),
            threshold = TOC_theshold,
            filename = file_name,
            fixatrow = i+1,
            filenameDB = file_name_db
        )

        rowdata = {
            'student_id': OCC_method.id,
            'name': OCC_method.name,
            'OCC_score': OCC_method.final_score,
            'OCC_Grade': "",
            'OCC_central-groove_grade': OCC_method.Grade_Cental_groove,
            'OCC_B-func_grade': OCC_method.Grade_Occ_B,
            'OCC_L-incline of B cusp_grade': OCC_method.Grade_L_of_B,
            'OCC_L nonfunc_grade': OCC_method.Grade_Lnon,
            'OCC_B incline of L cusp_grade': OCC_method.Grade_BofL,

            'Buccal_score': Buccal_method.final_score,
            'Buccal_Grade': "",
            'Buccal_B plane1_grade': Buccal_method.Grade_Buccal_Bplane1,
            'Buccal_B plane2_grade': Buccal_method.Grade_Buccal_Bplane2,

            'Lingual_score': Lingual_method.final_score,
            'Lingual_Grade': "",
            'Lingual_plane1_grade': Lingual_method.Grade_Lplane1,
            'Lingual_plane2_grade': Lingual_method.Grade_Lplane2,

            'Proximal_score': Proximal_method.final_score,
            'Proximal_Grade': "",
            'Proximal_Mesial_grade': Proximal_method.Grade_Mesial,
            'Proximal_Distal_grade': Proximal_method.Grade_Distal,

            'FinishingLine_score': Finishingline_method.final_score,
            'FinishingLine_Grade': "",
            'FinishingLine_Buccal_grade': Finishingline_method.Grade_Buccal,
            'FinishingLine_Lingual_grade': Finishingline_method.Grade_Lingual,
            'FinishingLine_Mesial_grade': Finishingline_method.Grade_Mesial,
            'FinishingLine_Distal_grade': Finishingline_method.Grade_Distal,

            'TOC_score': TOC_method.final_score,
            'TOC_Grade': "",
            'TOC_BL_grade': TOC_method.Grade_BL,
            'TOC_MD_grade': TOC_method.Grade_MD,

            'TOTAL': OCC_method.final_score + Buccal_method.final_score + Lingual_method.final_score + Proximal_method.final_score + Finishingline_method.final_score + TOC_method.final_score,
            'Grade_overall': "",

        }
        name_encrypt = encrypt_aes256(OCC_method.name, secretkey)
        row_data_enc = rowdata.copy()
        row_data_enc["name"] = name_encrypt.hex()
        
        all_results.append(rowdata)
        all_results_encrypt.append(row_data_enc)

  
    df = pd.DataFrame(all_results, columns=file_header)
    df.to_csv(file_path_result, index=False, encoding="utf-8-sig")
    
    df_enc = pd.DataFrame(all_results_encrypt, columns=file_header)
    df_enc.to_csv(file_path_encrypt, index=False, encoding="utf-8-sig")


    return file_path_result

def cluster_11_lithium(config, data, data_range):
    config_11_lithium = config['cluster_11_lithium']
    incisal_edge_threshold = config_11_lithium['incisal_edge']
    buccal_threshold = config_11_lithium['Buccal']
    lingual_threshold = config_11_lithium['Lingual']
    proximal_threshold = config_11_lithium['Proximal']
    finishing_line_threshold = config_11_lithium['Finishing_line']
    toc_threshold = config_11_lithium['TOC']
    final_score = config_11_lithium['Final_score']
    
    time_stamp = datetime.now().strftime("%Y-%m-%d")
    file_name = f"cluster_11_lithium_{time_stamp}.csv"
    file_name_db = f"cluster_11_lithium_{time_stamp}_encrypt.csv"
    
    file_header = config_11_lithium['Header_Format']
    folder_name_result = "results"
    folder_name_encrypt = "results_encrypt"
    
    if not os.path.exists(folder_name_result):
        os.makedirs(folder_name_result)
    if not os.path.exists(folder_name_encrypt):
        os.makedirs(folder_name_encrypt)
    
    file_path_result = os.path.join(folder_name_result, file_name)
    file_path_encrypt = os.path.join(folder_name_encrypt, file_name_db)
    df = pd.DataFrame(columns=file_header)
    
    df.to_csv(file_path_result, index=False, encoding="utf-8-sig")
    df_enc = pd.DataFrame(columns=file_header)
    df_enc.to_csv(file_path_encrypt, index=False, encoding="utf-8-sig")
    
    all_results = []
    all_results_encrypt = []
    
    crypto_config = config['Encrypt']
    secretkey = crypto_config['secret']
    gradeA = 0
    gradeB = 0
    gradeC = 0
    gradeF = 0
    for i in range(data_range):
        Incisal_method = Incisal(
            incisal = float(data.iloc[i+2,2]),
            threshold = incisal_edge_threshold
            )
        
        buccal_method = Buccal_11(
            md1 = float(data.iloc[i+2,3]),
            md2 = float(data.iloc[i+2,4]),
            threshold = buccal_threshold
        )
        
        lingual_method = Lingual_11(
            L1 = float(data.iloc[i+2,5]),
            L2 = float(data.iloc[i+2,6]),
            threshold = lingual_threshold
        )
        proximal_method = Proximal_11(
            mesial = float(data.iloc[i+2,7]),
            distal = float(data.iloc[i+2,8]),
            threshold = proximal_threshold
        )
        finishing_line_method = FinishingLine_11(
            b = float(data.iloc[i+2,9]),
            l = float(data.iloc[i+2,10]),
            mesial = float(data.iloc[i+2,11]),
            distal = float(data.iloc[i+2,12]),
            threshold = finishing_line_threshold
        )
        toc_method = Toc_11(
            bl = float(data.iloc[i+2,13]),
            md = float(data.iloc[i+2,14]),
            threshold = toc_threshold
        )
        final_grade = "N/A"
        
        issue =""
        undercut = str(data.iloc[i+2,15])
        
            
        
        finalscore = Incisal_method.final_score + buccal_method.final_score + lingual_method.final_score + proximal_method.final_score + finishing_line_method.final_score + toc_method.final_score
        if undercut == "no":
            if finalscore >= final_score['A'][0] and finalscore <= final_score['A'][1]:
                final_grade = "A"
                gradeA +=1
            elif finalscore >= final_score['B'][0] and finalscore < final_score['B'][1]:
                final_grade = "B"
                gradeB +=1
            elif finalscore >= final_score['C'][0] and finalscore < final_score['C'][1]:
                final_grade = "C"
                gradeC +=1
            else:
                gradeF +=1
                final_grade = "F"
        else:
            gradeF +=1
            issue = "undercut"
            final_grade = "F"
            
        
        rowdata = {
            "student_id": str(data.iloc[i+2,0]),
            "name": str(data.iloc[i+2,1]),
            "total_score": finalscore,
            "final_garde": final_grade,
            "incisal_score": Incisal_method.final_score,
            "incisal_grade": Incisal_method.incisal_grade,
            "buccal_score" : buccal_method.final_score,
            "buccal_BP1_grade": buccal_method.Grade_md1,
            "buccal_BP2_grade": buccal_method.Grade_md2,
            "ligual_score" : lingual_method.final_score,
            "ligual_LP1_grade": lingual_method.L1_grade,
            "ligual_LP2_grade": lingual_method.L2_grade,
            "proximal_score": proximal_method.final_score,
            "proximal_mesial_garde": proximal_method.mesial_grade,
            "proximal_distal_garde": proximal_method.distal_grade,
            "finishing_line_score": finishing_line_method.final_score,
            "finishing_line_B_garde": finishing_line_method.b_grade,
            "finishing_line_L_garde": finishing_line_method.l_grade,
            "finishing_line_mesial_garde": finishing_line_method.mesial_grade,
            "finishing_line_distal_garde": finishing_line_method.distal_grade,
            "toc_score": toc_method.final_score,
            "toc_bl_grade": toc_method.bl_garde,
            "toc_md_grade": toc_method.md_garde,
            "issue":issue
            
        }
        
        name_encrypt = encrypt_aes256(rowdata["name"], secretkey)
        row_data_enc = rowdata.copy()
        row_data_enc["name"] = name_encrypt.hex()
        
        all_results.append(rowdata)
        all_results_encrypt.append(row_data_enc)
    
    
    
    df = pd.DataFrame(all_results, columns=file_header)
    totalstudent = len(all_results)

    summary_data = {
        "Summary": ["total", "A", "B", "C", "F"], 
        "Count": [totalstudent, gradeA, gradeB, gradeC, gradeF],
    }
    count_score_df = pd.DataFrame(summary_data)


    final_df = pd.concat([df, count_score_df], axis=1)
    final_df.to_csv(file_path_result, index=False, encoding="utf-8-sig")
        
    df_enc = pd.DataFrame(all_results_encrypt, columns=file_header)
    df_enc.to_csv(file_path_encrypt, index=False, encoding="utf-8-sig")
    
    
    return file_path_result

def cluster_16_PFMC(config, data, data_range):
    config_16_PFMC = config['cluster_16_PFMC']
    occ_16PFMC_threshold = config_16_PFMC['occ_16PFMC']
    buccal_16PFMC_threshold = config_16_PFMC['buccal_16PFMC']
    lingual_16PFMC_threshold = config_16_PFMC['lingual_16PFMC']
    proximal_16PFMC_threshold = config_16_PFMC['proximal_16PFMC']
    finishingline1_threshold = config_16_PFMC['finishing_line_MDandDB']
    finishingline2_threshold = config_16_PFMC['finishing_line_ML-DL']
    toc_16PFMC_threshold = config_16_PFMC['toc_16PFMC']
    final_score = config_16_PFMC['Final_score']

    time_stamp = datetime.now().strftime("%Y-%m-%d")
    file_name = f"cluster_16_PFMC_{time_stamp}.csv"
    file_name_db = f"cluster_16_PFMC_{time_stamp}_encrypt.csv"
        
    file_header = config_16_PFMC['Header_Format']
    folder_name_result = "results"
    folder_name_encrypt = "results_encrypt"

    if not os.path.exists(folder_name_result):
        os.makedirs(folder_name_result)
    if not os.path.exists(folder_name_encrypt):
        os.makedirs(folder_name_encrypt)
        
    file_path_result = os.path.join(folder_name_result, file_name)
    file_path_encrypt = os.path.join(folder_name_encrypt, file_name_db)
    df = pd.DataFrame(columns=file_header)
        
    df.to_csv(file_path_result, index=False, encoding="utf-8-sig")
    df_enc = pd.DataFrame(columns=file_header)
    df_enc.to_csv(file_path_encrypt, index=False, encoding="utf-8-sig")
        
    all_results = []
    all_results_encrypt = []
        
    crypto_config = config['Encrypt']
    secretkey = crypto_config['secret']
    gradeA = 0
    gradeB = 0
    gradeC = 0
    gradeF = 0

    # for i in range(data_range):
    
    for i in range(data_range):
        occ_16PFMC = OCC_16PFMC(
            mb_cusp = float(data.iloc[i+2,3]),
            mb_incline = float(data.iloc[i+2,4]),
            mb_groove = float(data.iloc[i+2,5]),
            ml_cusp = float(data.iloc[i+2,6]),
            ml_incline = float(data.iloc[i+2,7]),
            ml_groove = float(data.iloc[i+2,8]),
            db_cusp = float(data.iloc[i+2,9]),
            db_incline = float(data.iloc[i+2,10]),
            db_groove = float(data.iloc[i+2,11]),
            dl_cusp = float(data.iloc[i+2,12]),
            dl_incline = float(data.iloc[i+2,13]),
            dl_groove = float(data.iloc[i+2,14]),
            threshold = occ_16PFMC_threshold
        )
        buccal_16PFMC = Buccal_16PFMC(
            mbp1 = float(data.iloc[i+2,15]),
            mbp2 = float(data.iloc[i+2,16]),
            dbp1 = float(data.iloc[i+2,17]),
            dbp2 = float(data.iloc[i+2,18]),
            threshold = buccal_16PFMC_threshold
        )
        lingual_16PFMC =Lingual_16PFMC(
            mlp1 = float(data.iloc[i+2,19]),
            mlp2 = float(data.iloc[i+2,20]),
            dlp1 = float(data.iloc[i+2,21]),
            dlp2 = float(data.iloc[i+2,22]),
            threshold = lingual_16PFMC_threshold
        )
        proximal_16PFMC = Proximal_16PFMC(
            mesial = float(data.iloc[i+2,23]),
            distal = float(data.iloc[i+2,24]),
            threshold = proximal_16PFMC_threshold
        )
        finishing_line_16PFMC = Finishing_line_16PFMC(
            mb = float(data.iloc[i+2,25]),
            ml = float(data.iloc[i+2,26]),
            db = float(data.iloc[i+2,27]),
            dl = float(data.iloc[i+2,28]),
            mesial = float(data.iloc[i+2,29]),
            distal = float(data.iloc[i+2,30]),
            threshold1 = finishingline1_threshold,
            threshold2 = finishingline2_threshold
        )
        toc_16PFMC = TOC_16PFMC(
            md = float(data.iloc[i+2,31]),
            bl = float(data.iloc[i+2,32]),
            threshold = toc_16PFMC_threshold
        )
        final_grade = "N/A"
        issue =""
        undercut = str(data.iloc[i+2,33])
        finalscore = occ_16PFMC.final_score + buccal_16PFMC.final_score + lingual_16PFMC.final_score + proximal_16PFMC.final_score + finishing_line_16PFMC.final_score + toc_16PFMC.final_score
        if undercut == "no":
            if finalscore >= final_score['A'][0] and finalscore <= final_score['A'][1]:
                final_grade = "A"
                gradeA +=1
            elif finalscore >= final_score['B'][0] and finalscore < final_score['B'][1]:
                final_grade = "B"
                gradeB +=1
            elif finalscore >= final_score['C'][0] and finalscore < final_score['C'][1]:
                final_grade = "C"
                gradeC +=1
            else:
                gradeF +=1
                final_grade = "F"
        else:
            gradeF +=1
            issue = "undercut"
            final_grade = "F"
        
        rowdata = {
            "student_id": str(data.iloc[i+2,0]),
            "name": str(data.iloc[i+2,2]),
            "total_score": finalscore,
            "final_garde": final_grade,
            "OCC_score": Incisal_method.final_score,
            "OCC_MB_cusp_grade": Incisal_method.incisal_grade,
            "OCC_MB_incline_grade" : buccal_method.final_score,
            "OCC_MB_groove_grade": buccal_method.Grade_md1,
            "OCC_DB_cusp_grade": buccal_method.Grade_md2,
            "OCC_DB_incline_grade" : lingual_method.final_score,
            "OCC_DB_groove_grade": lingual_method.L1_grade,
            "OCC_ML_cusp_grade": lingual_method.L2_grade,
            "OCC_ML_incline_grade": proximal_method.final_score,
            "OCC_ML_groove_grade": proximal_method.mesial_grade,
            "OCC_DL_cusp_grade": proximal_method.distal_grade,
            "OCC_DL_incline_grade": finishing_line_method.final_score,
            "OCC_DL_groove_grade": finishing_line_method.b_grade,
            "Buccal_score": finishing_line_method.l_grade,
            "Buccal_MBP1_grade": finishing_line_method.mesial_grade,
            "Buccal_MBP2_grade": finishing_line_method.distal_grade,
            "Buccal_DBP1_grade": toc_method.final_score,
            "Buccal_DBP2_grade": toc_method.bl_garde,
            "Lingual_score": toc_method.md_garde,
            "Lingual_MLP1_grade":issue,
            "Lingual_MLP2_grade":issue,
            "Lingual_DLP1_grade":issue,
            "Lingual_DLP2_grade":issue,
            "Proximal_score": proximal_method.final_score,
            "Proximal_mesial_grade": proximal_method.mesial_grade,
            "Proximal_distal_grade": proximal_method.distal_grade,
            "Finishing_line_score": finishing_line_method.final_score,
            "Finishing_line_MB_grade": finishing_line_method.b_grade,
            "Finishing_line_ML_grade": finishing_line_method.l_grade,
            "Finishing_line_DB_grade": finishing_line_method.mesial_grade,
            "Finishing_line_DL_grade": finishing_line_method.distal_grade,
            "Finishing_line_mesial_grade": finishing_line_method.mesial_grade,
            "Finishing_line_distal_grade": finishing_line_method.distal_grade,
            "TOC_score": toc_method.final_score,
            "TOC_MD_grade": toc_method.md_garde,
            "TOC_BL_grade": toc_method.bl_garde,
            "issue":issue
        }
                
        name_encrypt = encrypt_aes256(rowdata["name"], secretkey)
        row_data_enc = rowdata.copy()
        row_data_enc["name"] = name_encrypt.hex()
                
        all_results.append(rowdata)
        all_results_encrypt.append(row_data_enc)
    
    df = pd.DataFrame(all_results, columns=file_header)
    totalstudent = len(all_results)
        
    summary_data = {
        "Summary": ["total", "A", "B", "C", "F"], 
        "Count": [totalstudent, gradeA, gradeB, gradeC, gradeF],
            }
    count_score_df = pd.DataFrame(summary_data)
        
        
    final_df = pd.concat([df, count_score_df], axis=1)
    final_df.to_csv(file_path_result, index=False, encoding="utf-8-sig")
                
    df_enc = pd.DataFrame(all_results_encrypt, columns=file_header)
    df_enc.to_csv(file_path_encrypt, index=False, encoding="utf-8-sig")
    
    return file_path_result
            
        
        
        
        
        

app = FastAPI()

@app.get("/api/v1/data-path/{type:str}/{file_path:path}")
def get_cluster_data(type: str, file_path: str):
    try:
        config = loadConfig()

        data, data_range = loadDataSet(file_path)

        if type == '35_PFMC':
            calculation_results = cluster_35_PFMC(config, data, data_range)
        elif type == '11_lithium':
            calculation_results = cluster_11_lithium(config, data, data_range)
        elif type == '16_PFMC':
            calculation_results = cluster_16_PFMC(config, data, data_range)
        else:
            raise HTTPException(
                status_code=400, detail=f"invalid type: {type}"
            )

        return {
            "status": "success",
            "resource": file_path,
            "total_records": data_range,
            "result_link": calculation_results,
        }

    except HTTPException as http_ex:
        raise http_ex
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"internal server error: {str(e)}"
        )


if __name__ == "__main__":
    config = loadConfig()
    uvicorn.run("main:app", host=config['Network']['host'], port=config['Network']['port'], reload=True)