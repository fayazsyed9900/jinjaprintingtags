from django.shortcuts import render

# Create your views here.
def jinja2(request):
    d={'name':'basha'}
    return render(request,'jinja2.html',d)