from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'title':'World_Art - Главная',
        'content':'Магазин World Art'
    }
    
    return render(request,'main/index.html',context)


def about(request):
    context = {
        'title':'World_Art - О нас',
        'content':'О нас',
        'text_on_page':'Наша платформа позволит Вам найти картину или скульптуру, которая станет идеальным подарком коллеге или руководителю, замечательным украшением для Вашего офиса или первым шагом в создании корпоративной или частной коллекции. Artcenter.by позволит оперативно выбрать нужное Вам произведение искусства, услугу или сопутствующий товар, основываясь на Вашем бюджете, цели покупки, цветовом решении или совокупности нескольких задач.',     
    }  
    return render(request,'main/about.html',context)


def contact(request):
    context = {
         'title':'World_Art - Контакты',
        'text_contact':'Наши контакты',
        'number':'Мой телефон - +375293456748'
    }
    return render(request,'main/contact.html', context)
