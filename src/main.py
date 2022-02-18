import datetime
import logging
import logging.config
import sys

from pathlib import Path

from core.utils.log_formatter import LogFormatter


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


def main():
    logger.info('Welcome to YAOR (Yet Another Object Recognizer)!')
    logger.info(f'Loaded with configuration: {config}')


if __name__ == '__main__':
    main()
