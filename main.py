import json
import os

BOOKS_FILE = "books.json"

def load_books():
    if not os.path.exists(BOOKS_FILE):
        return []
    with open(BOOKS_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_books(books):
    with open(BOOKS_FILE, "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=2)

def add_book(books):
    pass

def list_books(books):
    if not books:
        print("Список книг пуст")
        return
    for i, b in enumerate(books, 1):
        print(f"{i}. {b['author']} - {b['title']} "
              f"(оценка: {b['rating']}, прочитано: {b['date']})")

def average_rating(books):
    if not books:
        print("Нет книг для расчёта")
        return
    avg = sum(b["rating"] for b in books) / len(books)
    print(f"Средняя оценка: {avg:.2f}")

def author_stats(books):
    if not books:
        print("Нет данных")
        return
    stats = {}
    for b in books:
        stats[b["author"]] = stats.get(b["author"], 0) + 1
    print("Статистика по авторам:")
    for author, count in sorted(stats.items()):
        print(f"  {author}: {count}")

def delete_book(books):
    pass

def main():
    books = load_books()
    while True:
        print("\n=== Трекер прочитанных книг ===")
        print("1. Добавить книгу")
        print("2. Показать все книги")
        print("3. Показать среднюю оценку")
        print("4. Статистика по авторам")
        print("5. Удалить книгу")
        print("6. Выход")
        choice = input("Выберите пункт: ").strip()
        if choice == "1":
            add_book(books)
        elif choice == "2":
            list_books(books)
        elif choice == "3":
            average_rating(books)
        elif choice == "4":
            author_stats(books)
        elif choice == "5":
            delete_book(books)
        elif choice == "6":
            print("До свидания!")
            break
        else:
            print("Неверный пункт меню, попробуйте снова")

if __name__ == "__main__":
    main()