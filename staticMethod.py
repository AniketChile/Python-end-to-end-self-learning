# static methods are the method that dont use the self parameter and work at the class level
class MathUtil:
    @staticmethod
    def addTwoSum(x,y):
        return (x+y)
    
print(MathUtil.addTwoSum(5,6))