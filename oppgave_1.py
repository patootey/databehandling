import csv
import locale
import numpy as np
# Importerer csv for å behandle csv filen, locale for å skrive om filen og numpy 
# for senere behandling

with open("konsumprisindex.csv", encoding="utf-8-sig") as fil:
    # Variabel for innholdet i filen slik det er lest av csv med ';' 
    # som skille mellom verdier
    filinnhold = csv.reader(fil, delimiter=";")
    
    # next gir den første raden i dataen til filen
    overskrift = next(filinnhold)

    # To lister som skal lagre dataen til minst og størst verdi i en måned og år
    # lo starter med verdi på 100% slik at den bare kan gå ned
    # Verdi, måned, år
    hoy = [0, 0, 0]
    lav = [100, 0, 0]

    # Liste med dataen i filinnhold som gjør at en kan behandle det
    data = []
    for i in filinnhold:
        data.append(i)

    # setlocale gjør at den fungerer og kan gjøre komma til dot
    locale.setlocale(locale.LC_ALL, "")
    
    # Looper gjennom dataen og endrer verdiene til lesbare numre
    for i in data:
        for x in range(len(i)):
            if i[x] == ".":
                # numpy not actual number brukes for å ha en verdi som
                # fungerer som int eller float uten at det har verdi
                i[x] = np.nan
            elif x != 0:
                # Endrer komma til punktum og legger det inn i riktig sted
                i[x] = locale.atof(i[x])
            else:
                # Endrer årstallet til int bare fordi
                i[x] = int(i[x])

    # Liste med alle årene som dukker opp i datasettet
    aar = [x[0] for x in data]
    
    for i in range(len(data)):
        # Liste som inneholder kun konsumprisen og ikke gjennomsnitt eller år
        konsmpris = data[i][2:]

        # Sjekker om den minste verdien er mindre enn den lagrede
        if min(konsmpris) < lav[0]:
            lav[0] = min(konsmpris)
            lav[1] = konsmpris.index(min(konsmpris)) + 2
            lav[2] = aar[i]
        
        # Sjekker om den største verdien er større enn den lagrede
        if max(konsmpris) > hoy[0]:
            hoy[0] = max(konsmpris)
            hoy[1] = konsmpris.index(max(konsmpris)) + 2
            hoy[2] = aar[i]

print(
    f"Måneden med lavest konsumprisindex var {overskrift[lav[1]]} i {lav[2]} med en verdi på {lav[0]}"
)
print(
    f"Måneden med høyest konsumprisindex var {overskrift[hoy[1]]} i {hoy[2]} med en verdi på {hoy[0]}"
)
