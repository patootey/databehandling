# hello

# Oppgave 1:
import csv
with open("konsumprisindex.csv", encoding="utf-8-sig") as fil:
    data = csv.reader(fil, delimiter=";")
    head = next(data)
    for i in data:
        print(i)

# Oppgave 2:
# Oppgave 1: Vebjørn og Mathilde


# Oppgave 3:
