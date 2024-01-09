import matplotlib.pyplot as plt
import numpy as np
 
data = np.loadtxt("konsumprisindex.csv",  delimiter=";", dtype=str).tolist()
years = []
months = []

data.pop(0)
for p in data:
    years.append(int(p[0]))
    month = []
    for i in range(len(p)- 1):
        d = p[i + 1].replace(",", ".")
        if (d != '.'):
            month.append(float(d))
        else:
            month.append(np.nan)
    months.append(month)

print(years)

averages = []

for m in months:
    averages.append(np.nanmean(m))


plt.plot(years, averages)
plt.show()

