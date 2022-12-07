from django.shortcuts import render
from .models import saiyan
# Create your views here.
def index(request):
    results = saiyan.objects.filter(fname = "vegeta")
    print(results)
    return render(request,'mysite/index.html',{'results':results})

    # post request to sumbit form
    # if request.method == 'POST':
    #     fname = request.POST.get('fname',"")
    #     power = request.POST.get('power',"")
    #     context = saiyan(fname = fname , power = power)
    #     context.save()
    
    # ORM specific values
    #  all values
    # results = saiyan.objects.all()
    
    # to get speicific values
    # results = saiyan.objects.filter(power ='saiyan')
    
    # exclude values
    # saiyan.objects.exclude(fname='vegeta')
    
    # or query set
    # results = saiyan.objects.filter(fname='Goku') | saiyan.objects.exclude(fname='vegeta')
    # results = saiyan.objects.filter(fname='Goku') or saiyan.objects.exclude(fname='vegeta')
    
    # and query set
    # results = saiyan.objects.filter(fname='yamcha') & saiyan.objects.filter(power='uselesss')
    
    # output individual fields
    