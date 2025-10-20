from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        message = request.POST.get('message', '').strip()
        if not name or not message:
            return render(request, 'catalog/contacts.html', {'name': name, 'message': message})
        return HttpResponse(f"{name}, благодарим за обращение!")
    return render(request, 'catalog/contacts.html')
