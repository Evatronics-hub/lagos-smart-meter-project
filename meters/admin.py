from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Meter

# Register your models here.

# admin.site.register(Meter)
@admin.register(Meter)
class MeterAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'meter_id', 'customer_balance')

    def customer_name(self, obj):
        return obj.user.name