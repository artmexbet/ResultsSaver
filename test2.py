with open("a", "rb") as a, open("b", "w") as b:
    b.write(a.read())