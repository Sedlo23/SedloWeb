from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import BinaryFile
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import STLModel,Telegram
def main_page(request):
    return render(request, 'main.html')

# Empty page views
@login_required
def zapisy_z_testovani(request):
    return render(request, 'zapisy.html')


@login_required
def telegramy(request):
    telegrams = Telegram.objects.all().values('id', 'name', 'latitude', 'longitude')
    return render(request, 'telegramy.html', {'telegrams': telegrams})



@login_required
def ostatni(request):
    return render(request, 'ostatni.html')

# SedloWeb/views.py# SedloWeb/views.py
@login_required
def programy(request):
    files = BinaryFile.objects.all()  # Retrieve all uploaded files
    return render(request, 'programy.html', {'files': files})
@login_required
def file_detail(request, file_id):
    binary_file = get_object_or_404(BinaryFile, id=file_id)
    return render(request, 'file_detail.html', {'binary_file': binary_file})

@login_required
def models_3d(request):
    stl_models = STLModel.objects.all()
    return render(request, 'models_3d.html', {'stl_models': stl_models})


@login_required
def model_detail(request, model_id):
    stl_model = get_object_or_404(STLModel, id=model_id)
    return render(request, 'model_detail.html', {'stl_model': stl_model})

@login_required
def telegram_detail(request, telegram_id):
    telegram = get_object_or_404(Telegram, id=telegram_id)
    return render(request, 'telegram_detail.html', {'telegram': telegram})