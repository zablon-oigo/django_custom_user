from django.contrib import admin
from .models import CustomUser,Profile
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm,CustomUserCreationForm
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=['user','photo','date_of_birth']
    list_filter=['date_of_birth']


class CustomUserAdmin(UserAdmin):
    add_form=CustomUserCreationForm
    form=CustomUserChangeForm
    model=CustomUser

    list_display=['email','is_staff','is_active']
    list_filter=['email','is_staff','is_active']
    fieldsets=(
        (None,{'fields':('email','password')}),
        ('Permissions',{'fields':('is_staff','is_active')}),
    )
    add_fieldsets=(
        (None,{
            'classes':('wide'),
            'fields':('email','password1','password2','is_staff','is_active')
        }),

    )

    search_fields = ['email']
    ordering =['email'] 
    filter_horizontal = ()  
  
admin.site.register(CustomUser, CustomUserAdmin)  

