from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserAdminCreationForm, UserAdminChangeForm

User = get_user_model()
admin.site.unregister(Group)
# Register your models here.
class UserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm  
    add_form = UserAdminCreationForm
    
    list_display = ['email', 'is_admin']
    list_filter = ['is_admin']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('permissions', {'fields': ('is_admin', 'is_candidate', 'is_staff', 'is_employer')}),
    )

    add_fieldsets = (
        (None, {
            'classes' : ('wide',),
            'fields' : ('email', 'password1', 'password2')
        }),
    )

    search_fields = ['email']
    ordering = ['email']
    filter_horizontal = ()




admin.site.register(User, UserAdmin)
