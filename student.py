import json

FILE_NAME = "students.json"

def load_data():
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)

def add_student(name):
    students = load_data()
    students.append({"name": name, "grades": []})
    save_data(students)
    print(f"'{name}' muvaffaqiyatli qo'shildi!")

def list_students():
    students = load_data()
    if not students:
        print("Talabalar mavjud emas.")
        return
    for i, s in enumerate(students, 1):
        print(f"{i}. Ism: {s['name']} | Baholar: {s['grades']}")

def search_student(name):
    students = load_data()
    found = [s for s in students if name.lower() in s['name'].lower()]
    if found:
        for s in found:
            print(f"Topildi: {s['name']} | Baholar: {s['grades']}")
    else:
        print("Bunday talaba topilmadi.")