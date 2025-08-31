# The generator and the iterator 

# the generator
the generator are the iterator that only run once.
the generator use the keyword yield
the yield keyword store the state of the object 

f = open('4_GeneratorAndIterator.md')
f.__next__() <!---- this is the raw method -->

<!-- The iterator has the acess to the iterable objects -->
<!-- the iter() is used and the paramter is the iterable objects -->
<!-- the iter(iterable_object) always point to the start and the __next__() / next() is use to go the next memory and generate the value -->
<!-- the stop iteration error is raised when the iterable object gets but of bound -->

<!-- For exampler for iter() -->
list1 = [1,2,3,4,5,6]
I = iter(list1)
print(I) -> this will print the starting memory point of the iterable object
to access the next we will use the
print(next(I)) - print(I.__next__()) //anyone can be use

<!-- Generator function even generator -->
<!-- the generator are the itertable objects that can at only run at once the generator has access to the yield key word which hold the current refernce of the object and keep the track of that and internally the __next__() keeps the track of the next object present in the iterable object -->
def even_Generator(limit):
    for i in range(2,limit+1,2):
        yeild i


for num in even_Generator(10):
    print(num)