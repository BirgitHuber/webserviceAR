import theano
theano.config.optimizer = "None"

from answer.nnutils.resnet50 import ResNet50
from keras.preprocessing import image
from answer.nnutils.imagenet_utils import preprocess_input, decode_predictions
import numpy
import os


def decode_image(filename):
    model = ResNet50(weights='imagenet')

    # load the image
    img = image.load_img(filename, target_size=(224, 224))

    # set the image
    x = image.img_to_array(img)
    x = numpy.expand_dims(x, axis=0)
    x = preprocess_input(x)

    # make prediction
    preds = model.predict(x)
    print('Predicted:', decode_predictions(preds))

    # remove the image
    os.remove(filename)
    # return the result
    return decode_predictions(preds)
