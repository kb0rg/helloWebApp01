from django.shortcuts import render

# Create your views here.
def index(request):
    numA = 5
    numB = 1500
    numC = 100000000
    return render(request, 
                    'index.html', 
                    {'numA': numA,
                    'numB': numB,
                    'numC': numC,
                    })