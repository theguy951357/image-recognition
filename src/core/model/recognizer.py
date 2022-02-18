import time
import logging
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image, ImageDraw, ImageColor, ImageFont

logger = logging.getLogger(__name__)


def draw_bounding_box_on_image(image, y_min, x_min, y_max, x_max, color, font, thickness=4, display_str_list=()):
    # Draws a line around the bounded entity
    draw = ImageDraw.Draw(image)
    im_width, im_height = image.size
    (left, right, top, bottom) = (x_min * im_width, x_max * im_width,
                                  y_min * im_height, y_max * im_height)
    draw.line([(left, top), (left, bottom), (right, bottom), (right, top), (left, top)], width=thickness, fill=color)

    # If the total height of the labels above the bounding box go past
    # the top of the image, stack the below the box instead of on top
    display_str_heights = [font.getsize(ds)[1] for ds in display_str_list]
    total_display_str_height = (1 + 2 * 0.05) * sum(display_str_heights)

    if top > total_display_str_height:
        text_bottom = top
    else:
        text_bottom = top + total_display_str_height

    # Reverse the list and output bottom to top
    for display_str in display_str_list[::-1]:
        text_width, text_height = font.getsize(display_str)
        margin = np.ceil(0.05 * text_height)
        draw.rectangle([(left, text_bottom - text_height - 2 * margin),
                        (left + text_width, text_bottom)],
                       fill=color)
        draw.text((left + margin, text_bottom - text_height - margin),
                  display_str, fill="black", font=font)
        text_bottom -= text_height - 2 * margin


def display_image(image):
    """Displays an image"""
    # TODO: Fig is not used. Jay, please resolve such that the plot will display correctly.
    """the tutorial this came from had the same thing. I think the tutorial meant to put fig instead of plt on the rest of the method. hopefully changing it to fig will work"""
    fig = plt.figure(figsize=(20, 15))
    fig.grid(False)
    fig.imshow(image)
    fig.show()


# TODO: Move to testing suite
def test_display_image():
    logger.info('Displaying test image')
    image = Image.open("../../../tests/data/images/test_scene.jpeg")
    display_image(image)


def draw_boxes(image, boxes, class_names, scores, max_boxes=10, min_score=0.1):
    """Overlay labeled boxes on the image with scores and labels"""
    colors = list(ImageColor.colormap.values())
    font = ImageFont.load_default()
    for i in range(min(boxes.shape[0], max_boxes)):
        if scores[i] >= min_score:
            y_min, x_min, y_max, x_max = tuple(boxes[i])
            display_str = "{}: {}%".format(class_names[i].decode("ascii"), int(100 * scores[i]))
            color = colors[hash(class_names[i]) % len(colors)]
            image_pil = Image.fromarray(np.uint8(image)).convert("RGB")
            draw_bounding_box_on_image(image_pil, y_min, x_min, y_max, x_max, color, font, display_str_list=[display_str])

            # BUG: image_pil cannot be converted into anything that a numpy array takes as input.
            # TODO: Jay, please resolve.
            np.copyto(image, np.array(image_pil))
    return image


def load_img(path):
    image = tf.io.read_file(path)
    image = tf.image.decode_jpeg(image, channels=3)
    return image


def run_detector(detector, path):
    img = load_img(path)

    converted_img = tf.image.convert_dtype(img, tf.float32)[tf.newaxis, ...]
    start_time = time.time()
    result = detector(converted_img)
    end_time = time.time()

    result = {key: value.numpy() for key, value in result.items()}

    object_count = len(result["detection_scores"])
    logger.debug(f'Found {object_count} objects!')
    logger.debug(f'Inference time: {end_time - start_time}')

    image_with_boxes = draw_boxes(img.numpy(), result["detection_boxes"], result["detection_class_entities"],
                                  result["detection_scores"])

    display_image(image_with_boxes)
