from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import *


# Register your models here.





class UserAdminConfig(UserAdmin):
    model = CustomUser
    search_fields = ('email', 'username', 'full_name')
    list_filter = ('email', 'username', 'full_name')
    ordering = ('-id',)
    list_display = ('username',)
    fieldsets = (
        ("Details", {'fields': ('email', 'username', 'password','full_name', 'email_verified_at', 
                                'status','is_verified')}),
        ('Permissions', {'fields': ('is_staff', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'full_name', 'password1', 'password2', 'is_staff')}
         ),
    )


admin.site.register(CustomUser, UserAdminConfig)


