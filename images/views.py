from django.shortcuts import render
from .models import Image,Location
from django.shortcuts import render,redirect
from django.http  import HttpResponse
import datetime as dt

from django.http  import HttpResponse,Http404
# Create your views here.
def landing(request):
    images = Image.objects.all()
    locations = Location.find_locations()
    print(locations)

    return render(request, 'landing.html', {'images': images[::-1], 'locations': locations})

def single(request,images_id):
    try:
        single = Image.objects.get(id = images_id)
    except Image.DoesNotExist:
        raise Http404()
    return render(request,"single.html", {"single":single})

def image_location(request,location):
    images = Image.filter_by_location(location)
    print(images)
    return render(request, 'location.html', {'location_images': images})

def search_results(request):
    if 'imagesearch' in request.GET and request.GET["imagesearch"]:
        category = request.GET.get("imagesearch")
        searched_images = Image.search_by_category(category)
        message = f"{category}"
        print(searched_images)
        return render(request, 'search.html', {"message": message, "images": searched_images})
    else:
        message = "You haven't searched for any image category"
        return render(request, 'search.html', {"message": message})