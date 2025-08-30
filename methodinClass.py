# a method defined is liket the regualr function but it defines the behavious or the action that the object can perform created from that class
# the first parameter in the method inside the class is the self which tell the current instance of that class i.w which object is trying to use this method

class College:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def helloStudent(student):
        return f"hello student whos name is {student.name}"
    

student1 = College("Aniket",97)
print(student1.helloStudent())