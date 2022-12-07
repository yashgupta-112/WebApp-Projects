from django.shortcuts import render
from .models import blog
# Create your views here.
def index(request):
     post=blog.objects.all()
     context ={'post':post}
     return render(request, 'blog/index.html',context)
