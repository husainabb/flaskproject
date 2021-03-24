from application import db, login_manager
from application import bcrypt
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    game = db.relationship("Game", backref="owned_user", lazy=True)

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_title = db.Column(db.String(30), nullable=False)
    owner = db.Column(db.Integer, db.ForeignKey("user.id"))
  
  
  
   # @property
   # def password(self):
    #    return self.password
    
    #@password.setter
    #def password(self, passwords):
     #   self.password_hash = bcrypt.generate_password_hash(passwords).decode('utf-8')

    #def check_password_correction(self, attempted_password):
     #   return bcrypt.check_password_hash(self.password_hash, attempted_password)
          
    

