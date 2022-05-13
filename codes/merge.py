import pandas as pd
from rich.console import Console

console = Console()

basename = "orient_harbour_ny_%s.rdb"

data_parameters = ["do", "ph", "specific_conductance", "salinity"]  #, "nitrate"]
df = pd.read_csv(basename % "temperature", delimiter="\t", comment="#", low_memory=False)

df = df.drop(["agency_cd", "site_no", "tz_cd"], axis=1)
df = df.drop(0).reset_index(drop=True)

console.log("Processing")

for param in data_parameters:
    console.log(f"Loading {basename % param}")
    each_df = pd.read_csv(basename % param, delimiter="\t", comment="#", low_memory=False)
    each_df = each_df.drop(["agency_cd", "site_no", "tz_cd"], axis=1)
    each_df = each_df.drop(0).reset_index(drop=True)
    df = pd.merge(df, each_df, on="datetime", how="left")

console.log("Merged")

df.to_csv(basename % "merged", sep=",", index=False)
console.log(f"Exported to {basename % 'merged'}")
