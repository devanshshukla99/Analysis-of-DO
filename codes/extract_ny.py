import pandas as pd
import nctoolkit as nc
import matplotlib as mpl
from datetime import datetime
import matplotlib.pyplot as plt
from rich.console import Console

console = Console()

# monitoring_station_latlong = (41.13663889, -72.30675)
# Calculation of subset
monitoring_station_lat = [40, 41.250]
monitoring_station_lon = [-73, -71]


for year in range(2018, 2019):
    global_df = pd.DataFrame()
    try:
        for month in range(1, 13):
            date = datetime(year=year, month=month, day=1).strftime("%Y%m")
            for i in range(0, 4):
                filenames = f"AQUA_MODIS.{date}{i}*.nc"
                console.log(filenames)
                ds = nc.open_data(filenames)
                # console.log(f"sellonlatbox,{monitoring_station_lon[0]},{monitoring_station_lon[1]},{monitoring_station_lat[0]},{monitoring_station_lat[1]} selname,sst")
                ds.cdo_command(f"sellonlatbox,{monitoring_station_lon[0]},{monitoring_station_lon[1]},{monitoring_station_lat[0]},{monitoring_station_lat[1]} selname,sst")
                ds.spatial_mean()
                ds.run()
                ds.merge()
                df = ds.to_dataframe()
                global_df = pd.concat([global_df, df])
                console.log(f"Appended to global_df {year}")
                # df.to_csv(filenames + ".csv", index=False)
                # console.log(f"dumped to {filenames + '.csv'}")
    finally:
        global_df.to_csv(f"GLOBAL_DF_{year}.csv", index=False)