"""
To predict two image classification along with confidence level
Author: Pooja SAXENA
Datum : 02 Oktober 2021
Place : Hamburg
"""
import os
import sys
import numpy as np
from matplotlib.pyplot import imread
from keras.preprocessing import image
import matplotlib.pyplot as plt
from google.colab import files

path="/Users/psaxena/Documents/weitebildung/"

def predict_local_image_with_confidence_level(image_name, image_target_size, model_name, output_class,  show_image=True):
  """
  Output the prediction:
   image_name= name of the jpf file in ~/Doc/weiterbildung/images_for_testing
   image_target_size: size of the image eg:(150,150)
   model_name = name of the model to make the prediction 
   output_class = array of two image classifier eg ["dog", "cat"]
  """  
  image_path = path + '/images_for_testing/' + image_name
  if not os.path.exists(image_path):
    print(f"{image_path} does not exist, quiting!")
    return
    
  img=image.load_img(image_path, target_size=image_target_size)
  img_tensor=image.img_to_array(img)
  img_tensor=np.expand_dims(img_tensor, axis=0)
  img_tensor /= 255.

  if show_image:
      plt.imshow(img_tensor[0])
      plt.axis('off')
      plt.show()
  
  pred = model_name.predict(img_tensor, batch_size=20)
  pred_class = output_class[0] if pred[0]>0.5 else output_class[1]
  confidence = round((1-pred[0][0])*100 if pred_class=='cat' else pred[0][0]*100,3)
  prediction = {'class':pred_class, 'confidence_level':confidence}
  return prediction

help(predict_local_image_with_confidence_level)


def predict_colab():
  uploaded=files+
  for fn in uploaded.keys():

    # predicting images
    path='/content/' + fn
    img=image.load_img(path, target_size=(150, 150))
  
    x=image.img_to_array(img)
    x=np.expand_dims(x, axis=0)
    images = np.vstack([x])
  
    classes = model.predict(images, batch_size=10)
  
    print(classes[0])


  
