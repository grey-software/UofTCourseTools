import requests, re, json
from bs4 import BeautifulSoup, element
from subject import Subject
from program import Program
from subject_group import Subject_Group
from typing import Dict, List, Set
from tqdm import tqdm  # progress bar magic


def create_subject_groups() -> List[Subject_Group]:
    all_subject_groups = []
    source = requests.get("https://www.utm.utoronto.ca/programs-departments").text
    soup = BeautifulSoup(source, 'lxml')
    subject_group_soups = soup.find('div', id='main-wrapper').find('div', id='content').find('div', class_='region region-content').find('p').find_all('b')[1:-2]

    for subject_group_soup in subject_group_soups:
        curr_subject_group = Subject_Group()
        curr_subject_group.set_name(subject_group_soup.text.replace('\xa0', " "))
        next_line_soup = subject_group_soup.next_sibling

        while(not group_title_reached(next_line_soup)):
            if isinstance(next_line_soup, element.Tag) and next_line_soup.get('href') is not None:
                # print(next_line_soup.text.split(' (')[0].replace('and', '&'))
                curr_subject_group.add_all_subject_names(next_line_soup.text.split(' ')[0].strip(','))

            next_line_soup = next_line_soup.next_sibling


        all_subject_groups.append(curr_subject_group)
        print(curr_subject_group.all_subject_names)
    
    return all_subject_groups


# test if a subject is no longer offered
def subject_exists(url: str) -> bool:
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    exist = soup.find('div', class_='centralpos').find('div', class_='contentpos').find(
        'dl', class_='title2')  # if the there are any program advisors
    return exist is not None


# test if a subject is no longer offered
def program_exists(code_name_level: List[str], all_program_types: Dict[str, str]) -> bool:
    return all_program_types.get(code_name_level[0]) is not None


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


# test if a program title is reached
def title_reached(test_soup) -> bool:
    return isinstance(test_soup, element.Tag) and test_soup.name == 'p' and test_soup['class'][0] == "title_program"


# test if a group title is reached
def group_title_reached(test_soup) -> bool:
    return isinstance(test_soup, element.Tag) and test_soup.name == 'b'


# return a dictionary with the code of the program as the key and its type as the value
def get_all_program_types() -> Dict[str, str]:
    url = "https://www.utm.utoronto.ca/registrar/office-registrar-publications/program-selection-guide"
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    program_list_soup = soup.find(
        'table', cellpadding="0").tbody.find_all('tr')[1:]
    type_dict = {}

    for type_soup in program_list_soup:
        type_soup = type_soup.find_all('td')[3:5]
        type_dict[type_soup[0].text.strip(
            '\n')] = type_soup[1].text.strip('\n')

    return type_dict


# finds the program name, code and its level
def get_code_name_level(scraped_program_title: str) -> List[str]:

    normal_pattern = "[A-Z]{5}[0-9]{4}"
    weird_pattern = "[A-Z]{9}[0-9A-Z]"
    curr_pattern = normal_pattern
    all_values = []

    if len(re.findall(curr_pattern, scraped_program_title)) == 0:
        curr_pattern = weird_pattern

    all_values.append(re.findall(curr_pattern, scraped_program_title)[0])
    all_values.append(re.split(curr_pattern, scraped_program_title)[1])
    level_section = re.split(curr_pattern, scraped_program_title)[0]

    if "Specialist" in level_section:
        all_values.append("Specialist")
    elif "Major" in level_section:
        all_values.append("Major")
    elif "Minor" in level_section:
        all_values.append("Minor")

    return all_values


# this is the group id of every subject in UTM
subject_ids = all_subject_ids(
    "https://student.utm.utoronto.ca/calendar//program_list.pl")

all_program_types = get_all_program_types() # gets the type of every program

# subject_ids = ["9"]

all_subject_groups = create_subject_groups()

for subject_id in tqdm(subject_ids):

    url = "https://student.utm.utoronto.ca/calendar//program_group.pl?Group_Id=" + subject_id
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    all_degrees = ["HBA", "HBSc", "BBA", "BCom"]

    if subject_exists(url):
        curr_subject = Subject()
        title = soup.find('p', class_='titlestyle')
        body = soup.find('div', class_='centralpos').find(
            'div', class_='contentpos')
        notes = body.find('ol', class_="numbers")
        programs = body.find_all('p', class_="title_program")

        if notes is not None:
            notes = notes.find_all('li')

        curr_subject.set_name(title.text.split(' (')[0].replace('and', '&'))

        for degree in all_degrees:
            if degree in title.text:
                curr_subject.add_degree(degree)

        if notes is not None:
            for note in notes:
                curr_subject.add_note(note.text.replace("\r", "").strip())

        for program_soup in programs:
            curr_program = Program()
            code_name_level = get_code_name_level(program_soup.text)

            # if program doesn't exist, don't include it
            if not program_exists(code_name_level, all_program_types):
                continue

            code_name_level = get_code_name_level(program_soup.text)

            # setting subject code, name, level and type
            curr_program.set_code(code_name_level[0])
            curr_program.set_name(code_name_level[1])
            curr_program.set_level(code_name_level[2])
            curr_program.set_program_type(all_program_types[curr_program.code])


            next_line_soup = program_soup.next_sibling
            while(not title_reached(next_line_soup)):

                if isinstance(next_line_soup, element.Tag):

                    # notes of the program
                    if next_line_soup.name == 'div' and next_line_soup['class'][0] == "lim_enrol":
                        all_notes = next_line_soup.find_all('li')

                        if all_notes is not None:
                            for note_soup in all_notes:
                                curr_program.add_note(note_soup.text.replace(
                                    "\r", "").replace("\t", "").strip())

                    # courses of the program
                    all_courses = next_line_soup.find_all('a')
                    if all_courses is not None:
                        for course_soup in all_courses:
                            if len(course_soup.text) == 8:
                                curr_program.add_course(course_soup.text)

                # reached the end of the page
                if next_line_soup is None:
                    break
                else: # keep going
                    next_line_soup = next_line_soup.next_sibling

            curr_subject.add_program(curr_program)

        for group in all_subject_groups:
            if group.subject_in_group(curr_subject.name.split(' ')[0].replace(',','')):
                group.add_subject(curr_subject)
                continue

            # write subject_group to json file
            with open('../output/subject_groups/' + group.name + '.json', 'w') as file:
                json.dump(group.to_json(), file)


        # write subject to json file
        with open('../output/subjects/' + curr_subject.name + '.json', 'w') as file:
            json.dump(curr_subject.to_json(), file)
