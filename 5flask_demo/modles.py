from extend import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(12), nullable=True, unique=True)
    telnumber = db.Column(db.Integer, nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    vip = db.Column(db.BOOLEAN, default=False)
    isdelate = db.Column(db.BOOLEAN, default=False)
    logintime = db.Column(db.DateTime, nullable=True)

#
# categorys = db.Table('categorys',
#     db.Column('category_id', db.Integer, db.ForeignKey('category.id')),
#     db.Column('category_id', db.Integer, db.ForeignKey('category.id'))
# )


class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    fatherc_id = db.Column(db.Integer, db.ForeignKey('fatherc.id'))

    fatherc = db.relationship('Fatherc', backref=db.backref('categorys'))


class Fatherc(db.Model):
    __tablename__ = 'fatherc'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)


class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    need_vip = db.Column(db.BOOLEAN, default=False)
    introduce = db.Column(db.Text, nullable=True)
    book_image = db.Column(db.String(50), nullable=True)
    isdelate = db.Column(db.BOOLEAN, default=False)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    category = db.relationship('Category', backref=db.backref('books'))


class Chapter(db.Model):
    __tablename__ = 'chapter'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    need_vip = db.Column(db.BOOLEAN, default=False)

    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))

    book = db.relationship('Book', backref=db.backref('chapters'))



#
# class Artical(db.Model):
#     __tablename__ = 'articals'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     name = db.Column(db.String(50), nullable=False)
#     content = db.Column(db.text, nullable=False)
#
#
# class Comment(db.Model):
#     __tablename__ = 'comments'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     name = db.Column(db.String(50), nullable=False)
#     content = db.Column(db.text, nullable=False)


category_book = db.Table('category_book',
                         db.Column('category_id', db.Integer, db.ForeignKey('category.id'), primary_key=True),
                         db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key=True),)


category_chapter = db.Table('category_chapter',
                            db.Column('category_id', db.Integer, db.ForeignKey('category.id'), primary_key=True),
                            db.Column('chapter_id', db.Integer, db.ForeignKey('chapter.id'), primary_key=True))


