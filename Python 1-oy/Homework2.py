#Ex 1
raqam = input("Biror raqam kiriting: ")
bosh = raqam[0]
oxir = raqam[-1]
print("Bosh va oxiridagi raqamlar:", bosh, oxir)

#Ex 2
ism = input("Ismingizni kiriting: ")
bosh_harf = ism[0]
print("Ismingizni bosh harfi:", bosh_harf)

#Ex 3
user = input("Familiyangizni kiriting: ")
oxirgi_harf = user[-1]
print("Familiyangizning oxirgi harfi:", oxirgi_harf)

#Ex 4
kun = int(input("Birinchi sonni kiriting (1-7): "))
qancha_kun = int(input("Ikkinchi sonni kiriting (qancha kundan keyin): "))

if kun == 1:
        print("Hozir Monday kuni.")
elif kun == 2:
        print("Hozir Tuesday kuni.")
elif kun == 3:
        print("Hozir Wednesday kuni.")
elif kun == 4:
        print("Hozir Thursday kuni.")
elif kun == 5:
        print("Hozir Friday kuni.")
elif kun == 6:
        print("Hozir Saturday kuni.")
else:
        print("Hozir Sunday kuni.")

keyin = (kun + qancha_kun) % 7

if keyin == 1:
        print(qancha_kun, "kun o'tgandan so'ng Monday kuni bo'ladi.")
elif keyin == 2:
        print(qancha_kun, "kun o'tgandan so'ng Tuesday kuni bo'ladi.")
elif keyin == 3:
        print(qancha_kun, "kun o'tgandan so'ng Wednesday kuni bo'ladi.")
elif keyin == 4:
        print(qancha_kun, "kun o'tgandan so'ng Thursday kuni bo'ladi.")
elif keyin == 5:
        print(qancha_kun, "kun o'tgandan so'ng Friday kuni bo'ladi.")
elif keyin == 6:
        print(qancha_kun, "kun o'tgandan so'ng Saturday kuni bo'ladi.")
elif keyin == 0:
        print(qancha_kun, "kun o'tgandan so'ng Sunday kuni bo'ladi.")
else:
        print("Noto'g'ri kiritildi.")