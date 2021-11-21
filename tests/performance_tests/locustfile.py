from locust import HttpUser, task


class ProjectPerfTest(HttpUser):
    @task
    def home(self):
        self.client.get("/")

    @task
    def login(self):
        self.client.post("/showSummary", data={"email": "john@simplylift.co"})

    @task
    def logout(self):
        self.client.get('/logout')
