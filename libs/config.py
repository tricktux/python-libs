import configparser
import sys
from pathlib import Path


class ConfigParser():
    """Wrapper around configparse."""

    def __init__(self, file):
        """Initialize with options."""
        new_file = Path(file)
        if not new_file.is_file():
            print('Failed to open file: "{}"', new_file)
            sys.exit(1)

        self.config = configparser.ConfigParser()
        self.config.read(new_file)

    def get_opt(self, section, name, default_val):
        """Get value from config file."""
        return self.config.get(section, name, fallback=default_val)


#  Sample use!
if __name__ == '__main__':
    config = ConfigParser('some_file.ini')
    config.get_opt('monster', 'awesome', 8)
