from django.shortcuts import render
from .forms import MyForms

# Create your views here.
def home(request):
    form = MyForms(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, "home.html", {"form":form})
