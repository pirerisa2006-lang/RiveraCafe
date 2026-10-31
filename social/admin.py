from django.contrib import admin
from .models import Redsocial


@admin.register(Redsocial)
class RedsocialAdmin(admin.ModelAdmin):
    list_display = ("name", "link")
