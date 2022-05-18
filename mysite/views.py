# I have Created This File- Raj
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
     #p={'name':'Raj','place':'USA'}
     return render(request,'index.html')
def analyze(request):
     # get the text
     djtext=(request.GET.get('text','default'))
     removepunc=(request.GET.get('removepunc','off'))

     #print(removepunc)
     # analyze the text
     #print(djtext)
     if removepunc=='on':
          punctuations='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
          analyzed=''
          for char in djtext:
               if char not in punctuations:
                    analyzed=analyzed+char
          params={'purpose':'Removed punctuations','Analyzed_text':analyzed}
          return render(request,'analyze.html',params)
     else:
          return HttpResponse("Error")





    
    
#def capfirst(request):
 #    return HttpResponse("capitalize first <a href='removepunc'>back</a>")
#def newlineremove(request):
 #    return HttpResponse("NewLine Remove <a href='capitalizefirst'>back</a>")
#def spaceremove(request):
 #    return HttpResponse("Space Remove <a href='newlineremove'>back</a>")
#def charcount(request):
#     return HttpResponse("Char Count <a href='spaceremove'>back</a>")
