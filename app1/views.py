from django.shortcuts import render

# Create your views here.

def jinja1(request):
    d={'name':'fayaz'}
    return render(request,'jinja1.html',context=d)