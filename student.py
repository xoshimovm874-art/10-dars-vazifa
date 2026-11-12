import json
from pathlib import Path

FILENAME = Path(__file__).with_name("students.json")


def load_data():
    try:
        with FILENAME.open("r", encoding="utf-8") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

    if isinstance(data, dict):
        return [
            {"name": name, "grades": grades if isinstance(grades, list) else []}
            for name, grades in data.items()
        ]
    return data if isinstance(data, list) else []


def save_data(data):
    with FILENAME.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def talaba_qoshish(ism):
    ism = ism.strip()
    if not ism:
        print("Talaba ismi bo'sh bo'lmasligi kerak.")
        return

    data = load_data()
    if any(talaba["name"].casefold() == ism.casefold() for talaba in data):
        print("Bu talaba allaqachon mavjud!")
        return

    data.append({"name": ism, "grades": []})
    save_data(data)
    print(f"{ism} muvaffaqiyatli qo'shildi!")


def barcha_talabalar():
    data = load_data()
    if not data:
        print("Hozircha talabalar ro'yxati bo'sh.")
        return

    print("\n--- BARCHA TALABALAR ---")
    for raqam, talaba in enumerate(data, start=1):
        print(f"{raqam}. {talaba['name']} | Baholari: {talaba['grades']}")


def talaba_qidirish(ism):
    ism = ism.strip().casefold()
    for talaba in load_data():
        if talaba["name"].casefold() == ism:
            print(f"Topildi: {talaba['name']}, Baholari: {talaba['grades']}")
            return

    print(f"'{ism}' topilmadi.")
