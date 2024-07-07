from locust import HttpUser, task, between
from random import randint, choice
from string import ascii_lowercase


class WebsiteUser(HttpUser):
    wait_time = between(1, 5)
    @task(4)
    def view_links(self):
        movie_id = randint(1, 5200)
        self.client.get(f'/api/links/?movie_id={movie_id}', name='/api/links')

    @task(4)
    def view_movies(self):
        movie_name = choice(ascii_lowercase)
        print(movie_name)
        self.client.get(f'/api/movies/?search={movie_name}', name='/api/movies')