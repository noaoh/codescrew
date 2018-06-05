#!/usr/bin/env python3
import re
import argparse
from pprint import pprint as pp

screw_db = [{'unscrew' : r';', 'screw' : '\u037e'},\
    {'unscrew' : '!', 'screw' : 'ǃ'},\
    {'unscrew' : ',', 'screw' : '‚'},\
    {'unscrew' : '\'', 'screw' : 'ꞌ'},\
    {'unscrew' : ':', 'screw' : '∶'},\
    {'unscrew' : '*', 'screw' : '∗'}]

def screw(a_file):
    with 
    with open(a_file, "r+") as screw_file:
        screw_text = screw_file.read()
        for screw_entry in screw_db:
            screw_text = re.sub(screw_entry['unscrew'], screw_entry['screw'], screw_text)

        screw_file.seek(0)
        screw_file.write(screw_text)
        screw_file.truncate()

def unscrew(a_file):
    with open(a_file, "r+") as unscrew_file:
        unscrew_text = unscrew_file.read()
        for screw_entry in screw_db:
            unscrew_text = re.sub(screw_entry['screw'], screw_entry['unscrew'], unscrew_text)

        unscrew_file.seek(0)
        unscrew_file.write(unscrew_text)
        unscrew_file.truncate()

def main():
    parser = argparse.ArgumentParser(description="Mess up (or fix) someone's code using lookalike unicode characters.")
    parser.add_argument('-f', '--file', help="The target file(s)")
    parser.add_argument('-u', '--unscrew', action="store_true", help="Unscrews file(s) (default: screws file(s))")

    args = parser.parse_args()
    if args.unscrew:
      unscrew(args.file)

    screw(args.file)

if __name__ == "__main__":
    main()
