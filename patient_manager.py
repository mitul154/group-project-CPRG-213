import patient


class PatientManager:
    def __init__(self):
        self.patient_list = []
        self.read_patients_file(self.patient_list)

    @staticmethod
    def format_patient_info_for_file(patient_object):
        return patient_object

    @staticmethod
    def enter_patient_info():
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
        return new_patient

    @staticmethod
    def read_patients_file(patient_list):
        with open("data/patients.txt", "r") as f:
            iter_f = iter(f)
            next(iter_f)
            for patient_data in iter_f:
                new_patient_object = patient.Patient()
                new_patient_object.set_pid(patient_data.rstrip().split("_")[0])
                new_patient_object.set_name(patient_data.rstrip().split("_")[1])
                new_patient_object.set_disease(patient_data.rstrip().split("_")[2])
                new_patient_object.set_gender(patient_data.rstrip().split("_")[3])
                new_patient_object.set_age(patient_data.rstrip().split("_")[4])
                patient_list.append(new_patient_object)

    def search_patient_by_id(self):
        patient_obj = None
        flag = False
        id = input("Enter the patient ID: ")
        for patient_object in self.patient_list:
            if patient_object.get_pid() == id:
                flag = True
                patient_obj = patient_object
                break
        if flag:
            print(patient_obj)
        else:
            print("Can’t find the patient….")

    @staticmethod
    def display_patient_info(patient_object):
        print(patient_object)

    def edit_patient_info_by_id(self):
        flag = False
        pid = input("Enter the patient ID which you want to edit: ")
        for patient_object in self.patient_list:
            if patient_object.get_pid() == pid:
                flag = True
                name = input("Enter the patient name: ")
                disease = input("Enter the patient's disease: ")
                gender = input("Enter the patient's gender: ")
                age = input("Enter the patient's age: ")
                patient_object.set_name(name)
                patient_object.set_disease(disease)
                patient_object.set_gender(gender)
                patient_object.set_age(age)
        if flag:
            with open("data/patients.txt", "w") as f:
                f.writelines(map(lambda x:x.__str__(), self.patient_list))
        else:
            print("Cannot find the patient …..")

    def display_patients_list(self):
        for _patient in self.patient_list:
            print(_patient)

    def write_list_of_patients_to_file(self, list_of_patients):
        with open("data/patients.txt", "a") as f:
            for _patient in list_of_patients:
                patient_format = self.format_patient_info_for_file(_patient)
                f.write(patient_format)

    def add_patient_to_file(self):
        pass




p1 = patient.Patient()
p1.set_name("djiowoaj")
a = PatientManager()
a.search_patient_by_id()
a.display_patient_info(p1)
# print(a.format_patient_info_for_file(p1))
