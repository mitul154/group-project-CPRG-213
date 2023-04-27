from Doctor import Doctor  # imports the Doctor class from Doctor.py


class DoctorManager:  # Creates the DoctorManager class

    def __init__(self):  # Creates the constructor for the DoctorManager class
        self.doctors = []
        self.read_doctors_file(self.doctors)

    @staticmethod
    def format_dr_info(doctor_object):  # Creates a static method to format the doctor's information
        split = str(doctor_object).split("_")
        return f"{split[0]:5s}{split[1]:20s}{split[2]:20s}{split[3]:20s}{split[4]:20s}{split[5]}"

    @staticmethod
    def enter_doctor_info():  # Creates a static method to ask the user to enter the doctor's information
        doctor_id = input("Enter the doctor id: ")
        name = input("Enter the doctor name: ")
        specialization = input("Enter the doctor's specialization: ")
        working_time = input("Enter the working time: ")
        qualification = input("Enter the doctor's qualification: ")
        room_number = input("Enter the doctor's room number: ")
        new_doctor = Doctor()
        new_doctor.set_doctor_id(doctor_id)
        new_doctor.set_new_name(name)
        new_doctor.set_new_specialization(specialization)
        new_doctor.set_new_working_time(working_time)
        new_doctor.set_new_qualification(qualification)
        new_doctor.set_new_room_number(room_number)
        print(f"\nDoctor whose ID is {doctor_id} has been added")
        return new_doctor

    @staticmethod
    def read_doctors_file(doctor_list):  # Creates a static method to read the doctors.txt file
        with open("data/doctors.txt", "r") as f:  # Opens the doctors.txt file in read mode
            for doctor_data in f:  # Loops through each line in the doctors.txt file
                new_doctor_object = Doctor()
                new_doctor_object.set_doctor_id(doctor_data.rstrip().split("_")[0])
                new_doctor_object.set_new_name(doctor_data.rstrip().split("_")[1])
                new_doctor_object.set_new_specialization(doctor_data.rstrip().split("_")[2])
                new_doctor_object.set_new_working_time(doctor_data.rstrip().split("_")[3])
                new_doctor_object.set_new_qualification(doctor_data.rstrip().split("_")[4])
                new_doctor_object.set_new_room_number(doctor_data.rstrip().split("_")[5])
                doctor_list.append(new_doctor_object)

    def search_doctor_by_id(self):  # Creates a method to search the doctor by ID
        doctor_obj = None  # Creates a variable to store the doctor object
        flag = False  # Creates a flag variable to check if the doctor is found
        id = input("Enter the doctor's ID: ")  # Asks the user to enter the doctor's ID
        for doctor_object in self.doctors:  # Loops through each doctor object in the doctors list
            if doctor_object.get_doctor_id() == id:
                flag = True
                doctor_obj = self.format_dr_info(doctor_object)
                break

        if flag:  # If the doctor is found, the doctor's information will be displayed
            print(f"ID{'':3s}Name{'':16s}Speciality{'':10s}Timing{'':14s}Qualification{'':7s}Room Number\n")
            print(doctor_obj)
        else:
            print("Can't find the doctor….")

    def search_doctor_by_name(self):  # Creates a method to search the doctor by name
        doctor_obj = None  # Creates a variable to store the doctor object
        flag = False  # Creates a flag variable to check if the doctor is found
        name = input("Enter the doctor's name: ")  # Asks the user to enter the doctor's name
        for doctor_object in self.doctors:  # Loops through each doctor object in the doctors list
            if (doctor_object.get_doctor_name()[3:].strip().casefold() == name.casefold()) or (
                    "dr." + doctor_object.get_doctor_name()[3:].strip().casefold() == name.casefold()):
                flag = True
                doctor_obj = self.format_dr_info(doctor_object)
                break
        if flag:  # If the doctor is found, the doctor's information will be displayed
            print(f"ID{'':3s}Name{'':16s}Speciality{'':10s}Timing{'':14s}Qualification{'':7s}Room Number\n")
            print(doctor_obj)
        else:
            print("Can’t find the doctor….")

    @staticmethod
    def display_doctor_info(doctor_object):  # Creates a static method to display the doctor's information
        print(doctor_object)

    def edit_doctor_info(self):  # Creates a method to edit the doctor's information
        flag = False  # Creates a flag variable to check if the doctor is found
        doctor_id = input("Enter the doctor ID which you want to edit: ")  # Asks the user to enter the doctor's ID
        for doctor_object in self.doctors:  # Loops through each doctor object in the doctors list
            if doctor_object.get_doctor_id() == doctor_id:  # If the doctor is found, the doctor's information will
                # be able to be edited
                flag = True  # Flag is set to True
                name = input("Enter the doctor's name: ")
                specialization = input("Enter the doctor's specialization: ")
                working_time = input("Enter the doctor's working time: ")
                qualification = input("Enter the doctor's qualification: ")
                room_number = input("Enter the doctor's room number: ")
                doctor_object.set_new_name(name)
                doctor_object.set_new_specialization(specialization)
                doctor_object.set_new_working_time(working_time)
                doctor_object.set_new_qualification(qualification)
                doctor_object.set_new_room_number(room_number)
        if flag:  # If the doctor ID is found, the information will be written in the doctors.txt file
            with open("data/doctors.txt", "w") as f:
                f.writelines(map(lambda x: x.__str__() + "\n", self.doctors))
                print(f"Doctor whose ID is {doctor_id} has been edited")
        else:
            print("Cannot find the doctor …..")

    def display_doctors_list(self):  # Creates a method to display the doctors list
        self.doctors.clear()
        self.read_doctors_file(self.doctors)
        for i in self.doctors:  # Loops through each doctor object in the doctors list
            print(self.format_dr_info(str(i)) + "\n")
            # print(f"".join(map(lambda x: f"{x:20s}", str(i).split('_')))+"\n")

    @staticmethod
    def write_list_of_doctors_to_file(
            list_of_doctors):  # Creates a method to write the list of doctors to the doctors.txt file
        with open("data/doctors.txt", "a") as f:  # Opens the doctors.txt file in append mode
            for _doctor in list_of_doctors:  # Loops through each doctor object in the list of doctors
                doctor_format = str(_doctor)  # Formats the doctor's information
                f.write(doctor_format)  # Writes the doctor's information to the doctors.txt file

    def add_dr_to_file(self):  # Creates a method to add a doctor to the doctors.txt file
        new_doctor = self.enter_doctor_info()  # Calls the enter_doctor_info() method to enter the doctor's information
        self.write_list_of_doctors_to_file(
            [f"\n{new_doctor}"])  # Writes the doctor's information to the doctors.txt file
