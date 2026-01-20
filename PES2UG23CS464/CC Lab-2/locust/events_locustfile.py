from locust import HttpUser, task, between

class EventsUser(HttpUser):
    wait_time = between(1, 2)
    
    # Configuration
    USER_PARAM = "locust_user"
    
    @task
    def view_events(self):
        """Simulate viewing events page"""
        with self.client.get(
            f"/events?user={self.USER_PARAM}",
            catch_response=True,
            name="/events"
        ) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Failed with status code: {response.status_code}")
