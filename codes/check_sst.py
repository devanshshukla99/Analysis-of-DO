import pandas as pd
import nctoolkit as nc
import matplotlib as mpl
from datetime import datetime
from datetime import timedelta
import matplotlib.pyplot as plt
from rich.console import Console

console = Console()

for year in range(2018, 2020):
    month = 1
    day = 1
    basedate = datetime(year=year, month=month, day=day)
    for i in range(1, 366):
        date = basedate + timedelta(i - 1)
        filenames = f"AQUA_MODIS.{date.strftime('%Y%m%d')}*.nc"
        console.log(filenames)
        ds = nc.open_data(filenames)
        if not ds.variables:
            print(filenames)
