class Faculty:

    def __init__(self, faculty_name):
        self.faculty_name = faculty_name
        self.specialty_list = []
        self.specialty_list_names = []

    def get_faculty_name(self):
        return self.faculty_name

    def add_new_specialty(self, new_specialty):
        if len(self.specialty_list_names) == 0:
            self.specialty_list.append(new_specialty)
            self.specialty_list_names.append(new_specialty.specialty_name)
            print(f"specialty {new_specialty.specialty_name} was successfully added")
        else:
            if new_specialty.specialty_name in self.specialty_list_names:
                print(f"specialty {new_specialty.specialty_name} "
                      f" already exists, the name of the specialty should be unique")
            else:
                self.specialty_list.append(new_specialty)
                self.specialty_list_names.append(new_specialty.specialty_name)
                print(f"specialty {new_specialty.specialty_name} was successfully added")

    def remove_specialty(self, specialty_to_remove):
        for i in self.specialty_list:
            if specialty_to_remove == i.specialty_name:
                self.specialty_list.remove(i)
                self.specialty_list_names.remove(i.specialty_name)
                print(f"specialty {specialty_to_remove} was removed")


