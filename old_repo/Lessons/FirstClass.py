class FirstClass:
    def setData(self, value):
        self.data = value
    def display(self):
        print(self.data)

x = FirstClass()
y = FirstClass()
x.setData("King Arthur")
y.setData(3.14159)
x.display()
y.display()