import json

from django.http import Http404, HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.views import View
from django.forms.models import model_to_dict
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, FormView, DeleteView, DetailView
from django.contrib.auth.decorators import login_required

from .models import Book, Category, Comment
from .forms import CommentForm

def add_comment(request, book_id):
    if request.method == "POST":    
        comment_form = CommentForm(request.POST)
        book = get_object_or_404(Book, id=book_id)
        if comment_form.is_valid():
            Comment.objects.create(book=book, **comment_form.cleaned_data)
            return redirect(reverse('book_detail_template', kwargs={'id': book.id}))
        else:
            ## TODO: in hal beham zan ro dorost KOOOOON.
            comments = book.comments.all()
            context = {
                "book": book, 
                "comments": comments,
                "comment_form": comment_form
                }
            return render(request, "book/book_detail.html", context)
    else:
        return HttpResponse(status=400)


def index(request):
    print("session:",request.session.get("name"))
    cat_qs = Category.objects.all()
    return render(request, "book/index.html", {"categories": cat_qs})


@login_required(login_url="/user/login/")
def book_list(request: HttpRequest):
    ## TODO: handle SQL ingection
    request.session["name"] = "Gholam"
    q = request.GET.get("search")
    book_qs = Book.objects.all()
    if q:
        book_qs = book_qs.filter(title__contains=q)
    return render(request, "book/book_list.html", {"books": book_qs})


class BookListV1(ListView):
    model = Book
    template_name: str =  "book/book_list.html"
    context_object_name = "books"
    paginate_by = 2


    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get("search")
        if q:
            qs = qs.filter(title__contains=q)
        return qs


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


def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    comments = book.comments.all()
    comment_form = CommentForm()
    context = {
        "book": book, 
        "comments": comments,
        "comment_form": comment_form
        }
    return render(request, "book/book_detail.html", context)


class BookDetailV2(DetailView):
    model = Book
    template_name: str = "book/book_detail.html"
    context_object_name = "book"
    pk_url_kwarg = "id"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comments = self.get_object().comments.all()
        comment_form = CommentForm()
        context["comments"]  = comments
        context["comment_form"] = comment_form
        return context