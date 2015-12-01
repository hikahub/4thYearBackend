# Create your views here.
from django.http import JsonResponse, HttpResponse
from geopy.geocoders import Nominatim
from.models import User, Landmarks
from django.core import serializers


def locations(request):
    geolocator = Nominatim()
    location = geolocator.geocode("eiffel tower,paris")
    print(location.address)
    print((location.latitude, location.longitude))
    return HttpResponse(location)


def signup(request):
    mail =request.POST.get('email', '')
    name1 = request.POST.get('name', '')
    psword = request.POST.get('password', '')
    print(psword)
    registerUser = User(email=mail, name=name1, password=psword)
    registerUser.save()

    reg_data = {
            'error': 'false',
            'userId': 'Has been register'

        }
    return JsonResponse(reg_data, safe=False)

def login(request):
    email1 = request.POST.get('email', '')
    password2 = request.POST.get('password', '')
    print(email1)

    data = User.objects.get(email=email1, password=password2)

    login_data = {
            'error': 'false',
            'userId': data.pk
        }
    return JsonResponse(login_data, safe=False)

def landmarks_list(request):
    placeName = request.POST.get('place_name', '')
    address1 = request.POST.get('address', '')
	category = request.POST.get('place_category','')
    admission1 = request.POST.get('admission', '')
    list_data = Landmarks.objects.get(place_name=placeName, address=address1, place_category=category, admission=admission1)

    landmarks_data = {
            'error': 'false',
            'id': list_data
        }
    return JsonResponse(landmarks_data, safe=False)

def landmark_info(request):
    placeName1 = request.POST.get('place_name', '')
    address2 = request.POST.get('address', '')
    descript = request.POST.get('place_desc', '')
    admission2 = request.POST.get('admission', '')
    image = request.POST.get('imageUrl', '')
    wiki = request.POST.get('wiki_link', '')
    openDays = request.POST.get('opening_days', '')
    info_data = Landmarks.objects.get(place_name=placeName1, address=address2, place_desc=descript, admission=admission2,imageUrl=image, wiki_link=wiki, opening_days=openDays)

    place_data = {
            'error': 'false',
            'id': info_data
        }
    return JsonResponse(place_data, safe=False)






