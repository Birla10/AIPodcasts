from locust import HttpUser, TaskSet, task, between

class PodcastTaskSet(TaskSet):
    @task
    def generate_podcast(self):
        payload = {
            "topic": "Technology",
        }
        self.client.post("/generate-podcast/", json=payload)

class PodcastUser(HttpUser):
    tasks = [PodcastTaskSet]
    wait_time = between(1, 5)