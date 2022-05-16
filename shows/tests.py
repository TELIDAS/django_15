from datetime import datetime, date
from unittest import TestCase
from . import models, forms


class TestModel(TestCase):
    def test_create_model_shows_success(self):
        pass

    def test_create_model_fail(self):
        pass

    def test_update_model(self):
        pass

    def test_delete_model(self):
        pass


class TestForms(TestCase):
    """
    Testing film forms
    """

    def test_shows_form_success(self):
        payload = {
            "title": 'title',
            "description": "descrip",
            "image": "game.jpeg",
            "quantity": 12,
            "genre": "Anime",
            "created_date": date.today(),
            "updated_date": date.today(),
            "duration": 12,
        }
        data = {**payload}
        print(data)
        form = forms.TVShowForm(data=payload)
        with self.assertRaises(ValueError):
            form.save()
