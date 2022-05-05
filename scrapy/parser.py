import requests
from bs4 import BeautifulSoup
from django.views.decorators.csrf import csrf_exempt

HOST = "https://www.fake-plants.co.uk/"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0"
}


@csrf_exempt
def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


@csrf_exempt
def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("li", class_="product-category product")
    plants = []

    for item in items:
        plants.append(
            {
                "title": item.find("h2", class_="woocommerce-loop-category__title").get_text(strip=True),
                "image": item.find("a").find("img").get("src"),
            }
        )
    return plants


@csrf_exempt
def parser_func():
    html = get_html(HOST)
    if html.status_code == 200:
        anime = []
        for page in range(0, 1):
            html = get_html(HOST)
            anime.extend(get_data(html.text))
        return anime

