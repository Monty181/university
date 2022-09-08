class Specialty:

    def __init__(self, specialty_name, faculty):
        self.specialty_name = specialty_name
        self.group_list = []
        self.group_list_names = []
        self.faculty = faculty

    def get_specialty_name(self):
        return self.specialty_name

    def add_new_group(self, new_group):
        if len(self.group_list_names) == 0:
            self.group_list.append(new_group)
            self.group_list_names.append(new_group.group_name)
            print(f"group {new_group.group_name} was successfully added")
        else:
            if new_group.group_name in self.group_list_names:
                print(f"group {new_group.group_name} "
                      f" already exists, the name of the group should be unique")
            else:
                self.group_list.append(new_group)
                self.group_list_names.append(new_group.group_name)
                print(f"group {new_group.group_name} was successfully added")

    def remove_group(self, group_to_remove):
        for i in self.group_list:
            if group_to_remove == i.group_name:
                self.group_list.remove(i)
                self.group_list_names.remove(i.group_name)
                print(f"group {group_to_remove} was removed")





