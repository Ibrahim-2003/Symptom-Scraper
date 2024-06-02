import os
from unicodedata import decomposition
import urllib.request
import time
import pyperclip
os.system('color a')

def getDescription(disease):
    url = f'https://google.com/search?q=is+{disease}+a+virus'

    # Perform the request
    request = urllib.request.Request(url)

    # Set a normal User Agent header, otherwise Google will block the request.
    request.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')
    raw_response = urllib.request.urlopen(request).read()

    # Read the repsonse as a utf-8 string
    html = raw_response.decode("utf-8")


    from bs4 import BeautifulSoup

    # The code to get the html contents here.

    soup = BeautifulSoup(html, 'html.parser')

    result = soup.find("span", {"class":"hgKElc"})
    if result is None:
        return None
    result = result.text
    return result

def getSymptoms(disease):
    url = f'https://google.com/search?q={disease}+symptoms'

    # Perform the request
    request = urllib.request.Request(url)

    # Set a normal User Agent header, otherwise Google will block the request.
    request.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')
    raw_response = urllib.request.urlopen(request).read()

    # Read the repsonse as a utf-8 string
    html = raw_response.decode("utf-8")


    from bs4 import BeautifulSoup

    # The code to get the html contents here.

    soup = BeautifulSoup(html, 'html.parser')

    result = soup.find("div", {"id":"ddTead"})
    if result is None:
        return None
    result = result.text
    return result

queries = ['Ebola', 'Salmonella', 'Chikungunya Virus', 'Enterovirus', 'Influenza', 'Listeria''Measles', 'Meningitis', 'Middle East Respiratory Syndrome', 'Mumps', 'Zika']


summary = ''
for query in queries:
    query = query.replace(' ', '+')
    solution = getSymptoms(query)
    description = getDescription(query)
    if solution != None:
        query = query.replace('+', ' ')
        summary += f'{query} = {description}\nSymptoms for {query}: {solution}\n---------------------------------\n\n'
    else:
        pass
pyperclip.copy(summary)
print(summary)
input()