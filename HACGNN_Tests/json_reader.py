from asyncore import write
import pickle
import pandas as pd
import json
import os



with open('CodeDoc_Generation\HACGNN_Tests\comprehensive-data-exploration-with-python.json', 'r') as nb:
    notebook = json.load(nb) # read JSON file from path (this is a dict)
    df = pd.DataFrame(notebook['cells']) # parse JSON into Pandas Dataframe


print(type(notebook))
for n in notebook:
    print(n)
# for c in notebook['cells']:
    # print(c.keys())

print(len(notebook['cells']))
print(df)
    
# csv_dump = pd.read_json('CodeDoc_Generation\HACGNN_Tests\dump.json')

