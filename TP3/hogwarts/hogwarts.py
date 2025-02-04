from typing import List
from characters.wizard import Wizard
from magical_items.abstract_magical_item import AbstractMagicalItem

class Hogwarts:
    def __init__(self):
        self.students: List[Wizard] = []
        self.magical_artifacts: List[AbstractMagicalItem] = []

    def enroll_student(self, wizard: Wizard):
        self.students.append(wizard)

    def create_magical_artifact(self, artifact: AbstractMagicalItem):
        self.magical_artifacts.append(artifact)

    def display_students(self):
        for student in self.students:
            print(f"Student: {student.name}, Magic Type: {student.magic_type}")