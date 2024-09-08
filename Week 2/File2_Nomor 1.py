TP = float(input("Masukkan Total Purchase : "))
Student = input("Apakah anda Student atau bukan? (Y/N) : ")
tax = 0.05
if (Student == "Y" or Student == "N"):
    if (Student == "Y"):
        Diskon = 0.2
        TulisanStudentDiscount = "20%"
    
    else:
        Diskon = 0
        TulisanStudentDiscount = "You Are Not A Student"
    
    Diskonfr = TP * Diskon
    DiskonT = TP - Diskonfr
    Pajak = DiskonT * tax
    Total = DiskonT + Pajak
    print(f"Total Purchases = ${TP:.2f}")
    print(f"Student's discount ({TulisanStudentDiscount}) = ${Diskonfr:.2f}")
    print(f"Total After Discount = ${DiskonT}")
    print(f"Sales Tax = ${Pajak}")
    print(f"Grand Total = ${Total}")
else:
    print("Jawaban Hanya Boleh Y/N!")
