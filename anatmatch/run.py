"""
Command line interface for anatmatch
"""

from argparse import ArgumentParser


def get_parser():
    """
    """

    parser = ArgumentParser(description='anatmach: a T1w image matcher')
    parser.add_argument('datasets', action='store', nargs='+',
                        help='Input datasets to check for shared subjects.')

    return parser


def main(argv=None):
    raise NotImplementedError('We haven\'t gotten here, yet! Try again later.')


if __name__ == '__main__':
    raise RuntimeError('anatmatch/run.py should not be run directly;\n'
                       'Please `pip install anatmach` and use the `anatmatch` '
                       'command')
