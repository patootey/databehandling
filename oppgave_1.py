import pandas

data = pandas.read_csv("konsumprisindex.csv", delimiter=";")

en = data.max()

print(en)
