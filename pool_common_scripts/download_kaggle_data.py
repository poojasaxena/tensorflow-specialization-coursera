"""
To download kaggle data.
Author: Pooja SAXENA
Datum : 02 Oktober 2021
Place : Hamburg
"""
import os
import zipfile
import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi
    

def upload_kaggle_dataset(kaggle_dataset_name, base_dir_name):
    """
    kaggle_dataset_name: name of the dataset to be downloaded, 
    base_dir_name: some directory where it suppose to be downloaded
    """
    if os.path.exists(base_dir_name):
        print(f"Dataset {kaggle_dataset_name} is avalable in {base_dir_name} with content: \n {os.listdir(base_dir_name)}")
        return
    else:
        print("Authenticating kaggle API======")
        api=KaggleApi()
        api.authenticate()
        print("Authenticated, downloading Dataset =======")
        api.competition_download_files(kaggle_dataset_name)
    
        with zipfile.ZipFile(kaggle_dataset_name+'.zip', mode='r') as zip_ref:
            zip_ref.extractall(base_dir_name)
            zip_ref.close()
        print(f"Dataset {kaggle_dataset_name} is downloaded in {base_dir_name} with content: \n {os.listdir(base_dir_name)}")
        
help(upload_kaggle_dataset)
