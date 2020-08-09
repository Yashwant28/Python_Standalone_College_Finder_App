import csv
import College
from College import populate_college_object

class FileHandler:

    @classmethod
    def read_csv(self):
        college_list = []
        with open("colleges.csv")as csv_file:
            self.csv_data = csv.reader(csv_file, delimiter=',')
            print("read opration completed successfully")
            for row in self.csv_data:
                collegeId = row[0]
                print(collegeId)
                collegeName = row[1]
                print(collegeName)
                courseType = row[2]
                print(courseType)
                city = row[3]
                print(city)
                fees = row[4]
                print(fees)
                pincode = row[5]
                print(pincode)

                college = populate_college_object(row[0], row[1], row[2], row[3], row[4], row[5])
                college_list.append(college)
                print("inside For loop",college_list)

        print("outside Forloop",college_list)
        return college_list

    @classmethod
    def write_into_csv(self, college: College):
        csv.register_dialect('myDialect', delimiter=',')
        college_list = [college.college_id, college.college_name, college.course_type, college.city, college.fees,
                        college.pin_code]
        with open("colleges.csv", mode='a') as csv_file:
            self.csv_writer = csv.writer(csv_file, dialect='myDialect')
            self.csv_writer.writerow(college_list)
            print("write opration completed successfully")
        return True


write_into_csv = FileHandler.write_into_csv
read_csv= FileHandler.read_csv