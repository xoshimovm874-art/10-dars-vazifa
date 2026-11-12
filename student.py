import json

FILENAME = "students.json"

def talaba_qoshish(ism):
    try:
        with open(FILENAME, "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}
    
    if ism not in data:
        data[ism] = []  # Bo'sh baholar ro'yxati bilan qo'shamiz
        with open(FILENAME, "w") as f:
            json.dump(data, f, indent=4)
        print(f"{"ism"} muvaffaqiyatli qo'shildi!")
    else:
        print("Bu talaba allaqachon mavjud!")

def barcha_talabalar():
    try:
        with open(FILENAME, "r") as f:
            data = json.load(f)
        print("\n--- BARCHA TALABALAR ---")
        for ism in data:
            print(f"- {ism}")
    except (FileNotFoundError, json.JSONDecodeError):
        print("Hozircha talabalar ro'yxati bo'sh.")

def talaba_qidirish(ism):
    try:
        with open(FILENAME, "r") as f:
            data = json.load(f)
            
        for talaba in data:
            if talaba["name"].lower() ==ism.lower():
                print(f"Topildi: {ism}, Baholari: {talaba["grades"]}")
                break
        else:
            print(f"'{ism}' topilmadi.")
    except FileNotFoundError:
        print("Ma'lumotlar bazasi topilmadi.")