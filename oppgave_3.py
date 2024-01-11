import tkinter as tk 
import numpy as np
import oppgave_2 as opg2
data = np.loadtxt("konsumprisindex.csv",  delimiter=";", dtype=str).tolist()
years = [int(x[0]) for x in data[1:]]
months = [opg2.parse_yearly_data(x) for x in data[1:]]
averages = [np.nanmean(x) for x in months]
root = tk.Tk()
root.geometry("400x300")
frame = tk.Frame(root)

tk.Label(frame, text="Skriv inn beløp: ").grid(column=1, row=0)
belop_entry = tk.Entry(frame)
belop_entry.grid(column=1, row=1)

tk.Label(frame, text="Beregn pris fra: ").grid(column=1, row=2)
fra_entry = tk.Entry(frame)
fra_entry.grid(column=1, row=3)

tk.Label(frame, text="Beregn pris til : ").grid(column=2, row=2)
til_entry = tk.Entry(frame)
til_entry.grid(column=2, row=3)

output = tk.Label(frame, text="Skriv no", font=("Helvetica", 20), width=0, fg="red")
output.grid(column=2, row=5)

def button():
    belop = int(belop_entry.get())
    fra = int(fra_entry.get())
    til = int(til_entry.get())
    if fra < 1929 or fra > 2023 or til < 1929 or til > 2023:
        output.config(text="feil år")
        fra_entry.delete(0,"end")
        til_entry.delete(0,"end")
        return

    output.config(text=f"{calculator(belop, fra, til)} kr !!!")

def calculator(belop, fra, til):
    return round(averages[years.index(til)] / averages[years.index(fra)] * belop, 1)

tk.Button(frame, text="Se prisendring", command=button, bg="green").grid(column=1, row=4, padx=0)

frame.place(y=70)
root.mainloop()
