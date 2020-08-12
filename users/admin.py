from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.html import format_html

from meters.models import Meter

# Register your models here.

from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import User

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('name', 'email', 'meter_id', 'customer_balance')
    list_filter = ('admin',)
    fieldsets = (
        (None, {'fields': ('name', 'email', 'password')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

    def meter_id(self, obj):
        # This is a custom method to display the user's meter_id
        try:
            meter_id = obj.meter_set.get().meter_id
        except Meter.DoesNotExist:
            meter_id = 'Null'
        return format_html(f'<i>{meter_id}</i>')

    def customer_balance(self, obj):
        try:
            customer_balance = obj.meter_set.get().customer_balance
        except Meter.DoesNotExist:
            customer_balance = 0.00
        return format_html(f'<b style="text-align: center;">{customer_balance}</b>')


admin.site.register(User, UserAdmin)

# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)