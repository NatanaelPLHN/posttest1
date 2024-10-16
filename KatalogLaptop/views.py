from django.shortcuts import render, redirect, get_object_or_404
from .models import Laptop
from .forms import LaptopForm
from django.db.models import Q


def home(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

def laptop_list(request):
    query = request.GET.get('q', '')
    laptops = Laptop.objects.all()

    if query:
        laptops = laptops.filter(
            Q(laptop_name__icontains=query) | Q(spec__icontains=query)
        )

    return render(request, 'katalog/katalog.html', {'laptops': laptops, 'query': query})

def laptop_create(request):
    if request.method == 'POST':
        form = LaptopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('katalog') 
    else:
        form = LaptopForm()
    return render(request, 'katalog/laptop_form.html', {'form': form})

def laptop_update(request, id_laptop):
    laptop = get_object_or_404(Laptop, id_laptop=id_laptop)
    if request.method == 'POST':
        form = LaptopForm(request.POST, instance=laptop)
        if form.is_valid():
            form.save()
            return redirect('katalog')  
    else:
        form = LaptopForm(instance=laptop)
    return render(request, 'katalog/laptop_form.html', {'form': form})

def laptop_delete(request, id_laptop):
    laptop = get_object_or_404(Laptop, id_laptop=id_laptop)

    if request.method == 'POST':
        laptop.delete()
        return redirect('katalog')  

    return render(request, 'katalog/laptop_confirm_delete.html', {'laptop': laptop})