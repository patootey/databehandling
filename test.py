# hello

# Oppgave 1:
import csv
with open("konsumprisindex.csv", encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=";")
    head = next(filinnhold)
    hi = ["num", "mon"]
    lo = ["num", "mon"]
    data = []
    for i in filinnhold:
        data.append(i)
    print(data)

# Oppgave 2:
# Oppgave 1: Vebjørn og Mathilde


# Oppgave 3:
