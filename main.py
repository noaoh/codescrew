import re
import argparse

screw_dict = [{'unscrew' : r';', 'screw' : r';'},\
    {'unscrew' : r'!', 'screw' : r'ǃ'},\
    {'unscrew' : r',', 'screw' : r'‚'},\
    {'unscrew' : r'\'', 'screw' : r'\ꞌ'},\
    {'unscrew' : r'\:', 'screw' : r'\∶'}]

def screw(a_file):
    with open(a_file, "r+") as screw_file:
        screw_text = screw_file.read()
        for screw_entry in screw_dict:
            screw_text = re.sub(screw_entry['unscrew'], screw_entry['screw'], screw_text)

    screw_file.seek(0)
    screw_file.write(screw_text)
    screw_file.truncate()

def unscrew(a_file):
    with open(a_file, "r+") as unscrew_file:
        unscrew_text = unscrew_file.read()
        for screw_entry in screw_dict:
            unscrew_text = re.sub(screw_entry['screw'], screw_entry['unscrew'], unscrew_text)

    unscrew_file.seek(0)
    unscrew_file.write(unscrew_text)
    unscrew_file.truncate()

def main():
    parser = argparse.ArgumentParser(description="Mess up (or fix) someone's code using lookalike unicode characters.")
    parser.add_argument('-f', '--file', description="The target file(s)")
    parser.add_argument('-u', '--unscrew', description="Unscrews files (optional, screws files by default)")

    args = parser.parse_args()
    if args.unscrew:
      unscrew(args.f)

    screw(args.f)

if __name__ == "main":
    main()
