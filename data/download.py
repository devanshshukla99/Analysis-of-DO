import os

API_KEY = "6a38abf402455bafad551e9c8063a6136e8438a2"
url = "https://oceandata.sci.gsfc.nasa.gov/ob/getfile/"

for i in range(7, 8):
    date = f"2018010{i}"
    sst_aqua_pattern = f"AQUA_MODIS.{date}.L3m.DAY.SST.sst.4km.nc"

    print(sst_aqua_pattern)

    os.system(f"wget -O {sst_aqua_pattern} {url}{sst_aqua_pattern}?appkey={API_KEY}")