"""
Config module for uplaoding the parameters in Flask application 
Author : Pooja SAXENA
EMail  : nrjrasaxena@gmail.com
Date   : 04 Oktober 2021
Place  : Hamburg
ref    : https://medium.com/@jbirdvegas/python-sometimes-you-need-configs-based-on-a-env-variable-177a5a2cc0ea
"""
import os

class Config(object):
    LOSS_FUNCTION  = "categorical_crossentropy"
    OPTIMIZER      = "adam"
    HOST_NAME      = "localhost"
    PORT_NUMBER    = 8000
    DEBUG_STATE    = "True"
    CLASSES_NAME   = ['dog','cat']
    MAIL_USERNAME  = os.environ.get('MAIL_USERNAME')
    IMAGE_SIZE     = 200
    MODEL_JSON     = "model_dogcat_classifier_cnn_85acc_okt21.json"
    MODEL_H5       = "model_dogcat_classifier_cnn_85acc_okt21.h5"
class AugmentationConfig(Config):
    MODEL_JSON     = "model_dogcat_classifier_cnn_augmentation_90acc_okt21.json"
    MODEL_H5       = "model_dogcat_classifier_cnn_augmentation_90acc_okt21.h5"
class TransferLearningConfig(Config):
    MODEL_JSON     = "model_dogcat_classifier_vgg_tLearn_93acc_okt21.json"
    MODEL_H5       = "model_dogcat_classifier_vgg_tLearn_93acc_okt21.h5"
    IMAGE_SIZE     = 224

def config_getter(key) -> str:
    env = os.getenv('APPLICATION_MODE', None)
    if env is None:
        print("Environment variable 'ENV' not set, returning local configs.")
    elif env == 'augmentation':
        return AugmentationConfig.__dict__.get(key)
    elif env == 'transferlearning':
        return TransferLearningConfig.__dict__.get(key)
    else:
        return Config.__dict__.get(key)

#if __name__ == '__main__':
def get_config():
    print("inside get_config function",os.environ['APPLICATION_MODE'])
#    model = config_getter('MODEL_H5')
#    print("model: ", model)
#    assert model == "model_dogcat_classifier_cnn_85acc_okt21.json" ##, 'Expected: model, received: {}'.format(model)

    os.environ['APPLICATION_MODE'] = 'augmentation'
    model_aug = config_getter('MODEL_H5')
    assert model_aug == 'model_dogcat_classifier_cnn_augmentation_90acc_okt21.h5', 'Expected: model aug, received: {}'.format(dev)

    os.environ['APPLICATION_MODE'] = 'transferlearning'
    model_tl = config_getter('MODEL_H5')
    assert model_tl == 'model_dogcat_classifier_vgg_tLearn_93acc_okt21.h5', 'Expected: model tl, received: {}'.format(qa)

    print(f"Success augmentation: {model_aug}, transferlearning: {model_tl}")
