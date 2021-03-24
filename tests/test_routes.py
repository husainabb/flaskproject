from flask import url_for, Flask, redirect, render_template, request
from flask_testing import TestCase
from application import db
from application.models import User, Game
from flask_sqlalchemy import SQLAlchemy
from app import app
from wtforms import StringField, SubmitField


class TestBase(TestCase):
    def create_app(self):

        # Pass in testing configurations for the app. Here we use sqlite without a persistent database for our tests.
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        # Create table
        db.create_all()

        # Create test registree
        sample1 = Game(game_title="Valheim")

        # save users to database
        db.session.add(sample1)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()

class TestViews(TestBase):

    def test_home_get(self):
        response = self.client.get(url_for('home_page'))
        self.assertEqual(response.status_code, 200)

class TestAddGame(TestBase):
    def test_game(self):
        response = self.client.get(url_for('games_page'))
        self.assertEqual(response.status_code, 200)
             
class TestAddGame(TestBase):
    def test_add_game(self):
        response = self.client.post(url_for('games_page'),
        data = dict(game_title="Valheim"),
        follow_redirects=True)
        self.assertIn(b"Valheim", response.data)   

class TestReadGame(TestBase):
    def test_read_game(self):
        response = self.client.get(url_for('MyGame_page'))
        self.assertEqual(response.status_code, 200) 

 
         