import student
import grades

while True:
    print("\n===== TALABALAR TIZIMI =====")
    print("1. Talaba qo'shish")
    print("2. Barcha talabalar")
    print("3. Talaba qidirish")
    print("4. Baho qo'shish")
    print("5. O'rtacha baho")
    print("6. Eng yuqori baho")
    print("0. Chiqish")

    tanlov = input("Tanlov: ")

    if tanlov == "1":
        student.talaba_qoshish()

    elif tanlov == "2":
        student.barcha_talabalar()

    elif tanlov == "3":
        student.talaba_qidirish()

    elif tanlov == "4":
        grades.baho_qoshish()

    elif tanlov == "5":
        grades.ortacha_baho()

    elif tanlov == "6":
        grades.eng_yuqori_baho()

    elif tanlov == "0":
        print("Dastur tugadi!")
        break

    else:
        print("Noto'g'ri tanlov!")