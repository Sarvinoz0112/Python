#Ex 1 Haqiqiy tipli, 16 ta elementdan iborat list yarating. Minimal va maksimal elementlarini indeksi(joylashgan o`rinini) toping.
def find_min_max_indices(my_list):
        
    min_index = my_list.index(min(my_list))
    max_index = my_list.index(max(my_list))
    return min_index, max_index
    
num_list = [2.2, 5.3, 8.5, 1.8, 4.3, 7.8, 3.4, 6.9, 9.1, 14.1, 25.0, 11.5, 21.6, 15.9, 22.4, 23.7, 17.1]

min_index, max_index = find_min_max_indices(num_list)

print(f"Index of the minimal element: {min_index}")
print(f"Index of the maximal element: {max_index}")



#Ex 2 Butun tipli, 14 ta elementdan iborat list yarating uni ichida ham musbat ham manfiy bo'lsin. Musbat sonlarning toqlari yig`indisini va sonini xisoblang.
def positive_odd_sum_and_count(numbers):

    positive_odd_sum = sum(num for num in numbers if num > 0 and num % 2 != 0) #Bu yerda "num" yozilgan, chunki biz musbat toq sonlarning yeg'indisini hisoblamoqchimiz

    positive_count = sum(1 for num in numbers if num > 0)# Bu yerda "1" yozilgan, chunki biz har bir musbat sonni nechtaligini sanamoqchimiz
    
    return positive_odd_sum, positive_count

numbers = [4, -3, 7, -2, 11, 5, -6, 14, 1, 8, -10, 3, 2, -7]

positive_odd_sum, positive_count = positive_odd_sum_and_count(numbers)

print("Sum of positive odd numbers:", positive_odd_sum)
print("Count of positive numbers:", positive_count)



#Ex 3
import random

nums_list = [random.uniform(0, 100) for _ in range(14)]

def sorting(lst):

    first_half = lst[:6]
    second_half = lst[6:]
    
    first_half.sort() #.sort() metodi ro'yxatning elementlarini o'sish tartibida (eng kichikdan eng kattaga) tartiblaydi.
    second_half.sort(reverse=True) #.sort(reverse=True) metodi ro'yxatning elementlarini kamayish tartibida (eng kattadan eng kichikka) tartiblaydi.

    return first_half + second_half

result = sorting(nums_list)
print(result)