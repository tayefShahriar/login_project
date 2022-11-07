from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView
from .models import Post, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
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

class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        p_form = ProfileUpdateForm(instance=request.user.profile)
        u_form = UserUpdateForm(instance=request.user)
        context = {
            "p_form": p_form,
            "u_form": u_form,
        }
        return render(request, "registration/profile.html", context)
    def post(self, request, *args, **kwargs):
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form.save()
        u_form.save()
        return redirect("profile")
