from django.contrib import admin

from .models import Language, Snippet, Tag

admin.site.register(Tag)
admin.site.register(Snippet)
admin.site.register(Language)
