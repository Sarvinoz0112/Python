#Ex 1. Foydalanuvchidan uning ismini so'rang, agar kiritilgan ism bo'sh satrga teng bo'lmasa,
# unda "Xush kelibsiz" matninig chiqaring va while o'z ishini to'xtatsin, 
# agar ism kiritish o'rniga foydalanuvchi "Enter" tugmasini bosib o'tib ketsa (ism kiritmasda), 
# unda qayta ism so'ralsin, toki ism sifatida uzunligi hech bo'lmaganda 1 ga teng bo'lmagan ism kiritilmagunicha.

text = input("Enter your name: ")

while text == "":
    text = input("Please enter your name: ")
    
print("Welcome,", text, "!")
        

#Ex 2. While operatorini ishlatgan holda 1-100 gacha raqamlar orasida faqat juftlari chiqarilsin.
# Bunda for operatori yoki range ishlatilmasin, faqat while operatori orqali.

raqam = 1

while raqam <= 100:
    if raqam % 2 == 0:
        print(raqam)
    raqam += 1


#Ex 3. Foydalanuvchidan so'z kiritish so'ralsin, agar so'z "exit" so'ziga teng bo'lsa, unda dastur darhol to'xtasin,
# aks holatda kiritilgan so'zni uzunligi chiqarib berilsin, toki "exit" kiritilmagunicha. So'z uzunligini len() funksiyasi orqali olishingiz mumkin,
# masalan: len("salom") bizga 5 ni qaytaradi va shu print ga uzatilsa so'z uzunligi kelib chiqadi, masalan: print("So'z uzunligi:", len("salom")) # So'z uzunligi: 5

word = input("So'z kiriting: ")

while word != "exit":
    word_length = len(word)
    print("Matnda", word_length, "ta harf bor")
    word = input("So'z kiriting: ")

print("Siz dasturdan chiqtingiz!")