from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Meter, Billing
from .forms import MeterChangeForm

admin.site.site_header = "Lagos Smart Project"
admin.site.site_title = "Admin"
admin.site.index_title = "Site Admin"

# @admin.register(Meter)
class MeterAdmin(admin.ModelAdmin):
    # add_form_template = MeterChangeForm
    list_display = ('customer_name', 'meter_id', 'customer_balance', 'billing_type')

    def customer_name(self, obj):
        return obj.user.name

    def billings(self, obj):
        METER_TIER = [
            (0, 'Basic'),
            (1, 'Shop'),
            (2, 'Company'),
        ]
        num = obj.billings
        return METER_TIER[num][1]

# @admin.register(Billing)
class MeterTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_per_unit', 'users')

    def users(self, obj):
        number = len(obj.meter_set.get_queryset())
        if not number:
            return 'null'
        elif number == 1:
            return '1 user'
        else:
            return f'{number} users'