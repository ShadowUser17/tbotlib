#!/usr/bin/env python3
from argparse import ArgumentParser
from traceback import print_exc

from tbotlib import Telegram
from tbotlib import Message


try:
    import config

except ImportError:
    print_exc()


if __name__ == '__main__':
    pass
