from settings import *
import json
from hashlib import md5
# Initializing our database
db = SQLAlchemy(app)


# the class Movie will inherit the db.Model of SQLAlchemy
class User(db.Model):
    __tablename__ = 'user'  # creating a table name
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    name = db.Column(db.String(80), nullable=False)
    # nullable is false so the column can't be empty
    email = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    updated_at = db.Column(db.String(80), nullable=False)

    def set_password(self, password):
        self.password = md5(password.encode('utf-8')).hexdigest()

    def json(self):
        return {'id': self.id, 'name': self.name,
                'email': self.email, 'password': self.password,'creat_at': self.creat_at, 'updated_at':self.updated_at }
        # this method we are defining will convert our output to json

    def sign_up(_name, _email, _password):
        '''function to add user to database using _name, _email, _password
        as parameters'''
        # creating an instance of our Movie constructor
        new_user = User(name=_name, email=_email, password=_password)
        db.session.add(new_user)  # add new user to database session
        db.session.commit()  # commit changes to session

    def get_all_users():
        '''function to get all users in our database'''
        return [User.json(user) for user in User.query.all()]

    def get_user(_id):
        '''function to get user using the id of the user as parameter'''
        return [User.json(User.query.filter_by(id=_id).first())]
        # User.json() coverts our output to json
        # the filter_by method filters the query by the id
        # the .first() method displays the first value

    def sign_in(_email, _password):
        return [User.json(User.query.filter_by(email=_email, password=_password).first())]
        new_user = User(email=_email, password=_password)
        db.session.add(new_user)  # add new user to database session
        db.session.commit()  # commit changes to session

    def update_user(_id, _name, _email, _password):
        '''function to update the details of a user using the id, name,
        email and password as parameters'''
        user_to_update = User.query.filter_by(id=_id).first()
        user_to_update.name = _name
        user_to_update.email = _email
        user_to_update.password = _password
        user_to_update.creat_at = _creat_at
        user_to_update.updated_at = _updated_at
        db.session.commit()

    def delete_user(_id):
        '''function to delete a user from our database using
           the id of the user as a parameter'''
        User.query.filter_by(id=_id).delete()
        # filter by id and delete
        db.session.commit()  # commiting the new change to our database

class Post(db.Model):
    __tablename__ = 'post'  # creating a table name
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    title = db.Column(db.String(80), nullable=False)
    # nullable is false so the column can't be empty
    content = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    update_at = db.Column(db.String(80) ,nullable=False)
    ranking = db.Column(db.String(80),nullable=False)
    view_number = db.Column(db.String(80), nullable=False)


    def json(self):
        return {'id': self.id, 'title': self.title,
                'content': self.content, 'creat_at': self.creat_at, 'update_at': self.update_at, 'ranking': self.ranking, 'view_number': self.view_number}
        # this method we are defining will convert our output to json

    def add_post(_title, _content, _creat_at, _update_at,_ranking, _view_number ):
        '''function to add movie to database using _title, _year, _genre
        as parameters'''
        # creating an instance of our tag constructor
        new_post = Post(title=_title, content=_content,  creat_at=_creat_at, update_at=_update_at, ranking=_ranking, view_number=_view_number )
        db.session.add(new_post)  # add new post to database session
        db.session.commit()  # commit changes to session
    def get_all_post():
        '''function to get all users in our database'''
        return [Post.json(post) for post in Post.query.all()]

    def get_post(_id):
        '''function to get user using the id of the user as parameter'''
        return [Post.json(Post.query.filter_by(id=_id).first())]
        # Post.json() coverts our output to json
        # the filter_by method filters the query by the id
        # the .first() method displays the first value

    def update_post(_id, _title, _content, _creat_at, _update_at, _ranking, _view_number  ):
        '''function to update the details of a user using the id, name,
        email and password as parameters'''
        post_to_update = Post.query.filter_by(id=_id).first()
        post_to_update.title = _title
        post_to_update.content = _content
        post_to_update.creat_at = _creat_at
        post_to_update.update_at = _update_at
        post_to_update.ranking = _ranking
        post_to_update.view_number = _view_number
        db.session.commit()

    def delete_post(_id):
        '''function to delete a user from our database using
           the id of the user as a parameter'''
        Post.query.filter_by(id=_id).delete()
        # filter by id and delete
        db.session.commit()  # commiting the new change to our database

class Tag(db.Model):
    __tablename__ = 'tag'  # creating a table name
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    name = db.Column(db.String(80), nullable=False)
    # nullable is false so the column can't be empty
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    category = db.Column(db.String(80), nullable=False)
    label = db.Column(db.String(80), nullable=False)

    def json(self):
        return {'id': self.id, 'name': self.name,
                'creat_at': self.creat_at, 'category': self.category, 'label': self.label}
        # this method we are defining will convert our output to json

    def add_tag(_name, _creat_at, _category, _label):
        '''function to add movie to database using _title, _year, _genre
        as parameters'''
        # creating an instance of our tag constructor
        new_tag = Tag(name=_name, creat_at=_creat_at, category=_category, label=_label )
        db.session.add(new_tag)  # add new movie to database session
        db.session.commit()  # commit changes to session

    def get_all_tag():
        '''function to get all users in our database'''
        return [User.json(tag) for tag in User.query.all()]

    def get_tag(_id):
        '''function to get user using the id of the user as parameter'''
        return [Tag.json(Tag.query.filter_by(id=_id).first())]
        # Tag.json() coverts our output to json
        # the filter_by method filters the query by the id
        # the .first() method displays the first value

    def update_tag(_id, _name,  _creat_at, _category, _label):
        '''function to update the details of a user using the id, name,
        email and password as parameters'''
        tag_to_update = User.query.filter_by(id=_id).first()
        tag_to_update.name = _name
        tag_to_update.creat_at = _creat_at
        tag_to_update.category = _category
        tag_to_update.label = _label
        db.session.commit()

    def delete_tag(_id):
        '''function to delete a user from our database using
           the id of the user as a parameter'''
        Tag.query.filter_by(id=_id).delete()
        # filter by id and delete
        db.session.commit()  # commiting the new change to our database

