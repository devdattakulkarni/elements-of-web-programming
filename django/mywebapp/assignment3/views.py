from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from http import HTTPStatus
from .models import Library

import json

def index(request):
    return HttpResponse("Hello, world. You're at assignment3 index.")

@csrf_exempt
def handle_libraries(request):
    if request.method == 'GET':
        libraries = {} # Return all the libraries
        return JsonResponse(libraries, status=HTTPStatus.OK)
        
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        library_name = data_json['name']
        print("Received Library with name:" + library_name)
        library = Library(name=library_name)
        library.save()
        library_id = library.id
        library_response = {}
        library_response["id"] = library.id
        library_response["name"] = library_name
        return JsonResponse(library_response, status=HTTPStatus.OK)

@csrf_exempt
def handle_single_library(request, library_id):

    library = {}
    if request.method == 'GET':
        libraryObj = Library.objects.filter(id=library_id)
        if len(libraryObj) > 0:
            name = libraryObj[0].name
            library['name'] = name
    return JsonResponse(library, status=HTTPStatus.OK)
