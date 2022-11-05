from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView
from .models import Post
# Create your views here.
class Homepage(ListView):
    model = Post
    template_name = "home.html"
    context_object_name = "posts"

class Registerview(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, "registration/register.html", {"form": form})
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        return redirect("register")
