fname = input("Enter First Name: ")
lname = input("Enter Last Name: ")
id = input("Enter Student ID: ")

class Student:
    def __init__(self, fname, lname, id):
        self.fname = fname
        self.lname = lname
        self.id = id

    def __str__(self):
        return f"First name {self.fname}, Last name {self.lname}, Student ID {self.id}"


    def save(self):
        with open(f"{self.id}.txt", "w") as fo:
            fo.write(f"{self.fname}\n{self.lname}")

    def read(self):
        with open(f"{self.id}.txt", "r") as fo:
            output = fo.readlines()
            print(f"The student firstname is {output[0].strip()}. The student lastname is {output[1]}")

test = Student(fname, lname, id)
print(test)
test.save()
test.read()
