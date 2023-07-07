#!/bin/python

import os
import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", action="store", default=None, nargs='*', help="The csv files to read data.")
parser.add_argument("-o", "--output", action="store", default=None, help="The csv file of the merged data.")
args = parser.parse_args()

data = [pd.read_csv(file) for file in args.file]
update_data = dict.fromkeys(data[0].columns)
for label in update_data.keys():
    ud_list = []
    for d in data:
        ud_list.extend(list(d[label]))
    update_data[label] = ud_list

pd.DataFrame(update_data).to_csv(f'./{args.output}', index=False)
