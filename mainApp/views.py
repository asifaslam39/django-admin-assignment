# mainApp/views.py

import pandas as pd
from django.shortcuts import render,HttpResponseRedirect
from .forms import UploadFileForm
from .models import Dish
from django.db.models import Q
import os
from django.conf import settings


def homePage(Request):
    dishes = Dish.objects.all()
    return render(Request, 'index.html', {'dishes': dishes})


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_path = os.path.join(settings.BASE_DIR, 'mainApp/data/restaurants_small.csv')
            data = pd.read_csv(file_path)  # Read the CSV file from the directory

            for _, row in data.iterrows():
                try:
                    lat, lon = map(float, row['lat_long'].split(','))
                    dish = Dish(
                        name=row['name'],
                        items=row['items'],
                        location=row['location'],
                        latitude=lat,
                        longitude=lon,
                        full_details=row['full_details']
                    )
                    dish.save()
                except Exception as e:
                    print(f"Error: {e}")

            return render(request, 'upload_success.html')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

    
def searchPage(request):
    if request.method == "POST":
        search = request.POST.get("search", '').strip()
        if search:
            dishes = Dish.objects.filter(
                Q(name__icontains=search) |
                Q(items__icontains=search) |
                Q(full_details__icontains=search) |
                Q(id__iexact=search)
            )
            return render(request, 'index.html', {'dishes': dishes, 'query': search})
        else:
            return render(request, 'index.html', {'dishes': [], 'query': search})
    else:
        return HttpResponseRedirect("/")