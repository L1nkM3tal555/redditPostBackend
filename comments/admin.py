from django.contrib import admin

from comments.models import Comentario

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'responseComment']