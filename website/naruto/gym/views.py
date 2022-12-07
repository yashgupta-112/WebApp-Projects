from django.shortcuts import render
from gym.models import contact,Post,Ninja
from django.contrib import messages
from django.http import request

# Create your views here.
def index(request):
     return render(request, 'gym/index.html')

def ccontact(request):
     if request.method=='POST':
          name = request.POST['fname']
          phone = request.POST['phone']
          email = request.POST['email']
          mess = request.POST['mess']
          cont =contact(name=name,phone=phone,email=email,content=mess)
          if len(name)<3 or len(phone)<11 or len(email)<3:
               messages.error(request, 'Please refill the contact form..')
          else:
               cont.save()
               
               messages.success(request, 'Your message has been send to our team')
     return render(request, 'gym/contact.html')          
def supp(request):
     Posts =Post.objects.all()
     context ={'Posts':Posts}
     return render(request, 'gym/supp.html',context)
def trans(request):
     return render(request, 'gym/trans.html')   
def bmr(request):
     return render(request, 'gym/prac.html') 
def create_ninja(request):
    return render(request, 'gym/ninja.html')  
def saiyan(request):
     return render(request, 'gym/saiyan.html')
def tonned(request):
     return render(request, 'gym/tonned.html')
def muscle(request):
     return render(request, 'gym/muscle.html') 
def dis(request):
     return render(request, 'gym/dis.html')
def health(request):
     return render(request, 'gym/healthy.html')