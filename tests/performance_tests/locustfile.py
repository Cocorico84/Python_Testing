from locust import HttpUser, task 

class ProjectPerfTest(HttpUser):
    @task
    def home(self):
        response = self.client.get("/")
        
    
    @task
    def login(self):
        response = self.client.post("/showSummary", data={"email": "john@simplylift.co"})