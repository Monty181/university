class Group:

    def __init__(self, group_name, faculty, specialty):
        self.group_name = group_name
        self.students_list = []
        self.students_full_name = []
        self.faculty = faculty
        self.specialty = specialty

    def get_group_name(self):
        return self.group_name

    def add_new_student(self, new_student):
        if len(self.students_full_name) == 0:
            self.students_list.append(new_student)
            self.students_full_name.append(f"{new_student.student_name} {new_student.student_last_name}")
            print(f"group {new_student.student_name} {new_student.student_last_name} was successfully added")
        else:
            if new_student.get_student_full_name() in self.students_full_name:
                print(f"group {new_student.get_student_full_name()} "
                      f" already exists, the name of the group should be unique")
            else:
                self.students_list.append(new_student)
                self.students_full_name.append(new_student.get_student_full_name())
                print(f"group {new_student.get_student_full_name()} was successfully added")

    def remove_student(self, student_to_remove):
        for i in self.students_list:
            if student_to_remove == i.get_student_full_name():
                self.students_list.remove(i)
                self.students_full_name.remove(i.get_student_full_name())
                print(f"student {student_to_remove} was removed")


