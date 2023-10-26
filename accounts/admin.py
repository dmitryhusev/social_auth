from .models import Profiles

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


class UserAdmin(UserAdmin):
    model = Profiles
    list_display = ("email", "id", "first_name", "last_name", "is_superuser", "is_active")
    list_filter = ()
    ordering = ("-id",)
    fieldsets = ()
    search_fields = ("first_name", "last_name", "email")
    add_fieldsets = (
            (
                None,
                {
                    'classes': ('wide',),
                    'fields': ('email', 'password1', 'password2'),
                },
            ),
        )

admin.site.register(Profiles, UserAdmin)
