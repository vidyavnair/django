from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html",{})
def counter(request):
    text=request.POST['text']
    text_len=len(text.split())
    return render(request,"counter.html",{'text_len':text_len})