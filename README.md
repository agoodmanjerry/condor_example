# condor_example
This is an example to submit jobs through condor on LIGO's CIT cluster. There are 3 csv files in the folder "org_data" with the ids, names and genders of people. This example shows how to filter the people by their gender (male or female) and then merge their information in one merged csv file called "merged data".
The dag file includes two jobs: filtering and merging. the dag files are generated by the "dag_generator.py": 
```bash
  python dag_generator --name female.dag --gender female --output all_female.csv
```

People can either send the dag by
```
  condor_submit_dag female.dag
```
or use the "filter.sub" or "merge.sub" in the "scripts" folder directly by
```
  condor_submit filter.sub
```
