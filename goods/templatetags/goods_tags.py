from django import template

from goods.models import Categories

register = template.Library()



@register.simple_tag()
def tag_categories():
    return Categories.objects.all()   #В административной панели хранятся все категории оттуда и берем их 