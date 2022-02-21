import argparse
import logging
import sys
from .utils.invalid_config_error import InvalidConfigError

from datetime import datetime
from pathlib import Path

from .config import Config

logger = logging.getLogger(__name__)


def parse_args(args):
    """Takes a set of arguments from the CLI and parses them."""
    if args is None or not isinstance(args, list) or len(args) == 0:
        raise InvalidConfigError('Expected program arguments, received None or invalid configuration.')

    desc = """Object Classifier, created by Harry Burnett, Chris Blaha, Jaydin Andrews, 
    and Matt Collins. The objective of this utility is to recognize everyday objects from 
    everyday scenes. Load an image of a scene and the software will produce an image 
    of the same scene with all recognized objects labeled."""

    parser = argparse.ArgumentParser(description=desc)

    parser.add_argument('-i', '--image', help='Absolute or relative file path of image to process for object '
                                              'recognition.', metavar='PATH', required=False)
    parser.add_argument('-m', '--model', help='File location of the model to use for object classification. If omitted,'
                                              ' will use ./models/default.pb -- Application will not run if this file '
                                              'or directory is missing. Used with -i.', default='./models/default.pb',
                        metavar='PATH', required=False)
    parser.add_argument('-n', '--name', help='Name of the output image file. Default is output-[current time]. Default '
                                             'output for model mode is model-[current time]. Used with -o and -i. Do '
                                             'not specify a file-type at the end of the name as it will be ignored.',
                        required=False)
    parser.add_argument('-o', '--out', help='Folder location for output. Used with -i. Default is ./out/ for '
                                            'classification mode and ./models/ for training mode.', default='./out/',
                        metavar='DIR', required=False)
    parser.add_argument('-t', '--train', '--train_dir', help='Path to image folder to train the model from. '
                                                             'This also sets the application into a training '
                                                             'configuration.', metavar='IMAGE_DIRECTORY_PATH',
                        required=False)
    parser.add_argument('-e', '--epochs', help='Number of Tensorflow epochs to use in the training. Default is 0.',
                        metavar='N', type=int, default=0, choices=[x for x in range(1, 100)], required=False)
    parser.add_argument('-v', '--verbose', help='Verbose logging.', action='store_true', required=False)

    return parser.parse_args(args)


def default_name(out_path, is_image_mode):
    """
    Gets the value of name from the given out_path, based on what is promised in the help
    message for the --name argument.

    :param out_path: The output path, default ./out/
    :param is_image_mode: Whether the configuration is in image mode.
    :return: Name for the file.
    """
    path = Path(out_path)
    if not path.exists():
        logger.debug(f'Path {path.absolute()} does not exist. Creating...')
        path.mkdir()

    base = 'output-' if is_image_mode else 'model-'
    time = datetime.utcnow()
    fmt = f'{time.month}-{time.day}-{time.year}-{time.hour}{time.minute}{time.second}'
    base += fmt
    return base


def init_config(args=None):
    """Generates a config from all user-defined CLI arguments."""
    if args is None:
        args = sys.argv[1:]

    parsed = parse_args(args)
    return Config.from_parsed_args(parsed)

