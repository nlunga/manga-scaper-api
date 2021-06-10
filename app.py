from flask import Flask
from flask.scaffold import F
import requests
from bs4 import BeautifulSoup
# import json
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/manga/<name>/<chapter>')
def get_manga_images(name, chapter):
    page = requests.get('https://earlymanga.org/manga/'+name.strip().replace(" ", "-")+'/chapter-'+chapter)
    content = page.content
    soup = BeautifulSoup(content, 'lxml')
    images = soup.find_all('img')

    output = []
    image_src = ''
    index = 0
    for image in images:
        image_src = 'https://earlymanga.org'+image['src']
        output.append(image_src)
        index += 1
    return {'images': output}
