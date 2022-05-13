import pandas as pd
from datetime import timedelta
from rich.console import Console

console = Console()

df_ny = pd.read_csv("orient_harbour_ny_merged.rdb")
df_aq = pd.read_csv("merged.csv")

console.log("Processing")

for i in range(0, 1095):
    df_aq["datetime"][i] = (pd.to_datetime(df_aq["datetime"][i]) + timedelta(0.5)).strftime("%Y-%m-%d %H:%M")

df_aqn = df_aq.set_index("datetime")
df_nyn = df_ny.set_index("datetime")


df = pd.merge(df_nyn, df_aqn, on="datetime", how="left")



for param in data_parameters:
    console.log(f"Loading {basename % param}")
    _df = pd.read_csv(basename % param, delimiter="\t", comment="#", low_memory=False)
    df = df.merge(_df)

console.log("Merged")
export_df = df.drop(0).reset_index(drop=True)

export_df.to_csv(basename % "merged", sep=",", index=False)
console.log(f"Exported to {basename % 'merged'}")
