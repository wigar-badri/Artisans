import random
from app import app
from faker import Faker
from faker_food import FoodProvider
from models import db, User, Book, Food, Gift, Event

fake = Faker()
fake.add_provider(FoodProvider)

def create_users(rows):
    users = []
    for _ in range(rows):
        user = User(
            username = fake.email(),
            password = fake.address(),
            name = fake.name(),
        )
        users.append(user)
    return users


def create_books(rows):
    books = []
    book_names = [
    "Book 1", "Book 2", "Book 3", "Book 4", "Book 5",
    "Book 6", "Book 7", "Book 8", "Book 9", "Book 10"
    ]
    for _ in range(rows):
        # Randomly select a book name from the list
        title = random.choice(book_names)
        author = fake.name()  # You can modify this if you want to generate random authors as well
        book = Book(
            image='https://as2.ftcdn.net/v2/jpg/01/66/55/01/1000_F_166550191_hEVqAvFjIbRMZNDTaBoi0j7fX7ynPS5x.jpg',
            title=title,
            author=author,
            price=random.randint(1, 30)
        )
        books.append(book)

    return books

def create_foods(rows):
    foods = []
    for _ in range(rows):
        food = Food(
            name=fake.dish(),
            price = random.randint(1, 30)
        )
        foods.append(food)
    return foods

def create_gifts(rows):
    gifts = []
    for _ in range(rows):
        gift = Gift(
            name=fake.name(),
            price = random.randint(1, 30)
        )
        gifts.append(gift)
    return gifts

def create_events(rows):
    events = []
    for _ in range(rows):
        event = Event(
            name=fake.name(),
            date=fake.date_this_decade(),
            price = random.randint(1, 30),
            available_tickets=random.randint(1, 30)
        )
        events.append(event)
    return events


if __name__ == '__main__':

    with app.app_context():

        # Clearing database
        print('Clearing database...')
        Book.query.delete()
        Food.query.delete()
        Gift.query.delete()
        Event.query.delete()
        User.query.delete()


        print('Seeding users ...')
        users = create_users(10)
        db.session.add_all(users)
        db.session.commit()

        print('Seeding books ...')
        books = create_books(10)
        db.session.add_all(books)
        db.session.commit()

        print('Seeding events ...')
        events = create_events(5)
        db.session.add_all(events)
        db.session.commit()

        print('Seeding foods ...')
        foods = create_foods(10)
        db.session.add_all(foods)
        db.session.commit()

        print('Seeding gifts ...')
        gifts = create_gifts(10)
        db.session.add_all(gifts)
        db.session.commit()

        print('Done seeding !!!')
