#Ex 1
import random

even_num = 0

my_list = [random.randint(1, 100)]

for _ in range(14):
    my_list.append(random.randint(1, 100)) # .randint(a, b) — returns a random integer from the range [a, b] (including both ends).
    
for i in my_list:
    if i % 2 == 0:
        even_num += 1

print(f"Random list: {my_list}")
print(f"Number of even numbers: {even_num}")


#Ex 2
import random

old_list = [random.randint(1, 100)]

for _ in range(12):
    old_list.append(random.randint(1, 100))

print("Preliminary list:", old_list)

average = sum(old_list) / len(old_list)

old_list[4] = average

print(f"Result: {old_list}")


#Ex 3
import random

my_list = [random.randint(1, 100)]

for _ in range(10):
    my_list.append(random.randint(1, 100))

print("Preliminary list:", my_list)

max_value = max(my_list)
index_a = my_list.index(max_value)

my_list[0], my_list[index_a] = my_list[index_a], my_list[0] #Bu qator birinchi element (my_list[0]) va maksimal elementning o'rni (my_list[index_a]) ni almashtiradi

print(f"New list: {my_list}")


#Ex 4
import random

my_list = [random.randint(1, 100)]

for _ in range(10):
    my_list.append(random.randint(1, 100))

print("Preliminary list:", my_list)

min_value = min(my_list)
max_value = max(my_list)

min_index = my_list.index(min_value)
max_index = my_list.index(max_value)

my_list[min_index], my_list[max_index] = my_list[max_index], my_list[min_index] #Bu qator birinchi element (my_list[0]) va maksimal elementning o'rni (my_list[index_a]) ni almashtiradi

print(f"New list: {my_list}")


#Ex 5
numbers = [5, 12, 7, 22, 3, 8, 15, 30, 17, 6, 9, 41, 28, 19, 24, 2, 10, 37, 44, 55]
print("List:", numbers)

max_even = 0
max_odd = 0

for num in numbers:
    if num % 2 == 0:
        if num > max_even:
            max_even = num
    else:
        if num > max_odd:
            max_odd = num

print(f"Largest even number: {max_even}")
print(f"Largest odd number: {max_odd}")