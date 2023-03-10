from django import template

from ecn.models import *

register = template.Library()


@register.inclusion_tag('ecn/inclusion/header.html')
def show_header(user='user'):   
    logo = Graphics.objects.get(description='логотип')   
    in_city_object_type = InCityObjectType.objects.filter(in_main_page=True)
    out_city_object_type = OutCityObjectType.objects.filter(in_main_page=True)
    return {
            "logo": logo,
            'in_city_object_type': in_city_object_type,
            'out_city_object_type': out_city_object_type,
            'user':user
            }


@register.inclusion_tag('ecn/inclusion/items_list.html')
def show_apa(
        obj_list_type='city',
        obj_type='vtorichnoe-zhile',
        s_or_r='s'
):
    if obj_list_type == 'city':
        selected_items = InCityObject.objects.filter(object_type__slug=obj_type).filter(sale_or_rent=s_or_r).order_by(
            '-time_create')
        incity_id = InCityObjectType.objects.get(slug=obj_type)
    else:
        selected_items = OutCityObject.objects.filter(object_type__slug=obj_type).order_by('-time_create')
        incity_id = OutCityObjectType.objects.get(slug=obj_type)
    return {
        'selected_items': selected_items,
        'incity_id': incity_id,
        'no_photo': Graphics.objects.get(description='нет фото')
    }


# @register.inclusion_tag('ecn/inclusion/links_list.html')
# def links_list():
#     selected_link = 