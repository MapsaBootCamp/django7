import re
from django.shortcuts import render
from django.http import JsonResponse

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

