import pandas

csv = pandas.read_csv("supermarkets.csv")
jsonF = pandas.read_json("supermarkets.json")
excel = pandas.read_excel("supermarkets.xlsx", sheet_name=0)
comaatext = pandas.read_csv("supermarkets-commas.txt")
## default separator is ","
separatortext = pandas.read_csv("supermarkets-semi-colons.txt", sep=";")


print(csv)
"""
var.set_index("ID") use as index
"""
print("\n", jsonF.set_index("ID"))

print("\n", excel.set_index("ID"))

print("\n", comaatext)

print("\n", separatortext.set_index("ID"))

data = pandas.read_csv("testexample.csv")
#data["Continent"] = data.shape[0] * ["welcome to america"]
print("\n", data)
