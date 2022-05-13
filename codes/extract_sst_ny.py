import pandas as pd
import nctoolkit as nc
import matplotlib as mpl
from datetime import datetime
from datetime import timedelta
import matplotlib.pyplot as plt
from rich.console import Console

console = Console()

# monitoring_station_latlong = (41.13663889, -72.30675)
# Calculation of subset
monitoring_station_lat = [40, 41.250]
monitoring_station_lon = [-73, -71]

for year in range(2020, 2021):
    global_df = pd.DataFrame()
    month = 1
    day = 1
    basedate = datetime(year=year, month=month, day=day)
    try:
        for i in range(1, 366):
            date = basedate + timedelta(i - 1)
            filenames = f"AQUA_MODIS.{date.strftime('%Y%m%d')}.L3m.DAY.SST.sst.4km.nc"
            console.log(filenames)
            ds = nc.open_data(filenames)
            # console.log(f"sellonlatbox,{monitoring_station_lon[0]},{monitoring_station_lon[1]},{monitoring_station_lat[0]},{monitoring_station_lat[1]} selname,sst")
            ds.cdo_command(f"sellonlatbox,{monitoring_station_lon[0]},{monitoring_station_lon[1]},{monitoring_station_lat[0]},{monitoring_station_lat[1]} selname,sst")
            ds.spatial_mean()
            ds.run()
            # ds.merge()
            df = ds.to_dataframe()
            df["datetime"] = pd.to_datetime(date)
            global_df = pd.concat([global_df, df])
            # console.log(f"Appended to global_df {year}")
            # df.to_csv(filenames + ".csv", index=False)
            # console.log(f"dumped to {filenames + '.csv'}")
    finally:
        global_df.to_csv(f"GLOBAL_DF_{year}.csv", index=False)
