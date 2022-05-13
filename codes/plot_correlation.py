import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import AutoDateLocator, AutoDateFormatter
from rich.console import Console

console = Console()
mpl.rcParams.update({
    "figure.dpi": 250,
    "xtick.minor.visible": True,
    "xtick.direction": "in",
    "ytick.minor.visible": True,
    "figure.subplot.top": 0.955,
    "figure.subplot.bottom": 0.215,
    # "figure.subplot.left": 0.140,
    "figure.subplot.right": 0.98,
    "ytick.direction": "in",
})
mpl.rcdefaults()
console.log("Processing")
df = pd.read_csv("final1.csv", delimiter=",")
df = df.set_index("datetime", drop=True)
dissolved_oxygen = df["do"]

salinity = df["salinity"]
_df = pd.DataFrame([dissolved_oxygen, salinity]).transpose()
fig = plt.figure()
plt.imshow(_df.corr())
plt.colorbar()
fig.savefig("plots/do_vs_salinity.png")

temp = df["temperature"]
_df = pd.DataFrame([dissolved_oxygen, temp]).transpose()
fig = plt.figure()
plt.imshow(_df.corr())
plt.colorbar()
fig.savefig("plots/do_vs_temp.png")

conductance = df["conductance"]
_df = pd.DataFrame([dissolved_oxygen, conductance]).transpose()
fig = plt.figure()
plt.imshow(_df.corr())
plt.colorbar()
fig.savefig("plots/do_vs_conductance.png")

pH = df["pH"]
_df = pd.DataFrame([dissolved_oxygen, pH]).transpose()
fig = plt.figure()
plt.imshow(_df.corr())
plt.colorbar()
fig.savefig("plots/do_vs_pH.png")


plt.close()
