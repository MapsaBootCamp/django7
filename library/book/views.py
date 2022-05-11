from email.headerregistry import ContentDispositionHeader
import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.forms.models import model_to_dict
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from matplotlib.pyplot import title

from .models import Book, Category


def index(request):
    cat_qs = Category.objects.all()
    return render(request, "book/index.html", {"categories": cat_qs})

def book_list(request):
    book_qs = Book.objects.all()
    return render(request, "book/book_list.html", {"books": book_qs})


@method_decorator(csrf_exempt, name='dispatch')
class BookList(View):
    
    # @csrf_exempt
    # def dispatch(self, request, *args, **kwargs):
    #     return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        book_list = list(Book.objects.values("title", "available_qty"))
        return JsonResponse(book_list, safe=False)
    
    def post(self, request):
        """
        یک کار خطرناک داریم میکنیم. داریم به کاربر اعتماد میکنیم و تایپ دیتاهای ارسالی توسط آن شلغم را چک نمیکنیم.
        دیفالت این است که همه کاربران گرگ ان مگر اینکه هم نداریم.
        """
        data = json.loads(request.body)
        title = data.get("title")
        category = get_object_or_404(Category, name=data.get("category"))
        author1 = data.get("author1")
        publisher = data.get("publisher")
        translated = data.get("translated")
        qty = data.get("qty")
        Book.objects.create(title=title, category=category, translated=translated, author1=author1, publisher=publisher, qty=qty)
        return JsonResponse({"status": "ba moafaghiat ijad shod"})

  
class BookDetail(View):

    def get(self, request, id):
        book_obj: Book = get_object_or_404(Book, id=id)
        return JsonResponse(model_to_dict(book_obj))
