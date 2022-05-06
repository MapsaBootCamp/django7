import json
from typing import Dict

from django.http import Http404, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from book.models import Book
from rent.models import RentBook
from user.models import Profile

@method_decorator(csrf_exempt, name='dispatch')
class BookRentView(View):

    RENTAL_DATA_FIELDS = ["username", "title", "author"]

    def _is_valid_data(self, data: Dict):
        result = {"error": False}
        for field in BookRentView.RENTAL_DATA_FIELDS:
            if field not in data.keys():
                result.update("error",  True)
                result["error_message"] = "field {field} lazemeh"
                return result
        return result

    def post(self, request):
        try:
            data = json.loads(request.body)
        except:
            return JsonResponse({'status':'false','message':"khak tu saret ke json naferestadi"}, status=400)
        if self._is_valid_data(data)["error"]:
            return JsonResponse(self._is_valid_data(data), status=400)

        user: Profile = get_object_or_404(Profile, username=data.get("username"))
        book: Book = get_object_or_404(Book, title=data.get("title"), author1=data.get("author"))

        if not book.available_qty:
            return JsonResponse({'status':'false','message':"khak tu saret dir umadi"}, status=404)
        book.available_qty -= 1
        book.save()
        RentBook.objects.create(book=book, user=user)
        return JsonResponse({'status':'true','message':"ba khubi va khshi ejare shod"})
