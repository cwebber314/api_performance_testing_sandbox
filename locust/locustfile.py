"""

To run:

    locust

Then open http://localhost:8089

In the locust UI:
- click start 
"""
from locust import HttpUser, task

class HelloWorldUser(HttpUser):

    def on_start(self):
        # self.client.headers = {'Authorization': 'my-auth-token'}
        self.client.headers = {'token': 'foo'}

    host = "http://localhost:8000"  
    @task
    def hello_world(self):
        self.client.get("/hello")
        self.client.get("/world")
        self.client.get("/get100")
        self.client.get("/get1000")