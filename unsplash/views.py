from django.shortcuts import render
from unsplash.models import ImageLinks
from django.core.paginator import Paginator
# Create your views here.


def unsplash(request):
    limit = 15
    images = ImageLinks.objects
    paginator = Paginator(images, limit)
    page = request.GET.get('page', 1)
    load = paginator.page(page)
    context = {
        'images': load
    }
    return render(request, 'unsplash.html', context)
