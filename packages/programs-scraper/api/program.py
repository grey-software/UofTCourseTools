import json
from typing import List, Dict, Union


class Program:

    """
    A class for storing specific information regarding each specialization
    """

    name: str
    level: str
    code: str
    notes: List[str]
    courses: Dict[int, Union[List[str]]]
    program_type: str

    def __init__(self):
        self.name = ""
        self.level = ""
        self.code = ""
        self.notes = []
        self.program_type = -1
        self.courses = {1: [], 2: [], 3: [], 4: []}

    def set_name(self, name: str):
        self.name = name

    def set_level(self, level: str):
        self.level = level

    def set_code(self, code: str):
        self.code = code

    def add_note(self, note: str):
        self.notes.append(note)
    
    def add_course(self, course: str):
        if course not in self.courses[int(course[3])]:
            self.courses[int(course[3])].append(course)
    
    def set_program_type(self, program_type: str):
        self.program_type = program_type

    def to_json(self):
        for i in range(1, 5):
            self.courses[i].sort()
        
        curr_json = {
            "name": self.name,
            "level": self.level,
            "code": self.code,
            "type": self.program_type,
            "notes": self.notes,
            "courses": self.courses
        }
        return curr_json
