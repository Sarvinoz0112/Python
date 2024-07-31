#Ex 1
my_list =[1, 1, 2, 8, 7, 8, 7, 6, 4, 5]
result = set(my_list)
print(result)


# #Ex 2
# list1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# list2 ={5, 6, 7, 8, 9, 10, 11, 12, 13, 14}

# result = list1.symmetric_difference(list2)
# print(result)



# #Ex 3
# choy = {"qora", "ko'k", "limonli"}
# kofe ={"Arabica", "Robusta","Espresso"}



# #Ex 1
# my_list = {"Sarvinoz", "Akmal", "Davron", "Mohiyahon"}
# name = input("Enter your name: ")
# if name in my_list:
#     print("Sening ismin bor:")
# else:
#     name = my_list.add(name)
# print(my_list)
# # ______________________________________________________


# #Ex 2
# def unique(day1, day2):
#     set_day1 = set(day1)
#     set_day2 = set(day2)

#     result = set_day1.symmetric_difference(set_day2)
    
#     return result


# day1 = ["S", "A", "I", "R", "S", "A"]
# day2 = ["S", "A", "I", "R", "S", "U", "P"]

# unique_visitors = unique(day1, day2)
# print(unique_visitors)
# print(len(unique_visitors))
# # ______________________________________________________


# def maxsulot(odam_sotvogan, sotvolinmagangan):
#     set1 = set(odam_sotvogan)
#     set2 = set(sotvolinmagangan)

#     if odam_sotvogan not in sotvolinmagangan:
#        print(sotvolinmagangan)

#     result = set1.symmetric_difference(set2)
    
#     return result


# odam_sotvogan = ["qora choy ", "ko'k choy ", "limonli "]
# sotvolinmagangan = ["ruchka ", "karto'shka ", "olma "]

# if odam_sotvogan not in sotvolinmagangan:
#     print(sotvolinmagangan)


def maxsulot(odam_sotvogan, sotvolinmagangan):
    set1 = set(odam_sotvogan)
    set2 = set(sotvolinmagangan)

    result = set1.symmetric_difference(set2)
    
    return result

odam_sotvogan = {"qora choy", "ko'k choy", "limonli"}
sotvolinmagangan = {"ruchka", "karto'shka", "olma"}

tavsiyalar = maxsulot(odam_sotvogan, sotvolinmagangan)

sotib_olmagan_narsalar = sotvolinmagangan.difference(odam_sotvogan)

print("Tavsiya qilinadigan mahsulotlar:", sotib_olmagan_narsalar)