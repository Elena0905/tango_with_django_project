from rango.models import Category
from rango.models import Page
from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    category_list = Category.objects.order_by('-likes')[:5]
    page_list= Page.objects.order_by('-views')[:5]
    context_dict = {'categories': category_list,'pages':page_list}
    
    return render(request, 'rango/index.html', context=context_dict)
 
def about(request):
    return HttpResponse( "Rango says here is the about page."+'<a href="/rango/">Index</a>')
def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None
    return render(request, 'rango/category.html', context=context_dict)
#def show_page(request,page_title_slug):
#    context_dict={}
#    try:
#        pages=Page.objects.get(slug=page_title)
#        pages=Page.objects.filter(pages=pages)
#        context_dict['pages'] = pages
#    except Page.DoesNotExist:
#        context_dict['pages'] = None
#    return render(request, 'rango/page.html', context=context_dict)
#    
        
        