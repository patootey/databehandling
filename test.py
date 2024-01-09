# hello

# Oppgave 1:
import csv
import locale
import numpy as np
with open("konsumprisindex.csv", encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=";")
    head = next(filinnhold)
    hi = ["num", "mon"]
    lo = ["num", "mon"]
    data = []
    for i in filinnhold:
        data.append(i)
    
    # data[0][2] = float(data[0][2])
    # setlocale gjør at den fungerer og kan gjøre komma til dot
    locale.setlocale(locale.LC_ALL, '')
    for i in data:
        for x in range(len(i)):
            if i[x] == '.':
                i[x] = np.nan
            elif x != 0:
                i[x] = locale.atof(i[x])
            else:
                i[x] = int(i[x])

    for i in data:
        print(i.index(min(i)))

# Oppgave 2:
# Oppgave 1: Vebjørn og Mathilde


# Oppgave 3:
