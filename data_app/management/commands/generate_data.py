import random
import string
from django.core.management.base import BaseCommand
from data_app.models import LargeData

def random_string(length=10):
    return ''.join(random.choices(string.ascii_letters, k=length))

class Command(BaseCommand):
    help = 'Generate 10 lakh rows of random data'

    def handle(self, *args, **kwargs):
        batch_size = 10000
        total = 1000000

        for i in range(0, total, batch_size):
            objs = [
                LargeData(
                    name=random_string(12),
                    organization_id=random.randint(1, 10000),
                    user_id=random.randint(1, 10000),
                    pan_id=random_string(10),
                    gstin=random_string(15),
                    customer_code=random_string(10),
                    contact_person_name=random_string(15),
                    contact_mobile=f"{random.randint(7000000000, 9999999999)}",
                    email=f"{random_string(5)}@example.com",
                    country_code="+91",
                    mobile=f"{random.randint(7000000000, 9999999999)}",
                    is_whatsapp_verified=random.choice([True, False]),
                    payment_term=random.choice(["NET30", "NET60", "COD"]),
                    credit_limit=random.uniform(1000, 100000),
                    outstanding_amount=random.uniform(0, 50000),
                    total_payment_amount_received=random.uniform(0, 200000),
                    total_amount_sales=random.uniform(1000, 1000000),
                    customer_type=random.choice(["Retail", "Wholesale", "Distributor"]),
                    customer_level=random.choice(["LEVEL-1", "LEVEL-2", "LEVEL-3"]),
                    parents_count=random.randint(0, 5),
                    level_3_customer_count=random.randint(0, 10),
                    level_2_customer_count=random.randint(0, 10),
                    customer_parent_id=random.randint(1, 50000),
                    distributor_id=random.randint(1, 50000),
                    segment_name=random.choice(["North", "South", "East", "West"]),
                    segment_discount_value=random.uniform(0, 10),
                    pricing_group_id=random.randint(1, 50),
                    whatsapp_opt=random.choice([True, False]),
                    customer_consent=random.choice([True, False]),
                    is_active=True,
                    allow_all_staff=random.choice([True, False]),
                    allow_all_beats=random.choice([True, False]),
                    allow_all_pro_cat=random.choice([True, False]),
                    custom_form_data=[{"field": "value"}],
                    accounts_sw_info={"master_id": random.randint(1000, 9999)},
                ) for _ in range(batch_size)
            ]
            LargeData.objects.bulk_create(objs)
            print(f"Inserted {i + batch_size} records")
