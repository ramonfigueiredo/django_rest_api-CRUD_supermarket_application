from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Item
from api.serializers import ItemSerializer


def index(request):
    return HttpResponse("<h1>Django REST API: Supermarket application CRUD</h1>"
                        "<p>"
                        "<a href='http://127.0.0.1:8000/api'>Open API</a>"
                        "<p>")


@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_items': '/',
        'Search by Category': '/?category=category_name',
        'Search by Subcategory': '/?subcategory=category_name',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }

    return Response(api_urls)
