import numpy as np
import matplotlib.pyplot as plt
import netCDF4
from mpl_toolkits.basemap import Basemap
from matplotlib.animation import FuncAnimation

ds = [
    netCDF4.Dataset("AQUA_MODIS.20180103.L3m.DAY.SST.sst.4km.nc"),
    netCDF4.Dataset("AQUA_MODIS.20180104.L3m.DAY.SST.sst.4km.nc"),
    netCDF4.Dataset("AQUA_MODIS.20180105.L3m.DAY.SST.sst.4km.nc"),
    netCDF4.Dataset("AQUA_MODIS.20180106.L3m.DAY.SST.sst.4km.nc")]
lat = ds[0].variables["lat"]
lon = ds[0].variables["lon"]
# sst = ds.variables["sst"]

mp = Basemap()
lon, lat = np.meshgrid(lon, lat)
x, y = mp(lon, lat)

fig = plt.figure()
mp.drawcoastlines()
ax = plt.gca()
plt.xlabel(r'x')
plt.ylabel(r'y')

# animation function
def animate(i): 
    print(i)
    sst = ds[i].variables["sst"]
    cont = plt.contourf(x, y, sst[:, :])
    return cont  

anim = FuncAnimation(fig, animate)
plt.show()