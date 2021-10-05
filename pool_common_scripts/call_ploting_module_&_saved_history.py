#!/usr/bin/env python

import sys
sys.path.append("/home/pooja/Documents/weiterbildung/deep-learning/coursera/tensorflow-developer-professional-specialization/tensor-flow-git/common_scripts_pool")

from ploting_script import plot_n_model

## history
try: 
    import dill as pickle                                                    
except ImportError:                                                         
    import pickle  

    
## Open saved history
path = "/home/pooja/Documents/weiterbildung/deep-learning/coursera/tensorflow-developer-professional-specialization/tensor-flow-git/course2_convolutional-neural-networks-tensorflow/08_imbalanced_dataset/trained_augmentatedhistory_Dict"    

calling_saved_history = pickle.load(open(path, "rb"))         

plot_n_model(num_history=1, 
             name_history=[calling_saved_history], 
             label_list=['simple'], 
             ylim_low=0,
             ylim_high=1.25,
             is_saved_history=True, 
             is_sparse_categorical=True)





