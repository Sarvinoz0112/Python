def divide_without_division(a, b):
    a = int(a)
    b = int(b)
    
    quotient = 0
    remainder = a
    
    while remainder >= b:
        remainder -= b
        quotient += 1
    return quotient, remainder

first_num = input("Enter first number: ")
second_num = input("Enter second number: ")
quotient, remainder = divide_without_division(first_num, second_num)

print(f"{first_num} ni {second_num} ga bo'lish natijasi:")
print(f"Bo'linma: {quotient}")
print(f"Qoldiq: {remainder}")