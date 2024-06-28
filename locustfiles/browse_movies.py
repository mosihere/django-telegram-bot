from locust import HttpUser, task, between
from random import randint


class WebsiteUser(HttpUser):
    wait_time = between(1, 5)
    @task(2)
    def view_links(self):
        movie_id = randint(1, 104)
        self.client.get(f'/api/links/?movie_id={movie_id}', name='/api/links')

    @task(4)
    def view_link(self):
        link_id = randint(187, 688)
        self.client.get(f'/api/links/{link_id}/', name='/api/links/:id/')