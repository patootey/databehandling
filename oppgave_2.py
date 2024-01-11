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
    year = parse_yearly_data(data[1])
    month_names = data[0][2:]
    print(year)
    # for p in data:
    #     if not skipped_first:
    #         skipped_first = True
    #         continue
    #     years.append(int(p[0]))
    pass


data = np.loadtxt("konsumprisindex.csv",  delimiter=";", dtype=str).tolist()

graph_yearly_average(data)

graph_months(data)

