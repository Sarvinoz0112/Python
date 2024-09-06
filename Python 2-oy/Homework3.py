#Ex 1
def get_unique_elements(my_list):
    unique_elements = set(my_list)
    return unique_elements

my_list = [1, 1, 2, 8, 7, 8, 7, 6, 4, 5]

result = get_unique_elements(my_list)

print(result)



#Ex 2
def check_elements_in_list(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    
    all_elements_in_second_list = set1.issubset(set2) # .issubset bir setning boshqa bir set ichida to'liq mavjudligini tekshiradi va faqat True va False jovob qaytaradi.
    
    return all_elements_in_second_list


list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = check_elements_in_list(list1, list2)

print(result)



#Ex 3
def check_name_in_lists(name, tea_list, coffee_list):
    in_tea_list = name in tea_list
    in_coffee_list = name in coffee_list

    return in_tea_list, in_coffee_list

tea_list = ["Alisa", "Bob", "Nicke", "Hardin", "Tom"]
coffee_list = ["Alice", "David", "Tom", "Safia", "Nicke"]

name = input("Enter your name: ")

in_tea_list, in_coffee_list = check_name_in_lists(name, tea_list, coffee_list)

if in_tea_list and in_coffee_list:
    print(f"{name} is in tea and coffee lists.")
elif in_tea_list:
    print(f"{name} is in the tea list.")
elif in_coffee_list:
    print(f"{name} is in the coffee list.")
else:
    print(f"{name} is in neither list.")



#Ex 4
def find_common_users(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    
    common_users = set1.intersection(set2)
    
    return common_users

list1 = ["Alice", "Bob", "Charlie", "Dave"]
list2 = ["Tom", "Bob", "Frank", "Charlie"]

common_users = find_common_users(list1, list2)

print(f"Common users: {common_users}")