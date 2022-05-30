from django.shortcuts import render
from .models import Image,Location

# Create your views here.
def landing(request):
    images = Image.objects.all()
    locations = Location.find_locations()
    print(locations)

    return render(request, 'landing.html', {'images': images[::-1], 'locations': locations})
