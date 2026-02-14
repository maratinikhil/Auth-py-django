from django.shortcuts import render

from django.http import HttpResponse

def class1(request):
    return HttpResponse("<tt>Functional Component<tt/>")