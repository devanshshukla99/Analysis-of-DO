# In[0]
import sys
import pandas as pd

folder = sys.argv[1]
files = "GLOBAL_DF_%s.csv"

global_df = pd.DataFrame()
for year in range(2018, 2021):
    filename = files % year
    df = pd.read_csv(folder + "/" + filename)
    global_df = pd.concat([global_df, df])

print(global_df)
global_df.to_csv("GLOBAL_merged.csv", index=False)


# In[1]

df_sst = pd.read_csv("GLOBAL_merged_sst.csv")
df_chl = pd.read_csv("GLOBAL_merged_chl.csv")

df = df_sst.merge(df_chl)
df = df[["datetime", "sst", "chlor_a"]]
df.to_csv("merged.csv", index=False)
