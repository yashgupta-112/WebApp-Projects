from django.shortcuts import render
from .models import saiyan
# Create your views here.


def index(request):
    if request.method == 'POST':
        fname = request.POST.get('fname', "")
        power = request.POST.get('power', "")
        context = saiyan(fname=fname, power=power)
        context.save()
    return render(request, 'mysite/index.html')
