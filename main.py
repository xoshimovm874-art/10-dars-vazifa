from student import talaba_qoshish, barcha_talabalar, talaba_qidirish
from grades import baho_qoshish, ortacha_baho, eng_yuqori_baho_olgan

def menu():
    while True:
        print("\n--- TALABALARNI BOSHQARISH TIZIMI ---")
        print("1. Talaba qo'shish")
        print("2. Barcha talabalarni ko'rish")
        print("3. Talaba qidirish")
        print("4. Talabaga baho qo'shish")
        print("5. O'rtacha bahoni hisoblash")
        print("6. Eng yuqori baho olgan talabani aniqlash")
        print("0. Chiqish")
        
        tanlov = input("Tanlovingizni kiriting (0-6): ")
        
        if tanlov == "1":
            ism = input("Talabaning ismi: ")
            talaba_qoshish(ism)
        elif tanlov == "2":
            barcha_talabalar()
        elif tanlov == "3":
            ism = input("Qidirilayotgan talaba ismi: ")
            talaba_qidirish(ism)
        elif tanlov == "4":
            ism = input("Talaba ismi: ")
            baho = int(input("Qo'yiladigan baho: "))
            baho_qoshish(ism, baho)
        elif tanlov == "5":
            ism = input("Talaba ismi: ")
            ortacha_baho(ism)
        elif tanlov == "6":
            eng_yuqori_baho_olgan()
        elif tanlov == "0":
            print("Dastur tugatildi.")
            break
        else:
            print("Noto'g'ri tanlov! Qaytadan urinib ko'ring.")

if __name__ == "__main__":
    menu()
