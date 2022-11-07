from django.shortcuts import render
from newlogin.models import Post
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.

class Postdetails(DetailView):
    model = Post
    template_name = "post/detail.html"

class Createpost(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'text']
    template_name = "post/newpost.html"
    success_url = "/"
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class Deletepost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "post/delete.html"
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    success_url = "/"

class Updatepost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'text']
    template_name = "post/newpost.html"
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    success_url = "/"
