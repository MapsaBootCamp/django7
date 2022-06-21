from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth import get_user_model

from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework.test import APITestCase

from app.models import Author, Book
from app.views import AuthorBookListView

User = get_user_model()

class TestApi(APITestCase):

    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        self.user = User.objects.create(username="A")
        self.user.set_password("1234")
        self.user.save()
        self.author = Author.objects.create(name="A", 
                                        birth_year="1995-02-12")
        self.book = Book.objects.create(author=self.author, name="b_A", page=430)
    

    def test_api(self):
        response = self.client.get("/", follow=True)
        self.assertContains(response=response, text="Khosh Amadi")

    def test_authentication_get_authors_with_books(self):
        
        request = self.factory.get("/api/library/authors/")
        view = AuthorBookListView.as_view()

        response = view(request)
        # check authentication required
        self.assertEqual(response.status_code, 403)
        
        force_authenticate(request, user=self.user)
        response = view(request)
        self.assertEqual(response.status_code, 200)
    
    def test_get_authors_with_book(self):
        self.client.login(username="A", password="1234")
        response = self.client.get("/api/library/authors/")
        data = response.data[0]
        self.assertIn("books", data.keys())
        self.assertContains(response, text="author")