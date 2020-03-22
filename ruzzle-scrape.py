import requests
from bs4 import BeautifulSoup
from itertools import chain
import pandas as pd
from tqdm import tqdm

def scrape_page(pagenum):
    '''
    Returns a list of words for a page number
    :param pagenum Page number of the all words page.
    :returns List of words for that page
    '''
    URL=f'http://www.ruzzleleague.com/boards/all-words/page-{pagenum}/'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    tables = soup.find('table')
    tds = tables.find_all('td')
    words = [word.text for word in tds[0:len(tds):4]]
    return words


if __name__=='__main__':
    '''
    Manually setting the final page limit as of now.
    '''
    all_words = []
    for page in tqdm(range(1,497)):
        words = scrape_page(page)
        all_words.append(words)
    all_words_unlist = chain(*all_words)
    df = pd.DataFrame({"words": all_words_unlist})
    df.to_csv("./ruzzle_words.csv", index=False)



