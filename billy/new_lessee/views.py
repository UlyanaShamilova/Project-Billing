from django.shortcuts import render

# Create your views here.
def new_lessee(request):
    return render(request, 'new_lesse/new_lessee.html')