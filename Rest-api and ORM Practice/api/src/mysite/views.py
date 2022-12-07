from django.shortcuts import render
from .models import saiyan
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import saiyanSerializer


# Create your views here.
def index(request):
    if request.method == 'POST':
        fname = request.POST.get('fname',"")
        power = request.POST.get('power',"")
        context = saiyan(fname = fname , power = power)
        context.save()
    return render(request,'mysite/index.html')

@api_view(['GET'])
def apioverview(request):
    api_urls ={
        'List':'/api/',
        'Detail':'/apidetail/<str:pk>',
        'Create':'/apicreate/',
        'Update':'/apiudate/<str:pk>/',
        'delete':'/apidelete/<str:pk>/'
    }
    return Response(api_urls)


@api_view(['GET'])
def api(request):
    result = saiyan.objects.all()
    serializer = saiyanSerializer(result,many = True)
    return Response(serializer.data)


@api_view(['DELETE'])
def apidelete(request,pk):
    result = saiyan.objects.get(id=pk)
    result.delete()

    return Response("Item deleted")

@api_view(['POST'])
def apiupdate(request,pk):
    result = saiyan.objects.get(pk=pk)
    serializer = saiyanSerializer(instance=result,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def apicreate(request):
    result = saiyan.objects.all()
    serializer = saiyanSerializer(result,many = True)
    return Response(serializer.data)

@api_view(['GET'])
def apidetail(request,):
    serializer = saiyanSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

