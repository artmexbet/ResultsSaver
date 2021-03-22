class A:
    def __init__(self):
        self.s = [["A"], ["B"], ["C"]]

    def find_item(self, item):
        for i in range(len(self.s)):
            if item in self.s[i]:
                return self.s[i]


a = A()
b = a.find_item("A")
print(b is a.s[0])
b.append("i")
print(a.s)
