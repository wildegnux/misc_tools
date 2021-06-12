#!/usr/bin/env python3

import lorem
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('function',
    help='which lorem function to run',
    choices=['sentence', 'paragraph'])
parser.add_argument('count',
    help='how many',
    type=int)
parser.add_argument('-n',
    help='no newline',
    action='store_true')
args = parser.parse_args()

kwargs = {}
if args.n:
    kwargs['end'] = ''

for i in range(0, args.count):
    if args.function == 'sentence':
        print(lorem.sentence(), **kwargs)
    elif args.function == 'paragraph':
        print(lorem.paragraph(), **kwargs)
