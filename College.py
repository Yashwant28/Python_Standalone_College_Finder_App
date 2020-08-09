class College:
    college_id: int
    college_name: str
    course_type: str
    city: str
    fees: float
    pin_code: int

    def __init__(self, college_id, college_name, course_type, city, fees, pin_code):
        self.college_id = college_id
        self.college_name = college_name
        self.course_type = course_type
        self.city = city
        self.fees = fees
        self.pin_code = pin_code


def populate_college_object(college_id, college_name, course_type, city, fees, pin_code):
    college_obj = College(college_id, college_name, course_type, city, fees, pin_code)
    print(college_obj)
    return college_obj
