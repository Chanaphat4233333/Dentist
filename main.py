import yaml
import pandas as pd
import os
from datetime import datetime
from fastapi import FastAPI, HTTPException
import uvicorn
from Services.cluster_35_PFMC.occ import Occ
from Services.cluster_35_PFMC.buccal import Buccal
from Services.cluster_35_PFMC.lingual import Lingual
from Services.cluster_35_PFMC.proximal import Proximal
from Services.cluster_35_PFMC.finishing_line import FinishingLine
from Services.cluster_35_PFMC.TOC import TOC


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
    FinishinglineB_theshold = config35PFMC['FinishinglineB_theshold']
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
            Distal = float(data.iloc[i+2, 17])
            BTheshold = FinishinglineB_theshold,
            LTheshold = FinishinglineL_theshold,
            filename = file_name,
            fixatrow = i+1,
            filenameDB = file_name_db
        )
        TOC_method = TOC(
            MD = float(data.iloc[i+2, 18]),
            UndercutMD = float(data.iloc[i+2, 19]),
            BL = float(data.iloc[i+2, 20]),
            UndercutBL = float(data.iloc[i+2, 21]),
            threshold = TOC_theshold,
            filename = file_name,
            fixatrow = i+1,
            filenameDB = file_name_db
        )
        score_occ = OCC_method.Finalscore()
        score_buccal = Buccal_method.Finalscore()
        score_lingual = Lingual_method.Finalscore()
        score_proximal = Proximal_method.Finalscore()
        score_finishingline = Finishingline_method.Finalscore()
        score_TOC = TOC_method.Finalscore()

        print("score_occ-->", score_occ)
        


    return file_path_result
    

app = FastAPI()

@app.get("/api/v1/data-path/{file_path:path}")
def get_cluster_data(file_path: str):
    try:
        config = loadConfig()

        data, data_range = loadDataSet(file_path)

        calculation_results = cluster_35_PFMC(config, data, data_range)

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