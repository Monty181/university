import specialty
import university
import faculty
import group
import student
from menu import Menu


def main():
    university_name = input("Hi! To create the university enter the name of the university:\n ")
    university_address = input("Now input the address of the university:\n")
    my_university = university.University(university_name, university_address)
    print("\nUniversity was successfully created")

    choice = 0

    while choice != 6:
        Menu.print_main_menu()
        choice = int(input("Input the number of menu item: \n"))

        if choice == 1:
            if Menu.choose_faculties_menu() == 1:
                my_university.add_faculty(faculty.Faculty(str(input("Please Enter the name of the faculty: \n"))))
            elif Menu.choose_faculties_menu() == 2:
                my_university.remove_faculty(str(input("Please enter name of faculty you want to remove: \n")))
            else:
                print("You input incorrect number, try again")

        elif choice == 2:
            if Menu.choose_specialty_menu() == 1:
                chosen_faculty = str(input(f"Please enter the name of faculty you want to add new specialty:\n"))
                for i in my_university.faculties_list:
                    if i.faculty_name == chosen_faculty:
                        i.add_new_specialty(specialty.Specialty(str(input("Please enter specialty name:\n")), i))
            elif Menu.choose_specialty_menu() == 2:
                chosen_faculty = str(input(f"Please enter the name of faculty you want to remove specialty:\n"))
                for i in my_university.faculties_list:
                    if i.faculty_name == chosen_faculty:
                        i.remove_specialty(str(input("Please enter the name of the specialty you want to remove:\n")))
            else:
                print("You input incorrect number, try again")

        elif choice == 3:
            if Menu.choose_group_menu() == 1:
                chosen_faculty = str(input(f"Please enter the name of faculty you want to add new group:\n"))
                for i in my_university.faculties_list:
                    if i.faculty_name == chosen_faculty:
                        chosen_specialty = str(input(f"Please enter the name of specialty you want to add new group:\n"))
                        for j in i.specialty_list:
                            if j.specialty_name == chosen_specialty:
                                j.add_new_group(group.Group(str(input("Please enter group name:\n")), i, j))
            elif Menu.choose_group_menu() == 2:
                chosen_faculty = str(input(f"Please enter the name of faculty you want to remove group:\n"))
                for i in my_university.faculties_list:
                    if i.faculty_name == chosen_faculty:
                        chosen_specialty = str(
                            input(f"Please enter the name of specialty you want to remove group:\n"))
                        for j in i.spetialty_list:
                            if j.specialty_name == chosen_specialty:
                                j.remove_group(str(input("Please enter group name you want to remove:\n")))
            else:
                print("You input incorrect number, try again")

        elif choice == 4:
            if Menu.choose_student_menu() == 1:
                chosen_faculty = str(input(f"Please enter the name of faculty you want to add new student:\n"))
                for i in my_university.faculties_list:
                    if i.faculty_name == chosen_faculty:
                        chosen_specialty = str(
                            input(f"Please enter the name of specialty you want to add new student:\n"))
                        for j in i.specialty_list:
                            if j.specialty_name == chosen_specialty:
                                chosen_group = str(input(f"Please enter the group you want to add new student:\n"))
                                for y in j.group_list:
                                    if y.group_name == chosen_group:
                                        y.add_new_student(student.Student(str(input("Please enter student's name:\n")),
                                                                          str(input("Please enter student's last name:\n")),
                                                                          str(input("Please enter student's phone number:\n")),
                                                                          i, j, y))
            elif Menu.choose_student_menu() == 2:
                chosen_faculty = str(input(f"Please enter the name of faculty you want to remove student:\n"))
                for i in my_university.faculties_list:
                    if i.faculty_name == chosen_faculty:
                        chosen_specialty = str(
                            input(f"Please enter the name of specialty you want to remove student:\n"))
                        for j in i.specialty_list:
                            if j.specialty_name == chosen_specialty:
                                chosen_group = str(
                                    input(f"Please enter the group you want to remove student:\n"))
                                for y in j.group_list:
                                    if y.group_name == chosen_group:
                                        y.remove_student(str(input("Please enter student's full name you want to remove:\n")))
            else:
                print("You input incorrect number, try again")

        elif choice == 5:
            Menu.choose_report_menu()
        elif choice == 6:
            print("Bye")
            break
        else:
            print("You input incorrect number, try again")


if __name__ == '__main__':
    main()
