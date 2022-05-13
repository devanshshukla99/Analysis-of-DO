import pandas as pd
from datetime import timedelta
from rich.console import Console

console = Console()

df_ny = pd.read_csv("orient_harbour_ny_merged.rdb")
df_aq = pd.read_csv("aq_merged.csv")

console.log("Processing")

for i in range(0, 1095):
    df_aq["datetime"][i] = (pd.to_datetime(df_aq["datetime"][i]) + timedelta(0.5)).strftime("%Y-%m-%d %H:%M")

df_aqn = df_aq.set_index("datetime")
df_nyn = df_ny.set_index("datetime")


df = pd.merge(df_nyn, df_aqn, on="datetime", how="left")

columns = {
    "106480_00010": "temperature",
    "106486_00400": "pH",
    "106484_00300": "do",
    "106481_00095": "conductance",
    "106483_90860": "salinity",
    # "106491_99137": "nitrate"
}

df.rename(columns, axis=1, inplace=True)
export_df = df.drop(["106480_00010_cd", "106484_00300_cd", "106486_00400_cd", "106481_00095_cd", "106483_90860_cd"], axis=1)
export_df = export_df[["salinity", "temperature", "sst", "chlor_a", "conductance", "pH", "do"]]
export_df.to_csv("final1.csv", index=True)
