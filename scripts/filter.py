#!/bin/python

import os
import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", action="store", default=None, help="The name of the csv file to be filtered.")
parser.add_argument("-g", "--gender", action="store", default=None, help="Pick out people depends on their gender, \"male\" or \"female\".")
parser.add_argument("-d", "--directory", action="store", default=None, help="The name of the directory to store filtered data.")
args = parser.parse_args()

file, gender, directory = args.file, args.gender, args.directory

data = pd.read_csv(file)
if not os.path.exists(directory):
    os.system(f'mkdir {directory}')

fid = file.split('/')[-1].split('_')[-1].split('.')[0]
if gender != None:
    filter_data = data[data['gender'] == gender]
    filter_data.to_csv(f'{gender}-data_{fid}.csv', index=False)
    os.system(f'mv ./{gender}-data_{fid}.csv {directory}')
