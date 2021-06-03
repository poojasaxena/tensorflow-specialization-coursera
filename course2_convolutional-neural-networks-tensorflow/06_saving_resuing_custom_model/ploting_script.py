import matplotlib.pyplot as plt

fig = plt.figure()
fig.patch.set_facecolor('white')

def plot_n_model(n=2, model_history=[],
          ylim_low=0.4, ylim_high=1.0, 
          label_list=[]    ,       
                 leg_loc='lower left', is_saved_history=False):
    """
    n: no of history to be plotted
    model_history : list of history name, ex [history_1, history_2]
    label_list : list of label names, ex ['simple_model', 'model_cnn']
    y_lim_low : lowest y scale
    y_lim_high : highest y scale
    leg_loc : location of legend ex: 'lower left', 'lower right', 'upper right', 'upper left'
    is_saved_history : if plotting saved history via pickle 
                     try:
                      import dill as pickle
                     except ImportError:
                        import pickle
                     with open('trainHistoryDict', 'wb') as file_pi:
                     pickle.dump(history.history, file_pi)
                     calling_saved_history = pickle.load(open('trainHistoryDict', "rb"))

    @usage::plot_n_model(n=2, model_history=[history1, history2], label_list=['simple', 'complex'])
    """
    fig = plt.figure(figsize=(15,5))

    assert(len(model_history) ==n)
    
    variable1, variable2='accuracy','val_accuracy'
    variable3, variable4='loss', 'val_loss'
    
    color=['red','blue', 'orange', 'green', 'black', 'aqua','yellow']
    
    plt.subplot(1,2,1)
    for index, history in enumerate(model_history):
        #print(index, history)

        if is_saved_history:
            plt.plot(history[variable1], label=label_list[index], c=color[index], ls='-')
            plt.plot(history[variable2], c=color[index],ls='--')
        else:
            plt.plot(history.history[variable1], label=label_list[index], c=color[index], ls='-')
            plt.plot(history.history[variable2], c=color[index],ls='--')            

        plt.ylabel(variable1)
        plt.xlabel('Epoch')
        plt.grid(True)
        plt.legend(loc=leg_loc)
        plt.title('Training - , Validation ---')

        
    plt.subplot(1,2,2)
    for index, history in enumerate(model_history):

        if is_saved_history:
            plt.plot(history[variable3], label=label_list[index], c=color[index], ls='-')
            plt.plot(history[variable4],  c=color[index],ls='--')
        else:
            plt.plot(history.history[variable3], label=label_list[index], c=color[index], ls='-')
            plt.plot(history.history[variable4],  c=color[index],ls='--')
            
        plt.title('Training - , Validation ---')

    plt.xlabel('Epoch')
    plt.ylabel(variable3)
    plt.grid(True)
    plt.legend(loc=leg_loc)
    plt.ylim(ylim_low,ylim_high)

help(plot_n_model)
