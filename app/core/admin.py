from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# import default user admin
from django.utils.translation import gettext as _
from core import models


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        # each bracket is a section, and the first element is title
        (_('Personal Info'), {'fields': ('name',)}),
        # should have comma even though it only has one element.
        (
            _('Permissions'),
            {
                'fields': ('is_active', 'is_staff', 'is_superuser')
            }
        ),
        (_('Important dates'), {'fields': ('last_login',)})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password', 'password2')
        }),
    )


admin.site.register(models.User, UserAdmin)
# admin.register(models.User, UserAdmin)
