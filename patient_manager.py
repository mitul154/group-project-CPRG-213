import patient


class PatientManager:  # This class is used to manage the patients
    def __init__(self):  # Creates the constructor for the PatientManager class
        self.patient_list = []
        self.read_patients_file(self.patient_list)

    @staticmethod
    def format_patient_info_for_file(
            patient_object):  # This method is used to format the patient information for the file
        split = str(patient_object).split("_")
        return f"{split[0]:5s}{split[1]:20s}{split[2]:20s}{split[3]:20s}{split[4]}"

    @staticmethod
    def enter_patient_info():  # This method is used to ask the user to enter the patient's information
        pid = input("Enter the patient id: ")
        name = input("Enter the patient name: ")
        disease = input("Enter the patient's disease: ")
        gender = input("Enter the patient's gender: ")
        age = input("Enter the patient's age: ")
        new_patient = patient.Patient()
        new_patient.set_pid(pid)
        new_patient.set_name(name)
        new_patient.set_disease(disease)
        new_patient.set_gender(gender)
        new_patient.set_age(age)
        print(f"\nPatient whose ID is {pid} has been added.")  # Prints a confirmation that the patient was added
        return new_patient

    def read_patients_file(self, patient_list):  # This method is used to read the patients file
        self.patient_list.clear()  # Clears the patient list
        with open("data/patients.txt", "r") as f:  # Opens the patients file
            for patient_data in f:  # Loops through the patients file
                new_patient_object = patient.Patient()
                new_patient_object.set_pid(patient_data.rstrip().split("_")[0])
                new_patient_object.set_name(patient_data.rstrip().split("_")[1])
                new_patient_object.set_disease(patient_data.rstrip().split("_")[2])
                new_patient_object.set_gender(patient_data.rstrip().split("_")[3])
                new_patient_object.set_age(patient_data.rstrip().split("_")[4])
                patient_list.append(new_patient_object)

    def search_patient_by_id(self):  # This method is used to search for a patient by their ID
        patient_obj = None  # Sets the patient object to None
        flag = False  # Sets the flag to False
        id = input("Enter the patient ID: ")  # Asks the user to enter the patient's ID
        for patient_object in self.patient_list:  # Loops through the patient list
            if patient_object.get_pid() == id:
                flag = True
                patient_obj = patient_object
                break
        if flag:  # If the flag is True, then the patient's information is displayed
            print(f"ID{'':3s}Name{'':16s}Disease{'':13s}Gender{'':14s}Age\n")  # Prints the header for the patient
            # information
            print(self.format_patient_info_for_file(patient_obj))  # Prints the patient information
        elif id == "id":
            print("Can’t find the patient….")  # If the flag is false but the patient ID is "id", then it prints that
            # the patient cannot be found
        else:
            print("Can’t find the patient….")

    @staticmethod
    def display_patient_info(patient_object):  # This method is used to display the patient's information
        print(patient_object)  # Prints the patient's information

    def edit_patient_info_by_id(self):  # This method is used to edit the patient's information by their ID
        flag = False  # Sets the flag to False
        pid = input("Enter the patient ID which you want to edit: ")  # Asks the user to enter the patient's ID
        for patient_object in self.patient_list:  # Loops through the patient list
            if patient_object.get_pid() == pid:  # If the patient's ID is found, then the patient's information is
                # edited
                flag = True  # Sets the flag to True
                name = input("Enter the patient name: ")
                disease = input("Enter the patient's disease: ")
                gender = input("Enter the patient's gender: ")
                age = input("Enter the patient's age: ")
                patient_object.set_name(name)
                patient_object.set_disease(disease)
                patient_object.set_gender(gender)
                patient_object.set_age(age)
        if flag:  # If the flag is True, then the patient's information is edited
            with open("data/patients.txt", "w") as f:  # Opens the patients file
                f.writelines(
                    map(lambda x: x.__str__() + "\n", self.patient_list))  # Writes the patient's information to
                # the patients file
                print(f"\nPatient whose ID is {pid} has been edited.")
        else:
            print("Cannot find the patient …..")

    def display_patients_list(self):  # This method is used to display the list of patients
        self.read_patients_file(self.patient_list)  # Calls the read_patients_file method
        for i in self.patient_list:  # Loops through the patient list
            print(self.format_patient_info_for_file(str(i)) + "\n")

    @staticmethod
    def write_list_of_patients_to_file(list_of_patients):  # This method is used to write the list of patients to the
        # patients file
        with open("data/patients.txt", "a") as f:  # Opens the patients file
            for _patient in list_of_patients:  # Loops through the list of patients
                patient_format = str(_patient)
                f.write(patient_format)

    def add_patient_to_file(self):  # This method is used to add a patient to the patients file
        new_patient = self.enter_patient_info()  # Calls the enter_patient_info method
        self.write_list_of_patients_to_file([f"\n{new_patient}"])  # Writes the patient's information to the patients
        # file
