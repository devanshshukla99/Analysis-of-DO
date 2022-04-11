import netCDF4
import pathlib
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

path = pathlib.Path(".")
files = path.glob("*.nc")

for file in files:
    print(file)
    if file.suffix != ".nc":
        continue
    else:
        ds = netCDF4.Dataset(file)
        lat = ds.variables["lat"]
        lon = ds.variables["lon"]
        sst = ds.variables["sst"]

        fig = plt.figure()
        mp = Basemap()
        lon, lat = np.meshgrid(lon, lat)
        x, y = mp(lon, lat)
        mp.contourf(x, y, sst[:, :], cmap="jet")

        mp.drawcoastlines()
        mp.colorbar()
        plt.title(file.name)
        fig.savefig(file.name + ".pdf")
        plt.close()
        # plt.show()


