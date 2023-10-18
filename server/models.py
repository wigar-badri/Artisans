from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

# --- USER --- #

class User(db.Model, SerializerMixin):
    # TABLE #
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    # RELATIONSHIPS/PROXY #
    liked_books = db.relationship('LikedBook', back_populates='user')
    books = association_proxy('liked_books', 'book')

    liked_foods = db.relationship('LikedFood', back_populates='user')
    foods = association_proxy('liked_foods', 'food')

    liked_gifts = db.relationship('LikedGift', back_populates='user')
    gifts = association_proxy('liked_gifts', 'gift')

    tickets = db.relationship('Ticket', back_populates='user')
    events = association_proxy('tickets', 'event')

    # SERIALIZE RULES #
    serialize_rules = ('-liked_books.user',)
    serialize_rules = ('-liked_foods.user',)
    serialize_rules = ('-liked_gifts.user',)
    serialize_rules = ('-tickets.user',)

# --- BOOK --- #
class Book(db.Model, SerializerMixin):
    # TABLE #
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String)
    description = db.Column(db.String)
    price = db.Column(db.Integer, nullable=False)

    # RELATIONSHIPS/PROXY #
    liked_books = db.relationship('LikedBook', back_populates='book')
    users = association_proxy('liked_books', 'user')

    # SERIALIZE RULES #
    serialize_rules = ('-liked_books.book',)

# --- LIKED-BOOKS --- #
class LikedBook(db.Model, SerializerMixin):
    # TABLE #
    __tablename__ = 'liked_books'

    id = db.Column(db.Integer, primary_key=True)

    # FOREIGN KEYS #
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'))

    # RELATIONSHIPS #
    user = db.relationship('User', back_populates='liked_books')
    book = db.relationship('Book', back_populates='liked_books')

    # SERIALIZE RULES #
    serialize_rules = ('-book.liked_books', '-user.liked_books')

# # --- FOOD --- #
class Food(db.Model, SerializerMixin):
    # TABLE #
    __tablename__ = 'foods'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    price = db.Column(db.Integer, nullable=False)

    # RELATIONSHIPS/PROXY #
    liked_foods = db.relationship('LikedFood', back_populates = 'food')
    users = association_proxy('liked_foods', 'user')

    # SERIALIZE RULES #
    serialize_rules = ('-liked_foods.food',)

# --- LIKED-FOODS --- #
class LikedFood(db.Model, SerializerMixin):
    # TABLE #
    __tablename__ = 'liked_foods'

    id = db.Column(db.Integer, primary_key=True)

    # FOREIGN KEYS #
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    food_id = db.Column(db.Integer, db.ForeignKey('foods.id'))

    # RELATIONSHIP #
    user = db.relationship('User', back_populates ='liked_foods')
    food = db.relationship('Food', back_populates='liked_foods')

    # SERIALIZE RULES #
    serialize_rules = ('-food.liked_foods', '-user.liked_foods')

# # --- GIFT --- #
class Gift(db.Model, SerializerMixin):
    # TABLE #
    __tablename__ = 'gifts'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    price = db.Column(db.Integer, nullable=False)

    # RELATIONSHIP #
    liked_gifts = db.relationship('LikedGift', back_populates = 'gift')
    users = association_proxy('liked_gifts', 'user')

    # SERIALIZE RULES #
    serialize_rules = ('-liked_gifts.gift',)


# # --- LIKED-GIFT --- #
class LikedGift(db.Model, SerializerMixin):
    # TABLE #
    __tablename__ = 'liked_gifts'

    id = db.Column(db.Integer, primary_key=True)

    # FOREIGN KEYS #
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    gift_id = db.Column(db.Integer, db.ForeignKey('gifts.id'))

    # RELATIONSHIP #
    user = db.relationship('User', back_populates ='liked_gifts')
    gift = db.relationship('Gift', back_populates='liked_gifts')

    # SERIALIZE RULES #
    serialize_rules = ('-gift.liked_gifts', '-user.liked_gifts')

# # --- EVENT --- #
class Event(db.Model, SerializerMixin):
    # TABLE #
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    date = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    price = db.Column(db.Integer, nullable=False)
    available_tickets= db.Column(db.Integer, nullable=False)

    # RELATIONSHIP #
    tickets = db.relationship('Ticket', back_populates = 'event')
    users = association_proxy('tickets', 'user')

    # SERIALIZE RULES #
    serialize_rules = ('-tickets.event',)

# # --- TICKET --- #
class Ticket(db.Model, SerializerMixin):
    # TABLE #
    __tablename__ = 'tickets'

    id = db.Column(db.Integer, primary_key=True)

    # FOREIGN KEYS #
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))

    # RELATIONSHIP #
    user = db.relationship('User', back_populates ='tickets')
    event = db.relationship('Event', back_populates='tickets')

    # SERIALIZE RULES #
    serialize_rules = ('-event.tickets', '-user.tickets')

