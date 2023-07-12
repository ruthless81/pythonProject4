class Person:
    def __init__(self,name,username,age):
        self.name = name
        self.username = username
        self.age = age

class DictMixin:
    def return_dict(self):
        return self.__dict__

class Student(Person,DictMixin):
    def __init__(self,University,name,username,age):
        self.University = University

        super().__init__(name,username,age)




student = Student("BTU","gela",'gnolidze',34)
#person = Person('gela','gnolidze',34)

print(student.__dict__)

