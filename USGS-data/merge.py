import pandas as pd
from rich.console import Console

console = Console()

basename = "orient_harbour_ny_%s.rdb"

data_parameters = ["do", "ph", "specific_conductance"]  #, "nitrate"]
df = pd.read_csv(basename % "temperature", delimiter="\t", comment="#", low_memory=False)

console.log("Processing")

for param in data_parameters:
    console.log(f"Loading {basename % param}")
    each_df = pd.read_csv(basename % param, delimiter="\t", comment="#", low_memory=False)
    df = pd.merge(df, each_df, on="datetime", how="left")

console.log("Merged")
export_df = df.drop(0).reset_index(drop=True)

export_df.to_csv(basename % "merged", sep=",", index=False)
console.log(f"Exported to {basename % 'merged'}")
