# create student class that takes name & marks of 3 subjects as arguments in constructor and then create a method to print the average

# class Student:
#     def __init__(self,name,marks1,marks2,marks3):
#         self.name = name
#         self.marks1 = marks1
#         self.marks2 = marks2
#         self.marks3 = marks3

#     def printAverageOfMarks(self):
#         return round((self.marks1+self.marks2+self.marks3)/3,2)

# student1 = Student("Aniket",97,98,96)
# print(student1.printAverageOfMarks())
        
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    
    
    def printAverageOfMarks(self):
        average = 0
        
        if(isinstance(self.marks,list)):
            for mark in self.marks:
                average += mark
            return round(average/len(self.marks),2)
        else:
            return round(self.marks/3,2)

student1 = Student("Aniket",[97,98,99])
student2 = Student("Rahul",89)
print(student2.printAverageOfMarks())