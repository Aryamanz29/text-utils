from django.shortcuts import render
from django.http import HttpResponse
def home(request):
     return render(request,'home.html',{})
def result(request):
        text=request.GET.get('text','defaultText')
        puncResponse=request.GET.get('puncResponse','off')
        capResponse=request.GET.get('capResponse','off')
        if capResponse=='on'and puncResponse=='on':
           removePunc=clearPunc(request,text)
           removeCap=capString(request,removePunc)
           return render(request,'result.html',{'removePunc':removeCap})
        elif puncResponse =='on':
           removePunc=clearPunc(request,text)
           return render(request,'result.html',{'removePunc':removePunc})
        elif capResponse =='on':
           removePunc=capString(request,text)
           return render(request,'result.html',{'removePunc':removePunc})
        else:
             return HttpResponse("<h1> error  404 </h1>")
def clearPunc(request,text):
        text=request.GET.get('text','defaultText')
        puncList="""#$%&'()*+, -./:;<=>?@[\]^_`{|}~"""
        removePunc=""
        for char in text:
          if char in puncList:
            removePunc+=""
          else:
            removePunc+=char
        return removePunc
def capString(request,text):
        removePunc=""  
        for char in text:
          if char.isupper()==True:
            removePunc+=char.lower()
          else:
            removePunc+=char
        return removePunc
        