import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv("final1.csv")
export_df = df.drop("datetime", axis=1).dropna()

y = export_df["do"]
x = export_df.drop("do", axis=1)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=45)

LR = LinearRegression()
LR.fit(x_train, y_train)

y_prediction = LR.predict(x_test)

# cm = confusion_matrix(y_test, y_prediction)
r2_score(y_test, y_prediction)
mean_squared_error(y_test, y_prediction)

fig = plt.figure()
ax = plt.gca()
ax.plot(range(1, 15), range(1, 15), "C2", label="1:1")
ax.plot(y_prediction, y_test, "o", markersize=1.5)
ax.set_xlabel(r"DO predicted [$mg L^{-1}$]")
ax.set_ylabel(r"DO field data [$mg L^{-1}$]")
ax.set_title("Multiple Linear Regression model")
ax.set_aspect("equal")
ax.set_xlim(5, 14)
ax.set_ylim(5, 14)
plt.legend()
# plt.show(block=False)
fig.savefig("plots/mlr_test.png")
