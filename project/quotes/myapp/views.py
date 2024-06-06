

# Create your models here.
from django.shortcuts import render
from .models import Quote
import requests




def Log(request):
    if request.method=='POST':
        email=request.POST['name']
        passw=request.POST['pass']
    return render(request,"log.html")
def register(request):
    return render(request,"register.html")
# for fetching random quotes from api and save it in our database Quote.
def get_random_quote():
    response = requests.get("https://api.quotable.io/random")
    data = response.json()
    text = data["content"]
    author = data["author"]
    
    
    if not Quote.objects.filter(text=text, author=author).exists():
        Quote.objects.create(text=text, author=author)
    
    return text, author

def home(request):
    quote = Quote.objects.order_by('?').first()
    return render(request, 'home.html', {'quote': quote.text, 'author': quote.author})

def search(request):
    query = request.GET.get('q')
    results = Quote.objects.filter(author__icontains=query)
    return render(request, 'search.html', {'results': results, 'query': query})
