from Doctor import Doctor


class DoctorManager:

    def __init__(self):
        self.doctors = []
        self.read_doctors_file(self.doctors)

    @staticmethod
    def format_dr_info(doctor_object):
        return str(doctor_object)

    @staticmethod
    def enter_doctor_info():
        doctor_id = input("Enter the doctor id: ")
        name = input("Enter the doctor name: ")
        specialization = input("Enter the doctor's specialization: ")
        working_time = input("Enter the working time: ")
        qualification = input("Enter the doctor's qualification: ")
        room_number = input("Enter the doctor's room number: ")
        new_doctor = Doctor(doctor_id, name, specialization, working_time, qualification, room_number)
        return new_doctor

    @staticmethod
    def read_doctors_file(doctor_list):
        with open("data/doctors.txt", "r") as f:
            iter_f = iter(f)
            next(iter_f)
            for doctor_data in iter_f:
                new_doctor_object = Doctor()
                new_doctor_object.set_doctor_id(doctor_data.rstrip().split("_")[0])
                new_doctor_object.set_new_name(doctor_data.rstrip().split("_")[1])
                new_doctor_object.set_new_specialization(doctor_data.rstrip().split("_")[2])
                new_doctor_object.set_new_working_time(doctor_data.rstrip().split("_")[3])
                new_doctor_object.set_new_qualification(doctor_data.rstrip().split("_")[4])
                new_doctor_object.set_new_room_number(doctor_data.rstrip().split("_")[5])
                doctor_list.append(new_doctor_object)

    def search_doctor_by_id(self):
        doctor_obj = None
        flag = False
        id = input("Enter the doctor's ID: ")
        for doctor_object in self.doctors:
            if doctor_object.get_doctor_id() == id:
                flag = True
                doctor_obj = doctor_object
                break
        if flag:
            print(doctor_obj)
        else:
            print("Can’t find the doctor….")

    def search_doctor_by_name(self):
        doctor_obj = None
        flag = False
        name = input("Enter the doctor's name: ")
        for doctor_object in self.doctors:
            if (doctor_object.get_doctor_name()[3:].strip().casefold() == name.casefold()) or ("dr."+doctor_object.get_doctor_name()[3:].strip().casefold() == name.casefold()):
                flag = True
                doctor_obj = doctor_object
                break
        if flag:
            print(doctor_obj)
        else:
            print("Can’t find the doctor….")

    @staticmethod
    def display_doctor_info(doctor_object):
        print(doctor_object)
    
    def edit_doctor_info(self):
        flag = False
        doctor_id = input("Enter the doctor ID which you want to edit: ")
        for doctor_object in self.doctors:
            if doctor_object.get_doctor_id() == doctor_id:
                flag = True
                name = input("Enter the doctor's name: ")
                specialization = input("Enter the doctor's disease: ")
                working_time = input("Enter the doctor's gender: ")
                qualification = input("Enter the doctor's age: ")
                room_number = input("Enter the doctor's room number: ")
                doctor_object.set_new_name(name)
                doctor_object.set_new_specialization(specialization)
                doctor_object.set_new_working_time(working_time)
                doctor_object.set_new_qualification(qualification)
                doctor_object.set_new_room_number(room_number)
        if flag:
            with open("data/doctors.txt", "w") as f:
                f.writelines(map(lambda x: x.__str__(), self.doctors))
        else:
            print("Cannot find the doctor …..")

    def display_doctors_list(self):
        self.doctors.clear()
        self.read_doctors_file(self.doctors)
        for i in self.doctors:
            print(f"".join(map(lambda x: f"{x:20s}", str(i).split('_')))+"\n")

    def write_list_of_doctors_to_file(self, list_of_doctors):
        with open("data/doctors.txt", "a") as f:
            for _doctor in list_of_doctors:
                doctor_format = self.format_dr_info(_doctor)
                f.write(doctor_format)

    def add_dr_to_file(self):
        new_doctor = self.enter_doctor_info()
        self.write_list_of_doctors_to_file([f"\n{new_doctor}"])
        print("New doctor has been added")


