
import logging
import logging.config
import datetime

from pathlib import Path

from core.utils.logformatter import LogFormatter


# Configure logger first thing -- it is possible imports rely on a configured logger before main() is run.
def setup_logger():
    formatter = LogFormatter()
    s = datetime.datetime.utcnow()
    path = Path('./logs')
    file = f'{path.absolute()}/object-rec_{s.year}-{s.month}-{s.day}-{s.hour}{s.minute}{s.second}.log'

    # Create log directory if it doesn't exist
    if not path.exists():
        path.mkdir()

    # Log to file...
    logging.basicConfig(filename=file, format=formatter.log_fmt, level=logging.DEBUG)

    # Log to console as well...
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(LogFormatter())
    logging.getLogger('').addHandler(console)


setup_logger()
logger = logging.getLogger('main')  # Main is unique. All other files start with ...getLogger(__name__)
logger.debug('Logger initialized.')


def main():
    logger.info('Welcome to Object Recognizer!')


if __name__ == '__main__':
    main()