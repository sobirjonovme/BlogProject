from django.contrib import admin
from .models import ArticleModel, CommentModel


class CommentInLine(admin.TabularInline):
    model = CommentModel
    extra = 0


class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentInLine]


# Register your models here.
admin.site.register(ArticleModel, ArticleAdmin)
admin.site.register(CommentModel)
