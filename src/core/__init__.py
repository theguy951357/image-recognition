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
    desc = """Object Classifier, created by Harry Burnett, Chris Blaha, Jaydin Andrews, 
    and Matt Collins. The objective of this utility is to recognize everyday objects from 
    everyday scenes. Load a directory of images and the software will produce an output directory 
    with the same images with all recognized objects labeled."""

    parser = argparse.ArgumentParser(description=desc)

    parser.add_argument('-i', '--image_dir', help='Absolute or relative directory path of images to process for object recognition.',
                        metavar='DIR_PATH', required=False, default='./images/')
    parser.add_argument('-vi', '--video_dir', help='Absolute or relative directory path of videos to process for object recognition.',
                        metavar='DIR_PATH', required=False, default='./videos/')
    parser.add_argument('-o', '--out_dir', help='Folder location for output. Default is ./out/',
                        default='./out/', metavar='DIR', required=False)
    parser.add_argument('-v', '--verbose', help='Verbose logging.', action='store_true', required=False, default=False)

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
