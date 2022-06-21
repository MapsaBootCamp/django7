from django.test import TestCase
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

from app.models import FollowerTable, FollowerUser, Author, Book

User = get_user_model()


class LibraryTest(TestCase):

    def setUp(self) -> None:
        self.author = Author.objects.create(name="A", 
                                        birth_year="1995-02-12")
        self.book = Book.objects.create(author=self.author, name="b_A", page=430)
    
    def test_get_age_author(self):
        self.assertEqual(self.author.get_age(), 27)

    def test_get_authors_books(self):
        self.assertEqual(len(self.author.books.all()), 1)

class FollowerModelTest(TestCase):
    
    def setUp(self) -> None:
        self.user1 = User.objects.create(username="A")
        self.user2 = User.objects.create(username="B")
        follower_table_obj = FollowerTable.objects.create(user=self.user1)
        self.follower_table_obj = follower_table_obj
        FollowerUser.objects.create(follower=follower_table_obj, user=self.user2, status="a")

    def test_model_fields(self):
        follower_fields = FollowerTable._meta.get_fields()
        model_field_name_list = []
        for item in follower_fields:
            if not isinstance(item, models.ManyToOneRel):
                model_field_name_list.append(item.verbose_name)
        assert "user" in model_field_name_list
    
    def test_get_user_follower_numbers(self):
        self.assertEqual(self.follower_table_obj.get_follower_numbers(), 1)

class FollowerUserTest(TestCase):

    def test_model_choice_field(self):
        max_length_status = FollowerUser._meta.get_field("status").max_length
        self.assertEqual(max_length_status, 1)