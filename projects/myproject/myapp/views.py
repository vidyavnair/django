from django.shortcuts import render

# Create your views here.
visit_count = 0

def home(request):
    return render(request, 'home.html')

def counting_page(request):
    global visit_count
    visit_count += 1
    return render(request, 'counting_page.html', {'count': visit_count})
