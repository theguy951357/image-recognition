import datetime
import logging
import logging.config
import os
import sys
import tensorflow as tf

from pathlib import Path

from core.utils.log_formatter import LogFormatter
from core.manipulation import Manipulator


# Configure logger first thing -- it is possible imports rely on a configured logger before main() is run.
def setup_logger():
    formatter = LogFormatter()
    s = datetime.datetime.utcnow()
    path = Path('../logs')  # Lives one directory above /src.
    file = f'{path.absolute()}/object-rec_{s.year}-{s.month}-{s.day}-{s.hour}{s.minute}{s.second}.log'

    # Create log directory if it doesn't exist
    if not path.exists():
        path.mkdir()

    # Log to file...debug logs are always logged to a file
    logging.basicConfig(filename=file, format=formatter.log_fmt, level=logging.DEBUG)

    # Log to console as well...console logs are dependent on the --verbose flag.
    # Not great to hard-code the -v/--verbose flag, but because core.Config is set up after logging is initialized,
    # and because core.Config *relies* on a configured logger, we'll use this for now.
    c_level = logging.DEBUG if ('-v' in sys.argv[1:]) or ('--verbose' in sys.argv[1:]) else logging.INFO
    console = logging.StreamHandler()
    console.setLevel(c_level)
    console.setFormatter(LogFormatter())
    logging.getLogger('').addHandler(console)


setup_logger()
logger = logging.getLogger('main')  # Main is unique. All other files start with ...getLogger(__name__)
logger.debug('Logger initialized.')

from core import init_config

config = init_config()


def ls_tf_devices():
    """Displays all devices tensorflow has access to.
    If both 'CPU' and 'GPU' are listed in the output,
    that means tensorflow has access to GPU accelerated training."""

    logger.info("Checking TensorFlow for hardware access. (Do you see 'GPU'?)...")
    # Check for TensorFlow GPU access
    logger.info(f"TensorFlow has access to the following devices:\n{tf.config.list_physical_devices()}")

    # See TensorFlow version
    logger.info(f"TensorFlow version: {tf.__version__}")


def main():
    logger.info('Welcome to YAOR (Yet Another Object Recognizer)!')
    logger.info(f'Loaded with configuration: {config}')

    ls_tf_devices()

    logger.info('Installing ETA models')
    os.system('eta install models')

    logger.info('Begin image labeling.')
    manipulator = Manipulator(config)
    manipulator.export()


if __name__ == '__main__':
    main()
