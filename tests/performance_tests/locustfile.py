from locust import HttpUser, task


class ProjectPerfTest(HttpUser):
    @task
    def home(self):
        self.client.get("/")

    @task
    def login(self):
        self.client.post("/showSummary", data={"email": "john@simplylift.co"})
    
    @task
    def get_book(self):
        self.client.get('/book/Spring Festival/Simply Lift')
    
    @task
    def purchase_place(self):
        self.client.post('/purchasePlaces', data={"club": "Simply Lift", "competition": "Spring Festival", "places": 3})

    @task
    def logout(self):
        self.client.get('/logout')
