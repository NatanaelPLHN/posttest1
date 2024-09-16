from django.shortcuts import render

def home(request):
    return render(request, 'home/index.html')

def katalog(request):
    return render(request, 'home/katalog.html')


def about(request):
    return render(request, 'home/about.html')