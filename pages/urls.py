from django.urls import path
from .views import (
    HomePageView,
    ArticleListView,
    ArticleDetailView,
    AboutView,
    ContactView,
    ArticleUpdateView,
    ArticleDeleteView,
    ArticleCreateView,
)


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('articles/', ArticleListView.as_view(), name='article_list'),
    path('articles/new/', ArticleCreateView.as_view(), name='article_new'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('articles/<int:pk>/edit', ArticleUpdateView.as_view(), name='article_edit'),
    path('articles/<int:pk>/delete', ArticleDeleteView.as_view(), name='article_delete'),
]
