from django.shortcuts import render
from Fetchdata.models import Ranking

def showdata(request):
    results=Ranking.objects.all()
    return render(request,'index.html', {"data":results})