from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def jampandu(request):
    return HttpResponse('<h1><marquee>Hi How Are You</h1><marquee>')


def test(request):
    return HttpResponse('<h1><marquee>Testing is completed</h1></marquee>')
