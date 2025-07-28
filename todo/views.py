from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

class ToDo(View):
    def get(self, request):
        return HttpResponse('<h1>Hello, world</h1>')
    