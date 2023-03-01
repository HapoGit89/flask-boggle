from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle
from app import show_start
import json


class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!

    def test_show_start(self):
        with app.test_client() as client:
            self.assertIn("<h1>Welcome, this is Boggle!</h1>", str(str(client.get('/').data)))
            self.assertEquals(200, (client.get('/').status_code ))

    def test_start_game(self):
        with app.test_client() as client:
            res = client.get('/game')
            self.assertEquals(session['words'], [])
            self.assertEquals(session['num_of_game'], 0)
            self.assertEquals(session['high_score'], 0)
            self.assertIsInstance(session['board'], list)
            self.assertIsInstance(session['board'][0], list)
            self.assertIsInstance(session['board'][0][0], str)

    def test_new_game(self):
        with app.test_client() as client:
            res1 = client.get('/game')
            res = client.get('/newgame')
            self.assertIsInstance(session['board'], list)
            self.assertIsInstance(session['board'][0], list)
            self.assertIsInstance(session['board'][0][0], str)
            self.assertIn(""" <p id="numGames">No of Games Played: 0</p>""", str(res.data))

    # def test_guess_validation(self):
    #     with app.test_client() as client:
    #         res = client.get('/game')
    #         res1 = client.post('/guess',  data=json.dumps(dict(guess= 'test')))
    #         self.assertIn(("ok" or "not-word" or "not-on-board"), str(res1.data))


    # def test_game_end(self):
    #      with app.test_client() as client:
    #         res = client.post('/gameend',  data=json.dumps(dict(score= 10)))
    #         self.assertIn(""" <p id="highscore">Highscore: 10</p>""", str(res.data))

    def test_check_valid_word(self):
        """ also checks find() and find_from() becaus check_valid_word needs them to work"""
        test_boggle = Boggle()
        self.assertIn(test_boggle.check_valid_word(test_boggle.make_board(), "test"), "ok not-word not-on-board")

    def test_read(self):
        test_boggle = Boggle()
        self.assertIn("Aaronite", test_boggle.read_dict("words.txt"))
        self.assertIn("rapiner", test_boggle.read_dict("words.txt"))

    


