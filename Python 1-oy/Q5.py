prime_sum = 0

for num in range(2, 101):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_sum += num

digit_sum = 0
for digit in str(prime_sum):
    digit_sum += int(digit)

print(f"The sum of prime numbers between 1 and 100 is: {prime_sum}")
print(f"The sum of the digits of this sum is: {digit_sum}")