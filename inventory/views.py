from django.shortcuts import render,redirect,get_object_or_404
from .models import Carpet
from .forms import CarpetForm

def carpet_list(request):
    carpets = Carpet.objects.all()
    return render(request, 'inventory/carpet_list.html', {'carpets': carpets})


def add_carpet(request):
    if request.method == 'POST':
        form = CarpetForm(request.POST, request.FILES)  # اینجا باید از request.FILES هم استفاده کنید
        if form.is_valid():
            form.save()
            return redirect('carpet_list')
    else:
        form = CarpetForm()
    return render(request, 'inventory/add_carpet.html', {'form': form})


def edit_carpet(request, carpet_id):
    carpet = get_object_or_404(Carpet, id=carpet_id)
    if request.method == 'POST':
        form = CarpetForm(request.POST, instance=carpet)
        if form.is_valid():
            form.save()
            return redirect('carpet_list')
    else:
        form = CarpetForm(instance=carpet)
    return render(request, 'inventory/edit_carpet.html', {'form': form})


def delete_carpet(request, id):
    carpet = get_object_or_404(Carpet, id=id)
    if request.method == 'POST':
        carpet.delete()
        return redirect('carpet_list')
    return render(request, 'inventory/delete_carpet.html', {'carpet': carpet})

def carpet_detail(request, carpet_id):
    carpet = get_object_or_404(Carpet, id=carpet_id)
    return render(request, 'inventory/carpet_detail.html', {'carpet': carpet})
