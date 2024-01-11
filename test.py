# hello

# Oppgave 1:
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
    years = [x[0] for x in data]
    for i in data:
        # print(i.index(min(i)))
        # print(head[i.index(min(i))])
        if min(i) < lo[0]:
            lo[0] = min(i)
            lo[1] = i.index(min(i))
            lo[2] = i[0]
        if max(i) > hi[0]:
            hi[0] = max(i)
            hi[1] = i.index(max(i))
            hi[2] = i[0]
        
print(f"Måneden med lavest konsumprisindex var {head[lo[1]]} i {lo[2]} med en verdi på {lo[0]}")
print(f"Måneden med høyest konsumprisindex var {head[hi[1]]} i {hi[2]} med en verdi på {hi[0]}")

# Oppgave 2:
# Oppgave 1: Vebjørn og Mathilde


# Oppgave 3:
