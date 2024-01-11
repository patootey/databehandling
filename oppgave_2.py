import matplotlib.pyplot as plt
import numpy as np

def parse_yearly_data(data : list):
    return [float(x.replace(',', '.')) if x != '.' else np.nan for x in data[2:]]

def graph_yearly_average(data : list):
    years = [int(x[0]) for x in data[1:]]
    months = [parse_yearly_data(x) for x in data[1:]]
    averages = [np.nanmean(x) for x in months]
    plt.plot(years, averages)
    plt.show()

def graph_months(data : list):
    year = [x for x in parse_yearly_data(data[1])]
    month_names = data[0][2:]
    for i in reversed(range(len(year))):
        if (np.isnan(year[i])):
            year.pop(i)
            month_names.pop(i)
    plt.bar(month_names, year, 0.5)
    plt.show()
    pass

data = np.loadtxt("konsumprisindex.csv",  delimiter=";", dtype=str).tolist()

graph_yearly_average(data)
graph_months(data)