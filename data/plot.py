import numpy as np
import matplotlib.pyplot as plt
import netCDF4
from mpl_toolkits.basemap import Basemap

ds = netCDF4.Dataset("AQUA_MODIS.20180107.L3m.DAY.SST.sst.4km.nc")
lat = ds.variables["lat"]
lon = ds.variables["lon"]
sst = ds.variables["sst"]

mp = Basemap(projection="stere")

lon, lat = np.meshgrid(lon, lat)
x, y = mp(lat, lon)
color_scheme = mp.pcolor(x, y, np.squeeze(sst), cmap="jet")

mp.drawcounties()

plt.show()









