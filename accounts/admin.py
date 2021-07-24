from django.contrib.auth.admin import UserAdmin
from accounts.models import Account
from django.contrib import admin


class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'phone_number','username','date_joined', 'last_login', 'is_active')
    list_display_links = ('email', 'first_name', 'last_name', 'phone_number', 'username',)
    readonly_fields = ('date_joined', 'last_login')
    ordering = ('-date_joined',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)
# Register your models here.
