class University:

    def __init__(self, university_name, university_address):
        self.university_name = university_name
        self.university_address = university_address
        self.faculties_list = []
        self.faculties_list_names = []

    def get_university_name(self):
        return self.university_name

    def get_university_address(self):
        return self.university_address

    def add_faculty(self, new_faculty):
        if len(self.faculties_list_names) == 0:
            self.faculties_list.append(new_faculty)
            self.faculties_list_names.append(new_faculty.faculty_name)
            print(f"Faculty {new_faculty.faculty_name} was successfully added")
        else:
            if new_faculty.faculty_name in self.faculties_list_names:
                print(f"Faculty {new_faculty.faculty_name} "
                      f" already exists, the name of the faculty should be unique")
            else:
                self.faculties_list.append(new_faculty)
                self.faculties_list_names.append(new_faculty.faculty_name)
                print(f"Faculty {new_faculty.faculty_name} was successfully added")

    def remove_faculty(self, faculty_to_remove):
        for i in self.faculties_list:
            if faculty_to_remove == i.faculty_name:
                self.faculties_list.remove(i)
                self.faculties_list_names.remove(i.faculty_name)
                print(f"Faculty {faculty_to_remove} was removed")





