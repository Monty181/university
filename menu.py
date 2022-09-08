class Menu:

    @staticmethod
    def print_main_menu():
        main_menu = ("""
        1. Faculties
        2. Specialties
        3. Groups
        4. Students
        5. Reports
        6. Exit
        """)
        print(main_menu)

    @staticmethod
    def choose_faculties_menu():
        faculty_menu = int(input("""
        1. Add new faculty
        2. Remove faculty
        
        Enter number of menu item: 
        """))
        return faculty_menu

    @staticmethod
    def choose_specialty_menu():
        specialty_menu = int(input("""
        1. Add new specialty
        2. Remove specialty
        
        Enter number of menu item: 
        """))
        return specialty_menu

    @staticmethod
    def choose_group_menu():
        group_menu = int(input("""
        1. Add new group
        2. Remove group
        
        Enter number of menu item: 
        """))
        return group_menu

    @staticmethod
    def choose_student_menu():
        student_menu = int(input(""""
        1. Add new student
        2. Remove student
        
        Enter number of menu item: 
        """))
        return student_menu

    @staticmethod
    def choose_report_menu():
        report_menu = int(input("""
        1. Brief information about the university
        2. Complete information about the university
        3. All specialties of a particular faculty
        4. All groups of a particular faculty
        5. All students of a particular group
        
        Enter number of menu item: 
        """))
        return report_menu






