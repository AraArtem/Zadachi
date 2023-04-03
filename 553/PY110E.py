import random
import json
from faker import Faker
from conf import model


fake_ru = Faker(locale="ru_RU")
random_books = {}

def main():
    fields(1)

def fields(count_) -> dict:
    """

    :param count_:
    :return:
    """
    for i in range(count_, 100):
        random_books[i] = {
            "model": model,
            "pk": i,
            "fields": {
                "title": title(),
                "year": years(),
                "pages": pages(),
                "isbn13": isbn(),
                "rating": rating(),
                "price": prices(),
                "author": author()
            }
        }
    with open("result.json", 'w', encoding='utf8') as file:
        json.dump(random_books, file, indent=4, ensure_ascii=False)
    count_ += 1

    return random_books


def title() -> str:
    list_of_the_books = "books.txt"
    with open(list_of_the_books, 'r', encoding='utf8') as file:
        books_list = file.readlines()
        return random.choice(books_list).strip()


def years() -> int:
    return random.randint(1960, 2023)

def pages() -> int:
    return random.randint(100, 2000)

def isbn() -> int:
    """

    :return:
    """
    fake_isbn = fake_ru.isbn13()
    return fake_isbn


def rating() -> str:
    rate = random.uniform(0, 5)
    return f"{rate:.1f}"


def prices() -> str:
    price = random.uniform(100.0, 5000.0)
    return f"{price:.1f}"


def author() -> str:
    list_of_the_authors = "author.txt"
    with open(list_of_the_authors, 'r', encoding='utf8') as f:
        authors_list = f.readlines()
        return random.choice(authors_list).strip()


if __name__ == "__main__":
    main()