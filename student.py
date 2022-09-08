class Student:

    def __init__(self, student_name, student_last_name, student_contact_phone, faculty, specialty, group):
        self.student_name = student_name
        self.student_last_name = student_last_name
        self.student_contact_phone = student_contact_phone
        self.faculty = faculty
        self.specialty = specialty
        self.group = group

    def get_student_name(self):
        return self.student_name

    def get_student_last_name(self):
        return self.student_last_name

    def get_student_contact_phone(self):
        return self.student_contact_phone

    def get_student_full_name(self):
        full_name = str(f"{self.student_name} {self.student_last_name}")
        return full_name
