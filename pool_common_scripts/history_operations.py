import os
import sys
import pickle

saved_model_path = os.environ.get("DirForSavedModel")

def saveHist(project_name, name, history):
    path = os.path.join(saved_model_path, project_name, name)
    
    if os.path.exists(path):
        print(f"{os.path.exists(path)} already exist!")
        return
    else:
        with open(path, "wb") as file_pi:
            pickle.dump(history.history, file_pi)


def loadHist(path):
    if os.path.exist(path):
        saved_history= pickle.load(open(path, "rb"))
    return saved_history
