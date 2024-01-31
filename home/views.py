from django.shortcuts import render

from home.models import Service, Gallery


def home(request):
    services = Service.objects.all()
    gallery = Gallery.objects.all()
    context = {'services': services, 'gallery': gallery}
    return render(request, 'home/home.html', context)


def contact(request):
    if request.method == "POST":
        print("Hi")
        return render(request, 'home/contact.html')
    return render(request, 'home/contact.html')
