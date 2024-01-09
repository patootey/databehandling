# hello

# Oppgave 1:
import csv
import locale
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
                i[x] = ""
            elif x != 0:
                i[x] = locale.atof(i[x])
            else:
                i[x] = int(i[x])
    for i in range(len(data)):
        if i != 0:
            print(min(data[i]))

# Oppgave 2:
# Oppgave 1: Vebjørn og Mathilde


# Oppgave 3:
