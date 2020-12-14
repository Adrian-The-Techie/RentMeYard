from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .api import API

# Create your views here.
@api_view(["POST"])
def api(request):
    response=API(request.data).api()

    return Response(response)