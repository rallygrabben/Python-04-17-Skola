

class student:
    def __init__(self, name, education, phone):
        self.name = name
        self.education = education
        self.phone = phone

    def get_student(self):
        answer = f"{self.name}\n\t    - Education: {self.education}\n\t    - Phone  Nr: {self.phone}\n\n"
        return answer