#!/usr/bin/env python
# coding: utf-8

import os
import sys

script_path = os.environ.get('DirForPoolScript')
sys.path.append(script_path)
from ploting_script import plot_n_model

## history
try: 
    import dill as pickle                                                    
except ImportError:                                                         
    import pickle  
    
model_path = os.environ.get("DirForSavedModel")

path = model_path + '/dog_cat_classifier/history_dogcat_classifier_vgg_tLearn_95acc_okt21'  
calling_saved_history = pickle.load(open(path, "rb"))         

plot_n_model(num_history=1, 
             name_history=[calling_saved_history], 
             label_list=['simple'], 
             ylim_low=0,
             ylim_high=1.25,
             is_saved_history=True, 
             is_sparse_categorical=False)
