"""
Keras-tuner to be used in image classifiaction application
For downloading the library: #python3 -m pip install --user keras-tuner 
"""
#import keras_tuner as kt
import tensorflow as tf
from keras_tuner import HyperModel
from tensorflow import keras

class CustomHyperModel(HyperModel):

    def __init__(self, is_vgg=False, l1_value=0):
        self.is_vgg = is_vgg
        self.l1_value = l1_value
        
    def build(self, hp_model):
        if self.is_vgg:
            input_image_shape = (28, 28, 1)
        else:
            input_image_shape = (28,28)
            
        model = keras.Sequential()        
        model.add(keras.layers.Embedding())
        for i in range(hp_model.Int('conv_blocks', 3, 5, default=3)):
            filters = hp_model.Int('filters_' + str(i), 32, 256, step=32)
            
            for _ in range(2):
                model.add(keras.layers.Conv2D(filters, kernel_size=(3,3), padding='same', input_shape=input_image_shape))
                model.add(keras.layers.BatchNormalization())
                model.add(keras.layers.ReLU())
            
            if hp_model.Choice('pooling' + str(i), ['avg', 'max']) == 'max' :
                model.add(keras.layers.MaxPooling2D())
            else:
                model.add(keras.layers.AvgPool2D())
        
        model.add(keras.layers.GlobalAvgPool2D())
        model.add(keras.layers.Dense(hp_model.Int('hidden_size', 30, 100, step=10, default=50), activation='relu',kernel_regularizer=tf.keras.regularizers.L1(l1=self.l1_value)))
        model.add(keras.layers.Dropout(hp_model.Float('dropout', 0, 0.5, step=0.1, default=0.5)))
        model.add(keras.layers.Dense(10, activation='softmax'))

        
        model.compile(optimizer=keras.optimizers.Adam(learning_rate=hp_model.Float('learning_rate', 1e-4, 1e-2, sampling='log')), 
                  loss='sparse_categorical_crossentropy', 
                  metrics=['accuracy'])

        print(model.summary())
        return model
