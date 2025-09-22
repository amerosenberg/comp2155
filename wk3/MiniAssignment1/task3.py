#1) Create a class called Color. (1 mark)
#2) Code 1 constructor that requires 2 parameters (2 marks)
#3) Code 2 properties/attributes of the class (2 marks)
#4) Code the toString method of the class that summarizes the properties of the class. (2 marks)
#5) Below the class definition, create one object that instantiates the Color class. (1 mark)
#Name it whatever you like. Pass whatever values you like to the constructor.
#6) Using formatted printing, output the two properties of the object. (1 mark)
#7) Output the summary of the object. (1 mark)

class Color:
    def __init__(self, hex, name):
        self.hex = hex
        self.name = name
    def __str__(self):
        return f"HexCode: {self.hex}, Name: {self.name}"

Color1 = Color("#880808", "Blood Red")

print(f"HexCode: {Color1.hex}, Name: {Color1.name}")

print(Color1)
