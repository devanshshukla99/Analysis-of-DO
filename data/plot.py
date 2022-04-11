import numpy as np
import matplotlib.pyplot as plt
import netCDF4
from mpl_toolkits.basemap import Basemap

ds = netCDF4.Dataset("AQUA_MODIS.20180104.L3m.DAY.SST.sst.4km.nc")
lat = ds.variables["lat"]
lon = ds.variables["lon"]
sst = ds.variables["sst"]

mp = Basemap()
lon, lat = np.meshgrid(lon, lat)
x, y = mp(lon, lat)
mp.contourf(x, y, sst[:, :], cmap="jet")
# mp.drawcountries()
mp.drawcoastlines()
mp.colorbar()
# color_scheme = mp.pcolor(x, y, sst, cmap="jet", latlon=True)


plt.show()









