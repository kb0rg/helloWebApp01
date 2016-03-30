from django.shortcuts import render
from collection.models import Thing

# Create your views here.
def index(request):
    numA = 5
    numB = 1500
    numC = 100000000
    things = Thing.objects.all()
    word = "sphygmomanometer"
    return render(request, 
                    'index.html', 
                    {'numA': numA,
                    'numB': numB,
                    'numC': numC,
                    'things': things,
                    'word': word,
                    })