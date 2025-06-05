import os
import django
import threading
import time
import random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "data_project.settings")
django.setup()

from data_app.models import LargeData

def run_query():
    uid = random.randint(1, 10000)  # Simulate real usage
    _ = LargeData.objects.filter(user_id=uid).values('name', 'user_id').first()

threads = []
num_queries = 900

start = time.time()

for _ in range(num_queries):
    t = threading.Thread(target=run_query)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

end = time.time()

print(f"Executed {num_queries} filtered queries in {end - start:.2f} seconds.")
