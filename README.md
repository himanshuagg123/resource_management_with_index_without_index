🔍 High-Load Data API with Django
This project demonstrates a Django-based API handling 1 million rows of random data and tests its performance under high concurrency using Locust. It includes data generation, API querying, indexing for optimization, and serving with Gunicorn for production readiness.

🚀 Features
Generates 10 lakh (1 million) rows of realistic random data using a Django management command.

Efficient API endpoint to query the data.

Uses indexing to improve read/query speed.

Load tested with Locust simulating up to 1000 concurrent users.

Uses Gunicorn as the production server.

🏗️ Setup Instructions
1. Clone & Install Dependencies
bash
Copy
Edit
git clone <your-repo-url>
cd data_project
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
2. Migrate the Database
bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
🧪 Generate Test Data
Use the custom management command to populate 1 million rows:

bash
Copy
Edit
python manage.py generate_data
Each record contains fields like user_id, organization_id, contact details, financial data, and segmentation.

🛠️ Admin Configuration
To access and view data in Django Admin:

python
Copy
Edit
# data_app/admin.py

from django.contrib import admin
from .models import LargeData

@admin.register(LargeData)
class LargeDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'name', 'email', 'mobile', 'customer_type')
    search_fields = ('user_id', 'name', 'email')
    list_filter = ('customer_type', 'customer_level', 'segment_name')
Start the admin server:

bash
Copy
Edit
python manage.py createsuperuser
python manage.py runserver
Visit: http://127.0.0.1:8000/admin/

🔗 API Endpoint
URL: /api/run-query/

Method: GET

Example Call:

http
Copy
Edit
GET /api/run-query/?count=1&type=get&user_id=123456
Returns JSON data for the requested user if found.

⚙️ Run with Gunicorn (Production Server)
bash
Copy
Edit
gunicorn data_project.wsgi:application --bind 0.0.0.0:8000 --workers 4
⚡ Load Testing with Locust
Create a locustfile.py with:

python
Copy
Edit
import random
from locust import HttpUser, task

class MyUser(HttpUser):
    host = "http://127.0.0.1:8000"

    @task
    def hit_once_and_stop(self):
        user_id = random.randint(1, 1000000)
        url = f"/api/run-query/?count=1&type=get&user_id={user_id}"

        with self.client.get(url, catch_response=True) as response:
            if response.status_code == 200 and "error" not in response.text:
                response.success()
            else:
                response.failure(f"Failed for user_id={user_id}")
Run Locust:

bash
Copy
Edit
locust -f locustfile.py
Open your browser:

arduino
Copy
Edit
http://localhost:8089
Set:

Number of users: 1000

Spawn rate: 100

Click Start Swarming.

📊 Optimization Techniques Used
Indexing on frequently queried fields like user_id.

Bulk Insertion using bulk_create() for efficient data generation.

Gunicorn server for scalable production serving.

Locust to simulate high concurrent traffic.

✅ Summary
This Django project efficiently manages and serves large-scale data (1 million rows) and is designed to perform under high traffic. Ideal for performance benchmarking, API load testing, and optimization exercises.

Let me know if you'd like to include the actual model structure or performance results from Locust tests!







You said:
remove admin cofigration


ChatGPT said:
Here is the updated README.md file with the Admin Configuration section removed as you requested:

🔍 High-Load Data API with Django
This project demonstrates a Django-based API handling 1 million rows of random data and tests its performance under high concurrency using Locust. It includes data generation, API querying, indexing for optimization, and serving with Gunicorn for production readiness.

🚀 Features
Generates 10 lakh (1 million) rows of realistic random data using a Django management command.

Efficient API endpoint to query the data.

Uses indexing to improve read/query speed.

Load tested with Locust simulating up to 1000 concurrent users.

Uses Gunicorn as the production server.

🏗️ Setup Instructions
1. Clone & Install Dependencies
bash
Copy
Edit
git clone <your-repo-url>
cd data_project
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
2. Migrate the Database
bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
🧪 Generate Test Data
Use the custom management command to populate 1 million rows:

bash
Copy
Edit
python manage.py generate_data
Each record contains fields like user_id, organization_id, contact details, financial data, and segmentation.

🔗 API Endpoint
URL: /api/run-query/

Method: GET

Example Call:

http
Copy
Edit
GET /api/run-query/?count=1&type=get&user_id=123456
Returns JSON data for the requested user if found.

⚙️ Run with Gunicorn (Production Server)
bash
Copy
Edit
gunicorn data_project.wsgi:application --bind 0.0.0.0:8000 --workers 4
⚡ Load Testing with Locust
Create a locustfile.py with:

python
Copy
Edit
import random
from locust import HttpUser, task

class MyUser(HttpUser):
    host = "http://127.0.0.1:8000"

    @task
    def hit_once_and_stop(self):
        user_id = random.randint(1, 1000000)
        url = f"/api/run-query/?count=1&type=get&user_id={user_id}"

        with self.client.get(url, catch_response=True) as response:
            if response.status_code == 200 and "error" not in response.text:
                response.success()
            else:
                response.failure(f"Failed for user_id={user_id}")
Run Locust:

bash
Copy
Edit
locust -f locustfile.py
Open your browser:

arduino
Copy
Edit
http://localhost:8089
Set:

Number of users: 1000

Spawn rate: 100

Click Start Swarming.

📊 Optimization Techniques Used
Indexing on frequently queried fields like user_id.

Bulk Insertion using bulk_create() for efficient data generation.

Gunicorn server for scalable production serving.

Locust to simulate high concurrent traffic.

✅ Summary
This Django project efficiently manages and serves large-scale data (1 million rows) and is designed to perform under high traffic. Ideal for performance benchmarking, API load testing, and optimization exercises.
