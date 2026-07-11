import yaml
import pandas as pd
import os
from datetime import datetime
from fastapi import FastAPI, HTTPException
import uvicorn
from Services.cluster_35_PFMC.occ import Occ

def loadConfig():
    with open("config.yml", "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)
    return config
def loadDataSet(path):
    data = pd.read_csv(path)
    data_range = data.max_row -3
    
    return data, data_range
    

def cluster_35_PFMC(config, data, data_range):
    config35PFMC = config['cluster_35_PFMC']
    OCC_theshold = config35PFMC['OCC_theshold']
    time_stamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    file_name = f"cluster_35_PFMC_{time_stamp}.csv"
    file_header = config35PFMC['Header_Format']
    folder_name_result = "results"
    
    if not os.path.exists(folder_name_result):
        os.makedirs(folder_name_result)
    
    file_path_result = os.path.join(folder_name_result, file_name)
    df = pd.DataFrame(columns=file_header)
    df.to_csv(file_path_result, index=False, encoding="utf-8-sig")
    for i in range (data_range) :
        test = Occ(
            id  = data.iloc[i+3,0],
            name = data.iloc[i+3,2],
            central=data.iloc[i+3,4],
            Bfunc=data.iloc[i+3,5],
            L_of_B=data.iloc[i+3,6],
            L_non=data.iloc[i+3,7],
            B_incline=data.iloc[i+3,8],
            theshold=OCC_theshold,
            filename = file_name,
            fixatrow = i+1
            )
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