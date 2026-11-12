import json

FILENAME = "students.json"

def baho_qoshish(ism, baho):
    try:
        with open(FILENAME, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Baza topilmadi.")
        return

    if ism in data:
        data[ism].append(baho)
        with open(FILENAME, "w") as f:
            json.dump(data, f, indent=4)
        print(f"'{ism}'ga {baho} baho qo'shildi.")
    else:
        print("Bunday talaba mavjud emas.")

def ortacha_baho(ism):
    try:
        with open(FILENAME, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        return 0

    if ism in data and data[ism]:
        orta = sum(data[ism]) / len(data[ism])
        print(f"{ism}ning o'rtacha bahosi: {orta}")
    else:
        print("Talaba topilmadi yoki baholari yo'q.")

def eng_yuqori_baho_olgan():
    try:
        with open(FILENAME, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Baza bo'sh.")
        return

    if not data:
        print("Talabalar yo'q.")
        return

    eng_zor = None
    max_orta = -1

    for ism, baholar in data.items():
        if baholar:
            orta = sum(baholar) / len(baholar)
            if orta > max_orta:
                max_orta = orta
                eng_zor = ism

    if eng_zor:
        print(f"Eng yuqori o'rtacha baho egasi: {eng_zor} (O'rtacha: {max_orta})")
    else:
        print("Hali hech kimga baho qo'yilmagan.")
