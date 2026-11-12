from student import load_data, save_data

def baho_qoshish(ism, baho):
    if not isinstance(baho, int) or isinstance(baho, bool) or not 1 <= baho <= 5:
        print("Baho 1 dan 5 gacha bo'lgan butun son bo'lishi kerak.")
        return

    ism = ism.strip().casefold()
    data = load_data()
    for talaba in data:
        if talaba["name"].casefold() == ism:
            talaba["grades"].append(baho)
            save_data(data)
            print(f"'{talaba['name']}'ga {baho} baho qo'shildi.")
            return

    print("Bunday talaba mavjud emas.")

def ortacha_baho(ism):
    ism = ism.strip().casefold()
    for talaba in load_data():
        if talaba["name"].casefold() == ism:
            baholar = talaba["grades"]
            if not baholar:
                print(f"{talaba['name']} uchun hali baho kiritilmagan.")
                return

            orta = sum(baholar) / len(baholar)
            print(f"{talaba['name']}ning o'rtacha bahosi: {orta:.2f}")
            return orta

    print("Talaba topilmadi.")

def eng_yuqori_baho_olgan():
    data = load_data()
    if not data:
        print("Talabalar yo'q.")
        return

    bahosi_borlar = [talaba for talaba in data if talaba["grades"]]
    if not bahosi_borlar:
        print("Hali hech kimga baho qo'yilmagan.")
        return

    eng_zor = max(
        bahosi_borlar,
        key=lambda talaba: sum(talaba["grades"]) / len(talaba["grades"]),
    )
    max_orta = sum(eng_zor["grades"]) / len(eng_zor["grades"])
    print(
        f"Eng yuqori o'rtacha baho egasi: {eng_zor['name']} "
        f"(O'rtacha: {max_orta:.2f})"
    )
