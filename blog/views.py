from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# from .models import Post


context = {
    'items': ["items", 'items'],
    'title': 'The Items'
}


def home(request):
    # data = Post.objects.all()
    return render(request, "index.html", {"posts": "data"})
    # return render("template/apps.html", str("context"))
    # return os.path.join(SETTINGS_PATH, 'templates'),
