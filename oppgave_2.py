# Importerer pyplot fra matplotlib for å tegne grafer
import matplotlib.pyplot as plt
# Importerer numpy for å håndtere NaN-verdier
import numpy as np

"""
Oppgave 2
"""

# Hjelpefunksjon som bruker list comprehension for å bytte ut . med , og erstatte tomme elementer med numpy-NaN-verdi
def parse_yearly_data(data : list):
    return [float(x.replace(',', '.')) if x != '.' else np.nan for x in data[2:]]

# Del a)
# Tegner graf av gjennomsnittsverdier for hvert år
def graph_yearly_averages(data : list):
    years = [int(x[0]) for x in data[1:]]
    months = [parse_yearly_data(x) for x in data[1:]]
    averages = [np.nanmean(x) for x in months]
    plt.plot(years, averages)
    plt.title("Gjennomsnittlige konsumprisindekser for hvert år")
    plt.xlabel("År")
    plt.ylabel("Gjennomsnittlig konsumprisindeks")
    plt.show()

# Del b)
# Tegner graf av verdier for hver måned i 2022
def graph_monthly_averages(data : list):
    year = [x for x in parse_yearly_data(data[1])]
    month_names = data[0][2:]
    for i in reversed(range(len(year))):
        if (np.isnan(year[i])):
            year.pop(i)
            month_names.pop(i)
    plt.bar(month_names, year, 0.5)
    plt.title("Konsumprisindekser for 2022")
    plt.xlabel("Måneder")
    plt.ylabel("Konsumpris")
    plt.show()

# Leser data
data = np.loadtxt("konsumprisindex.csv",  delimiter=";", dtype=str).tolist()

graph_yearly_averages(data)
graph_monthly_averages(data)