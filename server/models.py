from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

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

    # RELATIONSHIP #

    # SERIALIZER #

# --- BOOK --- #
class Book(db.Model, SerializerMixin):
    # TABLE #
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String)
    description = db.Column(db.String)
    price = db.Column(db.Integer, nullable=False)

# --- CARTEDBOOKS --- #
class CartedBook(db.Model, SerializerMixin):
    # TABLE #
    __tablename__ = 'cartedbooks'

    id = db.Column(db.Integer, primary_key=True)

    # RELATIONSHIP #
    # user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)

# --- FOOD --- #
class Food(db.Model, SerializerMixin):
    # TABLE #
    __tablename__ = 'foods'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    price = db.Column(db.Integer, nullable=False)


# --- CARTEDFOODS --- #
class CartedFood(db.Model, SerializerMixin):
    # TABLE #
    __tablename__ = 'cartedfoods'

    id = db.Column(db.Integer, primary_key=True)

    # RELATIONSHIP #
    # user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

# --- GIFT --- #
class Gift(db.Model, SerializerMixin):
    # TABLE #
    __tablename__ = 'gifts'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    price = db.Column(db.Integer, nullable=False)


# --- CARTEDGIFT --- #
class CartedGift(db.Model, SerializerMixin):
    # TABLE #
    __tablename__ = 'cartedgifts'

    id = db.Column(db.Integer, primary_key=True)

    # RELATIONSHIP #
    # user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

# --- EVENT --- #
class Event(db.Model, SerializerMixin):
    # TABLE #
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    date = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    price = db.Column(db.Integer, nullable=False)
    ticketsnum = db.Column(db.Integer, nullable=False)

# --- TICKET --- #
class Ticket(db.Model, SerializerMixin):
    # TABLE #
    __tablename__ = 'tickets'

    id = db.Column(db.Integer, primary_key=True)

    # RELATIONSHIP #
    # user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

