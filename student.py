

class student:
    def __init__(self, name, education, phone):
        self.name = name
        self.education = education
        self.phone = phone

    def get_student(self):
        answer = f"\t{self.name}\n\t\t{self.education}\n\t\t{self.phone}"
        return answer