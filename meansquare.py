## =======最小2乗平均プログラム========================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("data.csv", parse_dates=['Date'])

x = data['Date'].values.astype(np.int64) // 10 ** 9
y = data['end'].values
X = np.arange(1, len(x)+1)
y_data_3 = np.polyfit(x, y, 3)
Y3 = np.poly1d(y_data_3)(x)
y_data_4 = np.polyfit(x, y, 4)
Y = np.poly1d(y_data_4)(x)
plt.plot(x, Y)
plt.plot(x, Y3)
plt.scatter(x, y)
plt.show()