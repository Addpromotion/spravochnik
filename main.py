import csv
import os

SPRAVOCHNIK_FILE = "spravochnik.csv"
spravochnik = []

def create_spravochnik_if_not_exists():
    if not os.path.exists(SPRAVOCHNIK_FILE):
        with open(SPRAVOCHNIK_FILE, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Имя", "Фамилия", "Род занятий", "Номер телефона"])
        print("Создан новый файл справочника.")

def open_spravochnik():
    try:
        with open(SPRAVOCHNIK_FILE, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                print(', '.join(row))
    except FileNotFoundError:
        print("Справочник не найден.")

def save_contact_to_spravochnik(contact):
    with open(SPRAVOCHNIK_FILE, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(contact)
    print("Контакт успешно сохранен в справочнике.")

def create_contact():
    name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")
    occupation = input("Введите род занятий: ")
    phone = input("Введите номер телефона: ")
    contact = [name, last_name, occupation, phone]
    spravochnik.append(contact)
    save_contact_to_spravochnik(contact)

def main():
    create_spravochnik_if_not_exists()
    while True:
        print("\nМеню:")
        print("1. Открыть справочник")
        print("2. Создать контакт")
        print("3. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            open_spravochnik()
        elif choice == '2':
            create_contact()
        elif choice == '3':
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")

if __name__ == "__main__":
    main()
