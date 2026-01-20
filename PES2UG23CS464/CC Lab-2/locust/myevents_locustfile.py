from locust import HttpUser, task, between

class MyEventsUser(HttpUser):
    wait_time = between(1, 2)
    
    # Configuration
    USER_PARAM = "locust_user"

    @task
    def view_my_events(self):
        """Simulate viewing my events page"""
        with self.client.get(
            f"/my-events?user={self.USER_PARAM}",
            catch_response=True,
            name="/my-events"
        ) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Failed with status code: {response.status_code}")
