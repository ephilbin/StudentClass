class Student(Person):
    def _init_(self, name, age, gender, course):
        super()._init_(name, age, gender)
        self.course = course
        #adding attribute course and inheriting everything else
        def study(self):
            print(f"{self.name} is studying {self.course}.") 