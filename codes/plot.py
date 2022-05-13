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
console.log("Processing")
df = pd.read_csv("final1.csv", delimiter=",")

df = df.set_index("datetime", drop=True)
sst = df["sst"]
temp = df["temperature"].loc[:"2020-12-29 12:00"]

_df = pd.DataFrame([temp, sst]).transpose()
fig = plt.figure()
ax = fig.gca()
_df.plot(ax=ax, marker="o", y="temperature", label="in-situ", xlabel="", ylabel=r"Temperature [$^\circ C$]")
_df.plot(ax=ax, marker="x", y="sst", label="remote", xlabel="", ylabel=r"Temperature [$^\circ C$]")
ax.grid(True)
plt.xticks(rotation=90, fontweight='light',  fontsize='x-small',)# fig.autofmt_xdate()
fig.savefig("plots/temp_vs_sst.png")

mpl.rcdefaults()
fig = plt.figure()
plt.imshow(_df.corr())
plt.colorbar()
fig.savefig("plots/temp_vs_sst_corr.png")


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

fig = plt.figure()
ax = fig.gca()
df.plot(ax=ax, y="temperature", label="", xlabel="", ylabel=r"Temperature [$^\circ C$]")
ax.grid(True)
ax.get_legend().remove()
plt.xticks(rotation=90, fontweight='light',  fontsize='x-small',)# fig.autofmt_xdate()
fig.savefig("plots/temperature.png")

fig = plt.figure()
ax = fig.gca()
df.plot(ax=ax, y="salinity", label="", xlabel="", ylabel=r"Salinity [psu]")
ax.grid(True)
ax.get_legend().remove()
plt.xticks(rotation=90, fontweight='light',  fontsize='x-small',)# fig.autofmt_xdate()
fig.savefig("plots/salinity.png")

fig = plt.figure()
ax = fig.gca()
df.plot(ax=ax, y="pH", label="", xlabel="", ylabel=r"pH")
ax.grid(True)
ax.get_legend().remove()
plt.xticks(rotation=90, fontweight='light',  fontsize='x-small',)# fig.autofmt_xdate()
fig.savefig("plots/pH.png")


fig = plt.figure()
ax = fig.gca()
df.plot(ax=ax, y="conductance", label="", xlabel="", ylabel=r"Specific conductance $[\mu S cm^{-1} at 25^\circ C]$")
ax.grid(True)
ax.get_legend().remove()
plt.xticks(rotation=90, fontweight='light',  fontsize='x-small',)# fig.autofmt_xdate()
# plt.show(block=False)
fig.savefig("plots/conductance.png")


fig = plt.figure()
ax = fig.gca()
df.plot(ax=ax, y="do", label="", xlabel="", ylabel=r"Dissolved oxygen$[mg/liter]$")
ax.grid(True)
ax.get_legend().remove()
plt.xticks(rotation=90, fontweight='light',  fontsize='x-small',)# fig.autofmt_xdate()
# plt.show(block=False)
fig.savefig("plots/do.png")


sst_df = df["sst"].dropna()
fig = plt.figure()
ax = fig.gca()
sst_df.plot(ax=ax, label="", xlabel="", ylabel=r"Temperature$[^\circ C]$")
ax.grid(True)
# ax.get_legend().remove()
plt.xticks(rotation=90, fontweight='light',  fontsize='x-small',)# fig.autofmt_xdate()
# plt.show(block=False)
fig.savefig("plots/sst.png")


chlor_df = df["chlor_a"].dropna()
fig = plt.figure()
ax = fig.gca()
chlor_df.plot(ax=ax, label="", xlabel="", ylabel=r"Chlorophyll$[mg/m^3]$")
ax.grid(True)
# ax.get_legend().remove()
plt.xticks(rotation=90, fontweight='light',  fontsize='x-small',)# fig.autofmt_xdate()
# plt.show(block=False)
fig.savefig("plots/chlor_a.png")

plt.close()











# fig = plt.figure()
# ax = plt.gca()
# ax.grid(True)
# ax.tick_params("both", which="minor")
# # ax.plot(df[columns.get("temperature")], label=r"temperature $^\circ C$")
# ax.plot("datetime", columns.get("temperature"), data=df, label=r"temperature $^\circ C$")
# ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%b'))

# df = df.set_index("datetime")
# temp_df = df["temperature"].dropna()
# datetime_df = df["datetime"].dropna()

# fig = plt.figure()
# ax = fig.gca()
# plt.plot(df["datetime"])
# df.plot(ax=ax, y=temp_df, label="in-situ", xlabel="Time", ylabel=r"Temperature [$^\circ C$]")
# df.plot(ax=ax, y="sst", label="remote", xlabel="Time", ylabel=r"Temperature [$^\circ C$]")
# ax.grid(True)
# ax.get_legend().remove()
# # plt.gcf().autofmt_xdate()
# # ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%b'))
# plt.show()
