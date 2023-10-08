note = """
-----------------------------------------
       Python Integer Topic Note
-----------------------------------------

1. Introduction to Integers:

    - In Python, an integer is a whole number without a decimal point. It can be positive or negative.

2. Declaration and Assignment:

    - You can declare and assign integer values straightforwardly:
    
    age = 25
    count = -10
    
3. Arithmetic Operations:

    - Integers support various arithmetic operations:
    
    x = 10
    y = 5
    sum_result = x + y  # 15
    difference = x - y  # 5
    multiplication = x * y  # 50
    division = x / y  # 2.0 (float result)

4. Integer Division (Floor Division):

    - The '//' operator performs integer division, rounding down to the nearest whole number:
    
    result = 7 // 3  # 2

5. Modulus Operator:

    - The '%' operator calculates the remainder when one integer is divided by another:
    
    remainder = 7 % 3  # 1

6. Exponents:

    - You can use the '**' operator for exponentiation:
    
    square = 3 ** 2  # 9

7. Type Conversion:

    - You can convert other data types to integers using the 'int()' function:
    
    num_str = "42"
    num_int = int(num_str)  # Converts a string to an integer
    
8. Mathematical Functions:

    - Python provides mathematical functions for integers, such as 'abs()', 'pow()', 'round()', and 'divmod()':
    
    absolute_value = abs(-10)  # 10
    power = pow(2, 3)  # 8
    rounded_value = round(4.6)  # 5
    quotient, remainder = divmod(10, 3)  # Quotient: 3, Remainder: 1
    
-----------------------------------------
"""

print(note)
