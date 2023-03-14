from django.shortcuts import render

# Create your views here.
def sample(request):
    d={'name':'vinod'}
    return render(request,'JINJA_PRINTING_TAG.html',d)