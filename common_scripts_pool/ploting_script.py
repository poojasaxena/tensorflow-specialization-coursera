import matplotlib.pyplot as plt

fig = plt.figure()
fig.patch.set_facecolor('white')

def plot_n_model(num_history=2, name_history=[],
          ylim_low=0.4, ylim_high=1.0, 
          label_list=[],       
          leg_loc='lower left',
          is_sparse_categorical=False,       
          is_saved_history=False):
    """

    num_history  : no of history to be plotted
    name_history : list of history name, ex [history_1, history_2]
    label_list   : list of label names, ex ['simple_model', 'model_cnn']
    y_lim_low    : lowest y scale
    y_lim_high   : highest y scale
    leg_loc      : location of legend ex: 'lower left', 'lower right', 'upper right', 'upper left'
    is_sparse_categorical : True, if sparse_categorical_accuracy is being used. 
    is_saved_history : if plotting saved history via pickle
 
                     @@ Saving part--
                     try:
                       import dill as pickle
                     except ImportError:
                        import pickle
                     with open('trainHistoryDict', 'wb') as file_pi:
                     pickle.dump(history.history, file_pi)
                     
                     @@ Calling part --
                     try:
                        import dill as pickle
                     except ImportError:
                        import pickle
                     calling_saved_history = pickle.load(open('trainHistoryDict', "rb"))

    @usage::plot_n_model(num_history=2, name_history=[history1, history2], label_list=['simple', 'complex'])
    """
    fig = plt.figure(figsize=(15,5))

    assert(len(name_history) == num_history), 'Error, name_history should be of length num_history!'
    
    if is_sparse_categorical:
        acc_variable = ['sparse_categorical_accuracy', 'val_sparse_categorical_accuracy']
    else:
        acc_variable=['accuracy', 'val_accuracy']
    loss_variable = ['loss', 'val_loss']

    color=['red','blue', 'orange', 'green', 'black', 'aqua','yellow']
    
    plt.subplot(1,2,1)
    for index, history in enumerate(name_history):
        #print(index, history)

        if is_saved_history:
            plt.plot(history[acc_variable[0]], label=label_list[index], c=color[index], ls='-')
            plt.plot(history[acc_variable[1]], c=color[index],ls='--')
        else:
            plt.plot(history.history[acc_variable[0]], label=label_list[index], c=color[index], ls='-')
            plt.plot(history.history[acc_variable[1]], c=color[index],ls='--')            

        plt.ylabel(acc_variable[0])
        plt.xlabel('Epoch')
        plt.grid(True)
        plt.legend(loc=leg_loc)
        plt.title('Training - , Validation ---')

        
    plt.subplot(1,2,2)
    for index, history in enumerate(name_history):

        if is_saved_history:
            plt.plot(history[loss_variable[0]], label=label_list[index], c=color[index], ls='-')
            plt.plot(history[loss_variable[1]],  c=color[index],ls='--')
        else:
            plt.plot(history.history[loss_variable[0]], label=label_list[index], c=color[index], ls='-')
            plt.plot(history.history[loss_variable[1]],  c=color[index],ls='--')
            
        plt.title('Training - , Validation ---')

    plt.xlabel('Epoch')
    plt.ylabel(loss_variable[0])
    plt.grid(True)
    plt.legend(loc=leg_loc)
    plt.ylim(ylim_low,ylim_high)

help(plot_n_model)
