import os
import datetime
import subprocess
import numpy as np

API_KEY = "6a38abf402455bafad551e9c8063a6136e8438a2"
url = "https://oceandata.sci.gsfc.nasa.gov/ob/getfile/"

_down_range = np.array(list(range(19, 30)))

if len(_down_range) % 2 != 0:
    _down_range = np.insert(_down_range, 0, -1)
_down_range = _down_range.reshape(-1, 2)

for k in _down_range:
    print(k)
    for j in k:
        if j == -1:
            continue
        else:
            _date = datetime.datetime(year=2018, month=1, day=j)
            date = _date.strftime("%Y%m%d")
            sst_aqua_pattern = f"AQUA_MODIS.{date}.L3m.DAY.SST.sst.4km.nc"
            print(sst_aqua_pattern)
            # p = os.popen(f"wget -O {sst_aqua_pattern} {url}{sst_aqua_pattern}?appkey={API_KEY}")
    print("\n")


# p.wait()