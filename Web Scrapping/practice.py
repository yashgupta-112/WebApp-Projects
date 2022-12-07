import requests
from requests_html import HTML
import pandas as pd
import os

url ="https://www.boxofficemojo.com/year/world/"

# r = requests.get(url)
# print(r.status_code)
# print(r.text)

def url_file(url , filename="text.html"):
    r = requests.get(url)
    if r.status_code == 200:
        html_text = r.text
        with open(filename,'w') as f:
            f.write(html_text)
        return html_text
    return ""
url_file(url)