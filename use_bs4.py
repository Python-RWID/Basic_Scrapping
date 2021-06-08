import requests
# requests.get('https://detik.com')
from bs4 import BeautifulSoup

com = 'https://detik.com'
try:
    response = requests.get(com)
    if response.status_code == 200:
        print(f'Success! Response = {response.status_code}')
        # print(f'Content{response.text}') memperoses data dengan bs4
        soup = BeautifulSoup(response.text, features="html.parser")
        print(f'hasil pemanggilan {com}')
        print(f'Title : {soup.title.string}') #modified for scrapping
    else:
        print(f'Upss, ada kesalahan request {response.status_code}')
    # print(f'success,{response}')
    # print(f'Content {response.text}')
except Exception as a:
    print(f'There is an error {a}')
print(f'program ended')
