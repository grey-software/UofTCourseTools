import requests
from bs4 import BeautifulSoup
from typing import Set
from tqdm import tqdm # progress bar magic 


# test if a subject is no longer offered
def subject_exists(url: str) -> bool:
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    exist = soup.find('div', class_='centralpos').find('div', class_='contentpos').find(
        'dl', class_='title2')  # if the there are any program advisors
    return exist is not None

# finds all the subject ids
def all_subject_ids(url: str) -> Set[str]:
    ids = set()
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    subject_groups = soup.find('div', class_='centralpos').find(
        'div', class_='contentpos').find_all('div', class_='normaltext')[1].find_all('ul')

    for subject_group in subject_groups:
        for subject in subject_group.find_all('li'):
            subject_id = subject.a['href'].split('=')[1]
            ids.add(subject_id)
    return ids


ids = all_subject_ids("https://student.utm.utoronto.ca/calendar//program_list.pl")

# clear the file
with open('../output/dead_subjects.txt', 'a') as file:
            file.write("")

for subject_id in tqdm(ids):
    url = "https://student.utm.utoronto.ca/calendar//program_group.pl?Group_Id=" + subject_id
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    title = soup.find('p', class_='titlestyle')

    if not subject_exists(url):
        with open('../output/dead_subjects.txt', 'a') as file:
            file.write(title.text.split(' (')[0] + '\n')