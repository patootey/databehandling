import csv
import locale
import numpy as np

with open("konsumprisindex.csv", encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=";")
    head = next(filinnhold)
    # Verdi, måned, år
    hi = [0, 0, 0]
    lo = [100, 0, 0]
    data = []
    for i in filinnhold:
        data.append(i)

    # setlocale gjør at den fungerer og kan gjøre komma til dot
    locale.setlocale(locale.LC_ALL, "")
    for i in data:
        for x in range(len(i)):
            if i[x] == ".":
                i[x] = np.nan
            elif x != 0:
                i[x] = locale.atof(i[x])
            else:
                i[x] = int(i[x])

    years = [x[0] for x in data]
    for i in range(len(data)):
        konsmpris = data[i][2:]

        if min(konsmpris) < lo[0]:
            lo[0] = min(konsmpris)
            lo[1] = konsmpris.index(min(konsmpris)) + 2
            lo[2] = years[i]
        if max(konsmpris) > hi[0]:
            hi[0] = max(konsmpris)
            hi[1] = konsmpris.index(max(konsmpris)) + 2
            hi[2] = years[i]

    max_change = 0
    year_with_max_change = 0
    values_for_max_change = []

    for i in range(len(data)):
        konsmpris = data[i][2:]
        change = max(konsmpris) - min(konsmpris)

        if change > max_change:
            max_change = change
            year_with_max_change = years[i]
            values_for_max_change = konsmpris

    print(
        f"Året med størst endring i konsumprisindex fra januar til desember var {year_with_max_change}."
    )
    print(f"Dette var verdiene for alle månedene dette året: {values_for_max_change}")

print(
    f"Måneden med lavest konsumprisindex var {head[lo[1]]} i {lo[2]} med en verdi på {lo[0]}"
)
print(
    f"Måneden med høyest konsumprisindex var {head[hi[1]]} i {hi[2]} med en verdi på {hi[0]}"
)
