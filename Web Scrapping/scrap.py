import requests
from requests_html import HTML
import pandas as pd
import os

BASE_DIR = os.path.dirname(__file__)
def url_to_txt(url, filename="world.html", save=False):
    r = requests.get(url)
    if r.status_code == 200:
        html_text = r.text
        if save:
            with open(f"world.html", 'w') as f:
                f.write(html_text)
        return html_text
    return None

url ="https://www.boxofficemojo.com/year/world/"
def parse_and_extract(url, name='2020'):
    html_text = url_to_txt(url)
    if html_text == None:
        return False
    r_html = HTML(html=html_text)
    table_class = ".imdb-scroll-table"
    r_table = r_html.find(table_class)
    table_data = []
    header_names = []
    if len(r_table) == 0:
        return False
    parsed_table = r_table[0]
    rows = parsed_table.find("tr")
    header_row = rows[0]
    header_cols = header_row.find('th')
    header_names = [x.text for x in header_cols]
    for row in rows[1:]:
        cols = row.find("td")
        row_data = []
        table_data_dicts=[]
        row_dict_data = {}
        for i, col in enumerate(cols):
            header_name = header_names[i]
            row_data.append(col.text)
            table_data_dicts.append(row_dict_data)
        table_data.append(row_data)
    df = pd.DataFrame(table_data, columns=header_names)
    df.to_csv("movie.csv", index=False)
    return True
parse_and_extract(url)