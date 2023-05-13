from django.shortcuts import render, get_object_or_404
from .models import Service, Gallerie, Categorie, Benin_Mobilier
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib import messages
from django.conf import settings
from django.contrib import messages

# Create your views here.

def index (request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        country = request.POST.get('country')
        article = request.POST.get('article')
        quantite = request.POST.get('quantite')
        # indicatif = request.POST.get('indicatif')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        

        html = render_to_string('store/email.html', {
            'name':name,
            'email':email,
            'country':country,
            'article': article,
            'quantite':quantite,
            # 'indicatif':indicatif,
            'phone':phone,
            'message':message,
            })
        

 
        send_mail('Nouvelle commande', '','email', [settings.EMAIL_HOST_USER], html_message=html)
        messages.success(request, "Votre message a été envoyé avec succes !!")

    return render(request, 'store/index1.html')

# def vehicules(request, slug):
#     voiture = get_object_or_404(Voiture, slug=slug)
#     if request.method == 'POST':
#         car = voiture.marque
#         print(car)
#         return render(request, 'store/appoinment.html', {'car':car})
#     # vehicules = Voiture.objects.all()
#     # return render(request, 'store/vehicules.html', {"vehicules":vehicules})
#     return render(request, 'store/vehicules.html')

# # def voiture(request, slug):
    
# #     return render(request, 'store/department-single.html', {'voiture':voiture} )



def a_propos(request):
    return render(request, 'store/about1.html')


def meubles(request):
    categories = Categorie.objects.all()
    meubles = Benin_Mobilier.objects.all()
    return render(request, 'store/doctor1.html', {"categories": categories, 
                                                   "meubles": meubles    })


def gallerie(request):
    gallerie = Gallerie.objects.all()
    return render(request, 'store/gallery.html', {"Gallerie": gallerie})


def contacter(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        

        html = render_to_string('store/email1.html', {
            'name':name,
            'email':email,
            'subject':subject,
            'phone':phone,
            'message':message,
            })
        

 
        send_mail('Nouvelle commande', '','email', [settings.EMAIL_HOST_USER], html_message=html)
        messages.success(request, "Votre message a été envoyé avec succes !!")

    return render(request, 'store/contact1.html')


def service(request):
    Services = Service.objects.all()
    # if request.method == 'POST':
    #     service = get_object_or_404(Service, slug = slug)
    #     commande = service.nom
    #     print(commande)
    #     return render(request, 'store/appointment.html', {'commande':commande})
    return render(request, 'store/service1.html' , {"Services":Services})

def reserver(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        country = request.POST.get('country')
        article = request.POST.get('article')
        quantite = request.POST.get('quantite')
        # indicatif = request.POST.get('indicatif')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        

        html = render_to_string('store/email.html', {
            'name':name,
            'email':email,
            'country':country,
            'article': article,
            'quantite':quantite,
            # 'indicatif':indicatif,
            'phone':phone,
            'message':message,
            })
        

 
        send_mail('Nouvelle commande', '','email', [settings.EMAIL_HOST_USER], html_message=html)
        messages.success(request, "Votre message a été envoyé avec succes !!")

    return render(request, 'store/appointment1.html')




