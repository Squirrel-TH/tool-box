import requests
from bs4 import BeautifulSoup
import pandas as pd
from collections import OrderedDict


class UseBeautifulSoup:
    def __init__(self, url):
        self.url = url

    def get_soup(self) -> BeautifulSoup:
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup

    def display_html_layers(self, soup: BeautifulSoup) -> None:
        print(soup.prettify())


# plese set URL
URL = ''

use_beautiful_soup = UseBeautifulSoup(URL)
tag = 'dd ul li p a.TextLinkWrapper_t1bvfs58'
elements = use_beautiful_soup.get_soup().select(tag)

computer_science_classes = []
for element in elements:
    class_name = element.get_text(strip=True)
    computer_science_classes.append(class_name)

# remove duplicate
unique_computer_science_classes = list(
    OrderedDict.fromkeys(computer_science_classes)
)

df = pd.DataFrame(unique_computer_science_classes)
csv_file_name = ''
df.to_csv(csv_file_name, index=False, header=False)
