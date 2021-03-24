from application import app
from flask import render_template, request, redirect, url_for, flash
from application.models import Game, User
from application.form import UserForm, GameForm
from application import db
from flask_login import login_user
from flask_bcrypt import Bcrypt


@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route('/Games', methods=['GET', 'POST'])
def games_page():
    error = ""
    form = GameForm()
    if request.method =='POST':
        game = Game(game_title=form.game_title.data)
        owner = Game(owner=form.owner.data)
        db.session.add(game)
        db.session.commit()
    return render_template("games.html", form=form)

@app.route("/MyGames")
def MyGame_page():
    all_games = Game.query.all()
    games_string = ""
    for game in all_games:
        games_string += " "+ game.game_title
    return render_template("My_Games.html", game_string=games_string)


@app.route('/update/<name>')
def update(name):
    first_game = Game.query.first()
    first_game.game_title = name
    db.session.commit()
    return first_game.game_title


@app.route("/delete/<name>")
def delete(name):
    first_game_delete = Game.query.first()
    db.session.delete(first_game_delete)
    db.session.commit()
    return render_template("My_Games.html")


#@app.route("/Register", methods=["GET", "POST"])
#def register_page():
 #   form = RegisterForm()
  #  if form.validate_on_submit():
   #     user_to_create = User(first_name=form.first_name.data,
    #                          last_name=form.last_name.data,
     #                         email=form.email.data,
      #                        password=form.password1.data)
       # db.session.add(user_to_create)
        #db.session.commit()
       # return redirect(url_for("games_page"))
   # if form.errors !={}:
    #    for err_msg in form.errors.values():
     #       flash(f'There was an error Registering: {err_msg}', category="danger")

    #return render_template("register.html", form=form)

#@app.route("/login", methods=["GET","POST"])
#def login_page():
 #   form = LoginForm()
  #  if form.validate_on_submit():
   #     attempted_user = User.query.filter_by(email=form.email.data).first()
    #    if attempted_user and attempted_user.check_password_correction(
     #       attempted_password=form.password.data
      #      ):
       #     login_user(attempted_user)
        #    flash(f"You have Successfuly Logged in {attempted_user.first_name}", category="success")
         #   return redirect(url_for("games_page"))
        #else:
         #   flash("Email and Password did not match! try again", category="danger")

    #return render_template("login.html", form=form)