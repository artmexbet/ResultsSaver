import openpyxl

with open("aaaa.xlsx", "rb") as data, open("s.xlsx", "wb+") as file:
    file.write(data.read())
a = openpyxl.load_workbook("s.xlsx")
ws1 = a.active
for i in "ABC":
    print(ws1[f"{i}1"].value)
