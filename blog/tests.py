from datetime import date
from . import models
from django.test import TestCase


class TestModel(TestCase):

    def test_create_model_post_success(self):
        payload = {
            'title': 'Test Title',
            'description': 'Test Description',
            'created_date': date.today(),
            'updated_date': date.today(),
            'count_post': 12,
            'image': 'game.jpeg'
        }
        post = models.Post.objects.create(**payload)
        self.assertEqual(post.title, payload['title'])
        self.assertEqual(post.description, payload['description'])
        self.assertEqual(post.created_date, payload['created_date'])

    def test_create_model_post_fail(self):
        payload = {
            'title': 'Test Title',
            'description': 'Test Description',
            'created_date': 'today',
            'updated_date': date.today(),
            'count_post': 'twelve',
            'image': 'game.jpeg'
        }
        with self.assertRaises(ValueError):
            post = models.Post.objects.create(**payload)

    def test_update_model_post(self):
        payload = {
            'title': 'Test Title',
            'description': 'Test Description',
            'created_date': date.today(),
            'updated_date': date.today(),
            'count_post': 12,
            'image': 'game.jpeg'
        }
        new_title = 'New Title'
        post = models.Post.objects.create(**payload)
        post.title = new_title
        print(post.title)
        post.save()
        post.refresh_from_db()
        self.assertEqual(post.title, new_title)

    def test_delete_model_post(self):
        payload = {
            'title': 'Test Title',
            'description': 'Test Description',
            'created_date': date.today(),
            'updated_date': date.today(),
            'count_post': 12,
            'image': 'game.jpeg'
        }
        post = models.Post.objects.create(**payload)
        pk = post.pk
        print(pk)
        post.delete()
        with self.assertRaises(models.Post.DoesNotExist):
            models.Post.objects.get(pk=pk)
