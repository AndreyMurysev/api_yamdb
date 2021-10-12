from django.contrib import admin

from .models import User

VOID = '-пусто-'

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'email', 'role')
    empty_value_display = VOID
