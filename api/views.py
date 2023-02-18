from django.http import HttpResponse
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Item
from api.serializers import ItemSerializer


def index(request):
    return HttpResponse("<h1>Django REST API: Supermarket application CRUD</h1>"
                        "<p><a href='http://127.0.0.1:8000/admin'>Admin page</a></p>"
                        "<p><a href='http://127.0.0.1:8000/api'>API</a></p>"
                        "<ol>"
                        "<li><a href='http://127.0.0.1:8000/api/create'>Create Item</a></li>"
                        "</ol>")

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


@api_view(['POST'])
def add_items(request):
    item = ItemSerializer(data=request.data)

    # validating for already existing data
    if Item.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
