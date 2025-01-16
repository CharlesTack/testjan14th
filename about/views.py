from django.shortcuts import render
from .models import About

# Create your views here.

class PostList(generic.ListView):
    
    template_name = "about/about.html"
    paginate_by = 6



def about_me(request):
    """
    Renders the About page
    """
    about = About.objects.all().order_by('-updated_on').first()
    
    return render(
        request,
        "about/about.html",
        {"about": about},
    )