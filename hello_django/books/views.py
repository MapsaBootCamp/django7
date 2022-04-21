import re
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView


from .models import Book

def book_list(requset):
    if requset.method == "GET":
        qs = Book.objects.all()
        result = []
        for elm in qs:
            result.append({
                "title": elm.title,
                "author": elm.author,
                "published": elm.published_year
            })

        return JsonResponse(result, safe=False)
    else:
        return JsonResponse({"error": "faghat get emkan pazireh"})



class ViewSalamKardan(View):

    def get(self, request):
        return render(request, "index.html", context={"name": "Ashkan"})


class ViewAleikGftan(TemplateView):
    template_name = "index.html"
    extra_context = {"name": "Ashkan"}

