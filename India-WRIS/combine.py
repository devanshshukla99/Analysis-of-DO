import pandas as pd
import pathlib

p = pathlib.Path(".")
files = p.glob("*")

d = pd.read_csv(next(files))
for file in files:
    print(file)
    df = pd.read_csv(file)
    d = pd.merge(d, df)

d.to_csv("output.csv")

def fix_do(file1, file2):
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)
    dt = pd.concat([df1, df2], axis=0, sort=True, ignore_index=True)
    d = dt.sort_values(by="DateTime", ignore_index=True)
    return d
