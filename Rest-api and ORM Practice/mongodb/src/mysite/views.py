from django.shortcuts import render
from .models import saiyan
# Create your views here.
def index(request):
    results = saiyan.objects.all()
    return render(request,'mysite/index.html',{'results':results})

    