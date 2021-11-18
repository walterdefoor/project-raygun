import requests
import os
import time
import logging
import pdfkit
import dotenv
import pandas as pd
from readability import Document
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


dotenv.load_dotenv()

logging.basicConfig(level=logging.INFO, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.info('Program Start')

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
BEARER_TOKEN = os.getenv('WESEARCH_BEARER_TOKEN')
WESEARCH_DB = os.getenv('WESEARCH_DB')


def upload_doc(filename, filelocation):
    files = {'file': (filename, open(filelocation, 'rb'))}
    headers = {
        'Authorization': 'Bearer TOKENHERE'
    }

    response = requests.post(str('https://project-apollo-api.stg.gc.casetext.com/v0/' + WESEARCH_DB),
                             files=files,
                             headers=headers)
    logging.info(str("Submitted " + filename + " from " + filelocation))
    logging.info(response.json())
    return


def strip_chars(string):
    special_char_string = ''.join(item for item in string if not (item.isalnum() or item.isspace()))
    return special_char_string


def main():
    df = pd.read_json('links.jsonl', lines=True)
    count = 0
    options = Options()
    options.headless = True
    browser = webdriver.Firefox(options=options)

    for index, row in df.iterrows():
        browser.get(row['url_to'])
        html = browser.page_source

        doc = Document(html)

        pdfkit.from_string(doc.summary(), 'temp.pdf')

        if len(row['link_text']) > 1:
            filename = row['link_text']
        else:
            filename = strip_chars('url_to')

        upload_doc(str(doc.title().replace("/", "") + ".pdf"), os.path.join(THIS_FOLDER, 'temp.pdf'))
        count += 1
        print(count)

    return


if __name__ == '__main__':
    start_time = time.time()
    print("Beep beep boop boop starting")
    main()
    elapsed_time = time.time() - start_time
    print(time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))