import random
from locust import HttpUser, task

class MyUser(HttpUser):
    host = "http://127.0.0.1:8000"

    @task
    def hit_once_and_stop(self):
        user_id = random.randint(1, 1000000)  # Adjust range as needed
        url = f"/api/run-query/?count=1&type=get&user_id={user_id}"

        with self.client.get(url, catch_response=True) as response:
            if response.status_code == 200 and "error" not in response.text:
                response.success()
            else:
                response.failure(f"Failed for user_id={user_id}")

        # self.environment.runner.quit()
