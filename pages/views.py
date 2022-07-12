from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy

from .models import ArticleModel

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.
class HomePageView(ListView):
    model = ArticleModel
    template_name = 'home.html'


class ArticleListView(ListView):
    model = ArticleModel
    template_name = 'article_list.html'


class ArticleDetailView(DetailView):
    model = ArticleModel
    template_name = 'article_detail.html'


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = ArticleModel
    template_name = 'article_new.html'
    fields = [
        'sarlavha',
        'qisqa_mazmun',
        'body',
        'photo',
    ]

    def form_valid(self, form):
        form.instance.muallif = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ArticleModel
    template_name = 'article_edit.html'
    fields = [
        'sarlavha',
        'qisqa_mazmun',
        'body',
        'photo',
    ]

    def test_func(self):
        obj = self.get_object()
        return obj.muallif == self.request.user


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ArticleModel
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

    def test_func(self):
        obj = self.get_object()
        return obj.muallif == self.request.user


class AboutView(TemplateView):
    template_name = 'about.html'


class ContactView(TemplateView):
    template_name = 'contact.html'
