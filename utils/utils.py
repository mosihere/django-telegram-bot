import re
import requests
from movies.models import Movie




movie = Movie.objects.get(id=1)
print(movie)


def get_links(record: tuple):
    url = record[1]
    movie_name = record[2]
    response = requests.get(url)
    links = re.findall(r'https://.*kingupload.*mkv', response.text)
    links_page = re.findall(r'https://.*kingupload.*[0-9]/', response.text)

    qualities = find_movie_quality(links)
    get_seasons = find_series_season(links_page)

    if links and links_page and get_seasons and qualities:
        sorted_season = sorted(list(set(get_seasons)))
        sorted_links_page = sorted(list(set(links_page)))
        
        return links, movie_name, qualities, sorted_links_page, sorted_season
    
    elif links or links_page and not get_seasons:
        return links, movie_name, qualities
    
    elif links_page and not links:
        return links_page, movie_name, get_seasons
    
    else:
        return ''


def find_movie_quality(links: list) -> None:

    quality = re.findall(r'[0-9]{3,4}[p]', ' '.join(links))

    return quality


def find_series_season(links: list):
   
   season = re.findall(r'S\d{2}', ' '.join(links))

   return season



# print(get_links((1,'https://www.f2m12.top/1525/the-revenant-2015-farsi-dubbed', 'the-revenant-2015-farsi-dubbed', None)))