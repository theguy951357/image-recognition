import numpy as np
from matplotlib import pyplot as plt
from PIL import Image


class Recognizer():

    def load_image_into_numpy_array(self, image):
        (image_width, image_height) = image.size
        return np.array(image.getdata()).reshape(
                (image_height, image_width, 3)).astype(np.uint8)

    def test_display_image(self):
        print("Testing image show from PLT")
        image = Image.open("../../tests/data/images/test_scene.jpeg")
        image_np = self.load_image_into_numpy_array(image)
        plt.imshow(image_np)
        plt.show()

    def __init__(self):
        self.test_display_image()


recognizer = Recognizer()
recognizer.__init__()
