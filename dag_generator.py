#!/bin/python

import os
import glob
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--name", action="store", default=None, help="The name of the dag file.")
parser.add_argument("-f", "--filter", action="store", default=None, nargs='*', help="The csv files to be filterd.")
parser.add_argument("-g", "--gender", action="store", default=None, help="Picking out people depends on their gender, \"male\" or \"female\".")
parser.add_argument("-o", "--output", action="store", default=None, help="The csv file of the merged data.")
args = parser.parse_args()

if os.path.exists(args.name):
    os.system(f'rm -rf {args.name}')

if args.filter != None:
    org_data = args.filter
elif os.path.exists('./org_data'):
    org_data = glob.glob('./org_data/*')
    org_data.sort()

org_data_all = str()
for i in org_data:
    org_data_all += i+' '

f_jobs = [f'filter_{id}' for id in range(len(org_data))]
f_jobs_all = str()
for i in f_jobs:
    f_jobs_all += i+' '

gender = args.gender

f_data = [f"./filtered_data/{gender}-{file.split('/')[-1]}" for file in org_data]
f_data_all = str()
for i in f_data:
    f_data_all += i+' '

with open(args.name, 'x') as f:
    for job, file in zip(f_jobs, org_data):
        dagtext = '''JOB {} filter.sub
RETRY {} 0
VARS {} org_data="{}" gender="{}"\n
'''.format(job, job, job, file, gender)
        f.writelines(dagtext)

    dagtext = '''JOB merge merge.sub
RETRY merge 0
VARS merge filtered_data="{}" merge_output="{}"\n
PARENT {} CHILD merge
'''.format(f_data_all[:-1], args.output, f_jobs_all[:-1])
    f.writelines(dagtext)
