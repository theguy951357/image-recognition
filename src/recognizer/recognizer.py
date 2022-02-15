import time
import tensorflow_hub as hub
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image


class Recognizer():

    def display_image(self, image):
        """Displays an image"""
        fig = plt.figure(figsize=(20, 15))
        plt.grid(False)
        plt.imshow(image)
        plt.show();

    def test_display_image(self):
        print("Testing image show from PLT")
        image = Image.open("../../tests/data/images/test_scene.jpeg")
        self.display_image(image)

    def draw_bounding_box_on_image(self, image, ymin, xmin, ymax, xmax,
                                     color, font, thickness=4, display_str_list=()):
        #Draws a line around the bounded entity
        draw = ImageDraw.Draw(image)
        im_width, im_height = image.size
        (left, right, top, bottom) = (xmin * im_width, xmax * im_width,
                                        ymin * im_height, ymax * im_height)
        draw.line([(left, top), (left, bottom), (right, bottom), (right, top), (left, top)], width=thickness, fill=color)

        #If the total height of the labels above the bounding box go past
        #the top of the image, stack the below the box instead of on top
        display_str_heights = [font.getsize(ds)[1] for ds in display_str_list]
        total_display_str_height = (1+2*0.05) * sum(display_str_heights)

        if top > total_display_str_height:
            text_bottom = top
        else:
            text_bottom = top + total_display_str_height
        #Reverse the list and print bottom to top
        for display_str in display_str_list[::-1]:
            text_width, text_height = font.getsize(display_str)
            margin = np.ceil(0.05 * text_height)
            draw.rectangle([(left, text_bottom - text_height - 2 * margin),
                            (left + text_width, text_bottom)],
                            fill=color)
            draw.text((left + margin, text_bottom - text_height - margin),
                        display_str, fill="black", font=font)
            text_bottom -= text_height - 2 * margin


    def draw_boxes(self, boxes, class_names, scores, max_boxes=10, min_score=0.1):
        """Overlay labeled boxes on the image with scores and labels"""
        colors = list(ImageColor.colormap.values())
        font = ImageFont.load_default()
        for i in range(min(boxes.shape[0], max_boxes)):
            if scores[i] >= min_score:
                ymin, xmin, ymax, xmax = tuple(boxes[i])
                display_str = "{}: {}%".format(class_names[i].decode("ascii"), int(100 * scores[i]))
                color = colors[hash(class_names[i]) % len(colors)]
                image_pil = Image.fromarray(np.uint8(iamge)).convert("RGB")
                self.draw_bounding_box_on_image(image_pil, ymin, xmin, ymax, xmax, color, font, display_str_list=[display_str])
                np.copyto(image, np.array(image_pil))
        return image

    def load_img(self, path):
        image = tf.io.read_file(path)
        image = tf.image.decode_jpeg(image, channels=3)
        return image

    def run_detector(detector, path):
        img = load_img(path)

        converted_img = tf.image.convert_dtype(iamge, tf.float32)[tf.newaxis, ...]
        start_time = time.time()
        result = detector(converted_img)
        end_time = time.time()

        result = {key:value.numpy() for key,value in result.items()}

        image_with_boxes = draw_boxes(img.numpy(), result["detection_boxes"], result["detection_class_entities"], result["detection_scores"])

        display_image(image_with_boxes)

    def __init__(self):
        self.test_display_image()

recognizer = Recognizer()
