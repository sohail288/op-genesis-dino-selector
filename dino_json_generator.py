#! /usr/bin/env python3
"""
    Takes in a file formatted like
    // SITE
    dino name "dinokey"
    ...
    dino name "dinokey"

    // SITE
    dino name "dinokey"
    ...
    dino name "dinokey"

    And outputs a json file that maps dino names to their key + site
    {
        ...
        "Apatosaurus": {
            "key":"apato",
            "site": "Morrison Formation B"
        },
        ...
    }
"""

import json
import os
import re
import sys

import logging

site_re = r'^//\s+([A-Z ]+)$'
dino_re = r'^(?P<dinoname>[A-Za-z ]+)\s+"(?P<dinokey>\w+)"'
output_filename = 'app/dinos.json'

def basic_reader(dino_file):
    dino_dict = {}
    with open(dino_file, 'r', encoding='utf8') as fh:
        lines = (line.strip() for line in fh)
        for line_no, line in enumerate(lines):
            if line == '':
                continue
            if line.startswith('//'):
                matches = re.match(site_re, line)
                if matches is None:
                    print(f"improper site line at {line_no + 1}: {line}")
                    sys.exit(1)
                site, = matches.groups(1)
            else:
                try:
                    dinoname, dinokey = re.match(dino_re, line).groups()
                except AttributeError:
                    print(f"improper dino name at {line_no + 1}: {line}")
                    sys.exit(1)
                else:
                    if '<' in line:
                        # some lines have variations?
                        _, variation = line.split('<')
                        dinoname = f"{dinoname}_{variation.strip()}"
                    dinokey = dinokey.lower()
                    if dinokey in dino_dict:
                        dino_dict[dinokey]['dig_sites'].append(site)
                    else:
                        logging.debug(f"site: {site}")
                        dino_dict[dinokey] = {
                            "dino_name": dinoname,
                            "dig_sites": [site],
                        }
    return dino_dict



def make_dino_json(dino_list_files, reader=None):
    if reader is None:
        print("needs a reader callback")
        sys.exit(1)

    dino_dict = {}

    for fname in dino_list_files:
        dino_dict.update(reader(fname))
    
    return json.dumps(dino_dict, indent=1)


def parse_args(args):
    cli_args = []
    files = []
    for arg in args:
        if arg.startswith('--'):
            cli_args.append(arg.lstrip('-'))
        else:
            files.append(arg)
    return cli_args, files

def parse_options(options):
    opts = {}
    for option in options:
        opts[option] = True
    return opts


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    cli_args, files = parse_args(sys.argv[1:])
    cli_opts = parse_options(cli_args)
    if len(files) < 1:
        print("Must specify dinolist file[s]")
        sys.exit(1)

    dino_json = make_dino_json(files, basic_reader)
    if not cli_opts.get('test'):
        with open(output_filename, 'w') as fh:
            fh.write(dino_json)
    else:
        print(dino_json)
    sys.exit(0)

