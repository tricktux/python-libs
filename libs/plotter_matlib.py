from parse import Parser
import matplotlib.pyplot as plt
import csv
from sys import exit as sexit
from os.path import isfile


def set_parser():
    """docstring for set_parser"""
    parse = Parser()
    parse.add_description('Csv plotter')
    parse.parser.add_argument(
        '--csv', required=True, help='Path to the csv file')
    parse.parser.add_argument(
        '--x',
        required=True,
        type=int,
        default=0,
        help='Csv file column to use for x axis')
    parse.parser.add_argument(
            '--y',
            required=True,
            type=int,
            default=0,
            help='Csv file column to use for y axis')
    parse.parse()

    return parse


def main():
    parser = set_parser()
    file = parser.get_arg('csv', '')
    if not file:
        sexit('Failed to get csv file name')

    if not isfile(file):
        sexit('Failed to open csv file provided: "%s"' % file)

    x_col = parser.get_arg('x', -1)
    y_col = parser.get_arg('y', -1)

    if x_col < 0 or y_col < 0:
        sexit('Invalid values for x and y columns')

    with open(file) as csv_file:
        csv_read = csv.reader(csv_file, delimiter=',')
        x = []
        y = []

        next(csv_read, None)
        for row in csv_read:
            x.append(int(row[x_col]))
            y.append(int(row[y_col]))

    plt.plot(x, y, label='plot label')
    plt.xlabel('x label')
    plt.ylabel('y label')

    plt.title("plot title")

    plt.legend()

    plt.show()


if __name__ == '__main__':
    main()
