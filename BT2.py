# Phan tich loi
# Toan tu or dang bi su dung sai
# Toan tu or thi la 1 trong 2 dieu kien dung thi se ra dung dung
# Toan tu and thi phai 2 dieu kien dung moi in ra dung

# Sua code
print("----- BLOOD DONOR SCREENIG SYSTEM---")
donor_age =int(input("Enter donor's age: "))
donor_weight = float(input("Enter donor's weight(kg): "))

# He thong kiem tra dieu kien hien mau
if donor_age >= 18 and donor_weight >= 50:
    print("Result: ELIGIBLE. Please procced to the blood donation room.")
else:
    print("Result: NOT ELIGIBLE. Thank you for your interest")