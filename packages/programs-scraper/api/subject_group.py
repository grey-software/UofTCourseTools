from typing import List, Dict, Set
from subject import Subject


class Subject_Group:

    """
    A class for storing groups of subjects
    """

    group_name: str
    group: List[Subject]
    all_subject_names: Set[str]

    def __init__(self):
        self.group_name = ""
        self.group = []
        self.all_subject_names = set()

    def set_name(self, name: str):
        self.name = name

    def add_all_subject_names(self, subject_name: str):
        if subject_name != "":
            if not subject_name[0].islower():
                self.all_subject_names.add(subject_name)

    def add_subject(self, subject: Subject):
        self.group.append(subject)
    
    def subject_in_group(self, subject_name: str) -> bool:
        return subject_name in self.all_subject_names

    def to_json(self):
        curr_json = {
            "name": self.name,
            "group": [],
        }
        for subject in self.group:
            curr_json["group"].append(subject.to_json())

        return curr_json
