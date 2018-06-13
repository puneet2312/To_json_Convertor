import json
import pandas as pd


df = pd.read_csv("input.csv")

data = []
keys=df.columns.values
for row_number in range(df.shape[0]):
    if row_number == 0:
        continue
    row_data = {}
    for col_number, cell in enumerate(df.ix[row_number]):
        row_data[keys[col_number]] = cell
    data.append(row_data)

with open("out.json", 'w') as json_file:
    json_file.write(json.dumps(data, indent=4, sort_keys=True))