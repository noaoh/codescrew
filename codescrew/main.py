#!/usr/bin/env python3
import argparse
import fileinput
import sys
import logging
from logging.config import dictConfig

screw_db = [{'unscrew' : ';', 'screw' : '\u037e'},\
    {'unscrew' : '!', 'screw' : 'ǃ'},\
    {'unscrew' : ',', 'screw' : '‚'},\
    {'unscrew' : '\'', 'screw' : 'ꞌ'},\
    {'unscrew' : ':', 'screw' : '∶'},\
    {'unscrew' : '*', 'screw' : '∗'}]

logging_config = dict(
    version = 1,
    formatters = {
        'f': {'format':
              '%(levelname)-4s %(message)s'}
        },
    handlers = {
        'h': {'class': 'logging.StreamHandler',
              'formatter': 'f',
              'level': logging.DEBUG}
        },
    root = {
        'handlers': ['h'],
        'level': logging.DEBUG,
        },
)

dictConfig(logging_config)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def unicode_codepoint(string):
    return "".join([r"\u{0:X}".format(ord(s)) for s in string])

def screw(a_file):
    for line in fileinput.input(a_file, inplace=True):
        for screw_entry in screw_db:
            line = line.replace(screw_entry['unscrew'], screw_entry['screw'])

        sys.stdout.write(line)

def unscrew(a_file):
    for line in fileinput.input(a_file, inplace=True):
        for screw_entry in screw_db:
            line = line.replace(screw_entry['screw'], screw_entry['unscrew'])

        sys.stdout.write(line)

def main():
    parser = argparse.ArgumentParser(description="Mess up (or fix) someone's code using lookalike unicode characters.")
    parser.add_argument("file", help="The target file(s)")
    parser.add_argument('-u', '--unscrew', action="store_true", help="Unscrews file(s) (default: screws file(s))")

    args = parser.parse_args()
    if args.unscrew:
      unscrew(args.file)

    else:
        screw(args.file)

if __name__ == "__main__":
    main()
