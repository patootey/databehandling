import tkinter as tk  
root = tk.Tk()
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

def button():
    belop = int(belop_entry.get())
    fra = int(fra_entry.get())
    til = int(til_entry.get())
    if fra < 1929 and fra > 2023:
        print("u worng")
    if til < 1929 and til > 2023 & til > fra:
        print("u wronf")
    print((belop, fra, til))

    

     



tk.Button(frame, text="Se prisendring", command=button, bg="green").grid(column=1, row=4)

frame.place(y=70)
root.mainloop()