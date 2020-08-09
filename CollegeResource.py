import logging
from College import populate_college_object
import FileHandler


def register_college():
    logging.info("inside register_college function")
    print("Enter College Details")
    city, college_id, college_name, course_type, fees, pin_code = user_input()

    college = populate_college_object(college_id, college_name, course_type, city, fees, pin_code)
    result: bool = FileHandler.write_into_csv(college)
    if result:
        return True
    else:
        return False


def search_college(city: str, course_type: str):
    college_list = FileHandler.read_csv()
    print("inside College Resource", college_list)
    return college_list


def user_input():
    college_id = int(input("Enter College Id : "))
    college_name = str(input("Enter College Name : "))
    course_type = str(input("Enter Course Type : "))
    city = str(input("Enter City : "))
    fees = float(input("Enter Fees : "))
    pin_code = int(input("Enter Pin Code : "))
    return city, college_id, college_name, course_type, fees, pin_code
