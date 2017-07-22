import argparse
import os
from dove import __version__

_DEFAULT_PATH = str(os.curdir)

def main():
    parser = argparse.ArgumentParser(description='A quickstart for Dove', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-p', '--path', default=_DEFAULT_PATH,
                        help='The path to generate the blog into')
    parser.add_argument('-t', '--title', metavar='title', help='Set the title of the website')
    parser.add_argument('-a', '--author', metavar='author', help='Set the author name os the website')
    parser.add_argument('-l', '--lang', metavar='lang', help='Set the default website language')

    args = parser.parse_args()

    print('''Welcome to dove-quickstart v{v}.
    This script will help you create a new Dove-based website.

    Please answer the following questions so this script can generate the files
    needed by Dove.
    '''.format(v=__version__))

if __name__ == '__main__':
    main()
