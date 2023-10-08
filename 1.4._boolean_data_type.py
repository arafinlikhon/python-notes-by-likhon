note = """
-----------------------------------------
       Python Boolean Topic Note
-----------------------------------------

1. Introduction to Booleans:

    - In Python, Boolean values represent truth or falsehood and have two possible values: True and False.

2. Declaration and Assignment:

    - You can declare and assign Boolean values directly:
    
    is_python_fun = True
    is_raining = False
    
3. Comparison Operators:

    - Boolean values often result from comparisons using operators like '==', '!=', '>', '<', '>=', and '<=':
    
    age = 25
    is_adult = age >= 18  # Evaluates to True
    
4. Logical Operators:

    - Python provides logical operators 'and', 'or', and 'not' for combining Boolean values:
    
    is_sunny = True
    is_warm = True
    is_good_weather = is_sunny and is_warm  # Evaluates to True
    
5. Truthy and Falsy Values:

    - In Python, certain values are considered 'truthy' (evaluates to True) and 'falsy' (evaluates to False):
    
    - Falsy values include None, 0, empty sequences (e.g., empty string or list), and False.
    - Everything else is considered truthy.
    
6. Conditional Statements:

    - Boolean values are often used in conditional statements to control program flow:
    
    if is_sunny:
        print("It's a sunny day!")
    else:
        print("It's not sunny today.")
    
7. Boolean Expressions:

    - You can create complex Boolean expressions using parentheses to define the order of evaluation:
    
    is_warm_and_sunny = is_sunny and (temperature > 25)
    
8. Boolean Conversion:

    - You can convert other data types to Boolean using 'bool()' function:
    
    is_valid = bool(user_input)  # Converts user input to a Boolean value
    
-----------------------------------------
"""

print(note)
