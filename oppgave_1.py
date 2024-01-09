import pandas

data = pandas.read_csv("konsumprisindex.csv", delimiter=";", decimal=",")

en = data.max()

print(en)
