note = """
-----------------------------------------
       Python Float Topic Note
-----------------------------------------

1. Introduction to Floats:

    - In Python, a float is a data type that represents real numbers with a decimal point.

2. Declaration and Assignment:

    - You can declare and assign float values straightforwardly:
    
    temperature = 24.5
    pi = 3.14159265359
    
3. Arithmetic Operations:

    - Floats support various arithmetic operations, just like integers:
    
    x = 10.0
    y = 3.0
    sum_result = x + y  # 13.0
    difference = x - y  # 7.0
    multiplication = x * y  # 30.0
    division = x / y  # 3.33333333333

4. Type Conversion:

    - You can convert other data types to floats using the 'float()' function:
    
    num_str = "42.75"
    num_float = float(num_str)  # Converts a string to a float
    
5. Rounding:

    - Python provides functions for rounding float numbers:
    
    rounded_value = round(4.6)  # 5
    precise_rounding = round(4.567, 2)  # 4.57 (round to 2 decimal places)
    
6. Mathematical Functions:

    - Floats can be used with various mathematical functions, including 'abs()', 'pow()', 'sqrt()', 'sin()', 'cos()', 'tan()', and more:
    
    absolute_value = abs(-10.5)  # 10.5
    power = pow(2.0, 3.0)  # 8.0
    square_root = sqrt(25.0)  # 5.0
    sine_value = sin(0.0)  # 0.0
    cosine_value = cos(pi)  # -1.0
    tangent_value = tan(0.0)  # 0.0
    
7. Floating-Point Precision:

    - Be aware that float numbers have limited precision due to how computers store them, which can lead to small rounding errors in calculations.
    
-----------------------------------------
"""

print(note)
