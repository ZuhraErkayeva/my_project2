from django.contrib import admin
from .models import Kitob

@admin.register(Kitob)
class KitobAdmin(admin.ModelAdmin):
    list_display = ('nom', 'muallif', 'nashr_sana', 'isbn', 'sahifalar_soni', 'til', 'janr')
    search_fields = ('nom', 'muallif', 'isbn')

