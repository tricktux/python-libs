import argparse


class Parser():
    """Wrapper around argparse."""

    def __init__(self):
        """Initialize with options."""
        self.parser = argparse.ArgumentParser()
        self.args = {}

    def add_description(self, description):
        """Add a description"""
        #  Since class is a singleton not added to ctor. Could be complex
        self.parser.description = description

    def parse(self):
        """After arguments have been added go ahead and parse."""
        #  Convert the result of the function into a dict instead of a namespace
        self.args = vars(self.parser.parse_args())

    def get_arg(self, name, default_val):
        """Get value for argument passed to program."""
        if name not in self.args:
            return default_val
        return self.args[name]


#  Sample use!
if __name__ == '__main__':
    parse = Parser()
    parse.add_description('Sample Parser')
    parse.parser.add_argument(
        '--config',
        '-c',
        default='config.ini',
        help='Path to the configuration file')
    parse.parser.add_argument(
        '--debug', '-d', type=int, default=0, help='Create debug file')
    parse.parse()
    print(parse.get_arg('config', 'sandwish.ini'))
    print(parse.get_arg('debug', 2))
