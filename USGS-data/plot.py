import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from rich.console import Console

console = Console()
mpl.rcParams.update({
    "xtick.minor.visible": True,
    "xtick.direction": "in",
    "ytick.minor.visible": True,
    "ytick.direction": "in",
})

basename = "orient_harbour_ny_%s.rdb"
filename = basename % "merged"

console.log("Processing")

df = pd.read_csv(filename, delimiter=",")

columns = {
    "temperature": "106480_00010",
    "pH": "106486_00400",
    "do": "106484_00300",
    "conductance": "106481_00095",
    "nitrate": "106491_99137"
}

columns = {
    "106480_00010": "temperature",
    "106486_00400": "pH",
    "106484_00300": "do",
    "106481_00095": "conductance",
    "106491_99137": "nitrate"
}

console.print("temp")
console.print(df[columns.get("temperature")])
console.print(df["datetime"])

# fig = plt.figure()
# ax = plt.gca()
# ax.grid(True)
# ax.tick_params("both", which="minor")
# # ax.plot(df[columns.get("temperature")], label=r"temperature $^\circ C$")
# ax.plot("datetime", columns.get("temperature"), data=df, label=r"temperature $^\circ C$")
# ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%b'))

df.plot("datetime", columns.get("temperature"), label="", xlabel="Time", ylabel=r"Temperature [$^\circ C$]")
ax = plt.gca()
ax.grid(True)
ax.get_legend().remove()
plt.gcf().autofmt_xdate()
# ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%b'))
plt.show()
