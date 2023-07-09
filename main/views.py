from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def result(request):
    return render(request, 'result.html')

def ESE(request):
    return render(request, 'ese.html')
def ESH(request):
    return render(request, 'esh.html')
def ENE(request):
    return render(request, 'ene.html')
def ENH(request):
    return render(request, 'enh.html')
def ISE(request):
    return render(request, 'ise.html')
def ISH(request):
    return render(request, 'ish.html')
def INE(request):
    return render(request, 'ine.html')
def INH(request):
    return render(request, 'inh.html')