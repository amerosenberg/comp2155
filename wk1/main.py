class Grade:
    def __init__(self, percentage):
        self.percentage = percentage

    @property
    def percentage(self):
        return self.__percentage


    @percentage.setter
    def percentage(self, value:int)->None:
        if isinstance(value, int) and value >= 0 and value <= 100:
            self.__percentage = value
        else:
            raise ValueError("Invalid percentage")

class PassingGrade(Grade):
    def __init__(self, percentage):
        super().__init__(percentage)


my_grade = Grade(90)
print(my_grade.percentage)