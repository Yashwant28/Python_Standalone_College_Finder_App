import College
from CollegeResource import register_college
from CollegeResource import search_college


def main_menu():
    print("Press 1 to Main menu")
    print("Press 0 to Exit ")
    user_choice: int = int(input("Enter your choice : "))
    if user_choice == 1:
        print("------------------------------------------------------------------")
        print("\n**** Main menu *****")
        sub_menu()
    elif user_choice == 0:
        print("------------------------------------------------------------------")
        print("\n***** Bye *****")
        exit(0)
    else:
        print("------------------------------------------------------------------")
        print("\ninvalid Input Given Try Again")
        main_menu()


def sub_menu():
    print("Press 1 to Register New College")
    print("Press 2 to Search College")
    print("Press 3 to Delete a College")
    print("Press 0 to Exit ")
    user_choice: int = int(input("Enter your choice : "))
    if user_choice == 1:
        print("------------------------------------------------------------------")
        college_registration()
    elif user_choice == 2:
        print("------------------------------------------------------------------")
        city: int = str(input("Enter City : "))
        course_type: int = str(input("Enter Course Type : "))
        college_search(city, course_type)
    elif user_choice == 3:
        print("------------------------------------------------------------------")
    elif user_choice == 0:
        print("------------------------------------------------------------------")
        print("\n***** Bye *****")
        exit(0)
    else:
        print("------------------------------------------------------------------")
        print("\ninvalid Input Given Try Again")
        sub_menu()


def college_search(city: str, course_type: str):
    college: College = search_college(city, course_type)


def college_registration():
    if register_college():
        print("*********************** save operation successful ***********************")
    else:
        print("*********************** save operation failed ***********************")


if __name__ == '__main__':
    print("******************* WELCOME TO THE COLLEGE APP *******************")
    print("-")
    print("-")
    print("------------------------------------------------------------------")
    while True:
        main_menu()
