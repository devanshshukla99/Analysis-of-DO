import os
import datetime
import subprocess

API_KEY = "6a38abf402455bafad551e9c8063a6136e8438a2"
url = "https://oceandata.sci.gsfc.nasa.gov/ob/getfile/"

for i in range(10, 15):
    _date = datetime.datetime(year=2018, month=1, day=i)
    date = _date.strftime("%Y%m%d")
    sst_aqua_pattern = f"AQUA_MODIS.{date}.L3m.DAY.SST.sst.4km.nc"
    print(sst_aqua_pattern)

    p = os.popen(f"wget -O {sst_aqua_pattern} {url}{sst_aqua_pattern}?appkey={API_KEY}")

p.wait()