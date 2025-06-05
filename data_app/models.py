from django.db import models

from django.db import models

class LargeData(models.Model):
    name = models.CharField(max_length=300)
    organization_id = models.IntegerField()
    user_id = models.IntegerField()

    pan_id = models.CharField(max_length=80, null=True, blank=True)
    gstin = models.CharField(max_length=50, null=True, blank=True)
    customer_code = models.CharField(max_length=25, null=True, blank=True)

    contact_person_name = models.CharField(max_length=200, null=True, blank=True)
    contact_mobile = models.CharField(max_length=80, null=True, blank=True)
    email = models.EmailField(max_length=500, null=True, blank=True)

    country_code = models.CharField(max_length=4)
    mobile = models.CharField(max_length=80, null=True, blank=True)
    is_whatsapp_verified = models.BooleanField(default=False)

    payment_term = models.CharField(max_length=50, null=True, blank=True)
    credit_limit = models.DecimalField(max_digits=20, decimal_places=4, default=0.0)
    outstanding_amount = models.DecimalField(max_digits=20, decimal_places=4, default=0.0)
    total_payment_amount_received = models.DecimalField(max_digits=20, decimal_places=4, default=0.0)
    total_amount_sales = models.DecimalField(max_digits=20, decimal_places=4, default=0.0)

    customer_type = models.CharField(max_length=150, null=True, blank=True)
    customer_level = models.CharField(max_length=50, default='LEVEL-1')

    parents_count = models.PositiveSmallIntegerField(default=0)
    level_3_customer_count = models.PositiveSmallIntegerField(default=0)
    level_2_customer_count = models.PositiveSmallIntegerField(default=0)

    customer_parent_id = models.IntegerField(null=True, blank=True)
    distributor_id = models.IntegerField(null=True, blank=True)

    segment_name = models.CharField(max_length=100, null=True, blank=True)
    segment_discount_value = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)

    pricing_group_id = models.IntegerField(null=True, blank=True)

    whatsapp_opt = models.BooleanField(default=False)
    customer_consent = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    allow_all_staff = models.BooleanField(default=False)
    allow_all_beats = models.BooleanField(default=False)
    allow_all_pro_cat = models.BooleanField(default=False)

    custom_form_data = models.JSONField(default=list, blank=True)
    accounts_sw_info = models.JSONField(default=dict)

    created_at = models.DateTimeField(auto_now_add=True)
