# In Python the fundamental distinction is made on data whether it's value changes or not

if the value changes then it is called mutuable object
if the value dont not change then it is called the immutable object


# Mutable Data Types 
- list , set , dictonary

# Immutable Data Types
- Numbers (int,decimal) ,Boolean,string, tuples, frozenset


from decimal import Decimal

<!-- # Float imprecision -->
print(0.1 + 0.2 == 0.3)  # Output: False

<!-- # Decimal precise arithmetic -->
print(Decimal('0.1') + Decimal('0.2') == Decimal('0.3'))  # Output: True
