from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model


class UserAdmin(UserAdmin):
    model = get_user_model()
    list_display = ['username', 'email', 'first_name', 'last_name']


admin.site.register(get_user_model(), UserAdmin)
