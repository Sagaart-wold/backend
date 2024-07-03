from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ['email',
                    'phone',
                    'first_name',
                    'last_name',
                    'role',
                    'is_active',
                    'is_staff']

    list_filter = ['role',
                   'is_active',
                   'is_staff']

    search_fields = ['email',
                     'first_name',
                     'last_name',
                     'phone']

    ordering = ['email']

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name',
                                      'last_name',
                                      'phone',
                                      'address')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'role')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email',
                       'password1',
                       'password2',
                       'is_active',
                       'is_staff',
                       'role')}),
    )


admin.site.site_header = 'Управление пользователями'  
admin.site.site_title = 'Администрирование'
