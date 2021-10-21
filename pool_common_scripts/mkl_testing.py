import tensorflow as tf
major_version = int(tf.__version__.split(".")[0])
if major_version >= 2:
    from tensorflow.python import _pywrap_util_port
    print("MKL enabled:", _pywrap_util_port.IsMklEnabled())
else:
    print("MKL enabled:", tf.pywrap_tensorflow.IsMklEnabled()) 
