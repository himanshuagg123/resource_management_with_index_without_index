import os
import django
import threading
import time
import random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "data_project.settings")
django.setup()

from data_app.models import LargeData

def run_get_query():
    uid = random.randint(1, 1000000)  # Each thread uses a different user_id
    try:
        obj = LargeData.objects.get(user_id=uid)
        _ = (obj.name, obj.user_id)  # simulate accessing fields
    except LargeData.DoesNotExist:
        pass  # No user with this ID
    except LargeData.MultipleObjectsReturned:
        pass  # Not unique — skip or log if needed

threads = []
num_queries = 900

start = time.time()

for _ in range(num_queries):
    t = threading.Thread(target=run_get_query)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

end = time.time()

print(f"Executed {num_queries} random `.get()` queries in {end - start:.2f} seconds.")
