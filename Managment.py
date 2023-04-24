# Importing the classes from different files
# os is used to terminate the program later
import DoctorManager
import patient_manager
import os


class Display:
    # Initiates the Doctor manager class and patient manager class
    def __init__(self):
        self.patient = patient_manager.PatientManager()
        self.doctor = DoctorManager.DoctorManager()

    def display_menu(self):
        first_display_input = input("Welcome to Alberta Hospital (AH) Management system \n"
                                    "Select from the following options, or select 3 to stop: \n1 - 	Doctors\n"
                                    "2 - 	Patients\n3 -	Exit Program \n>>>")
        while first_display_input != 3:
            match first_display_input:
                case "1":
                    first_doctor_input = input("Doctors Menu:\n1 - Display Doctors list\n2 - Search for doctor by ID\n"
                                               "3 - Search for doctor by name\n4 - Add doctor\n5 - Edit doctor info\n"
                                               "6 - Back to the Main Menu\n>>>")
                    # calls the functions that user is trying to use
                    match first_doctor_input:
                        case "1":
                            self.doctor.display_doctors_list()
                        case "2":
                            self.doctor.search_doctor_by_id()
                        case "3":
                            self.doctor.search_doctor_by_name()
                        case "4":
                            self.doctor.add_dr_to_file()
                        case "5":
                            self.doctor.edit_doctor_info()
                        case "6":
                            # Calls the function again "acts as a back button"
                            initiator.display_menu()
                        case _:
                            print("You have entered a invalid response.\n")
                            initiator.display_menu()
                case "2":
                    patient_menu = input("Patients Menu:\n1 - Display patients list\n2 - Search for patient by ID"
                                         "\n3 - Add patient\n4 - Edit patient info\n5 - Back to the Main Menu\n>>>")
                    if patient_menu == "1":
                        print("ID\t\t\t\t\tName\t\t\t\tDisease\t\t\t\tGender\t\t\t\tAge\n")
                        self.patient.display_patients_list()
                        # for i in self.patient.patient_list:
                        #     print(f"".join(map(lambda x: f"{x:20s}", str(i).split('_'))))
                    elif patient_menu == "2":
                        self.patient.search_patient_by_id()
                    elif patient_menu == "3":
                        self.patient.add_patient_to_file()
                    elif patient_menu == "4":
                        self.patient.edit_patient_info_by_id()
                    elif patient_menu == "5":
                        initiator.display_menu()
                    else:
                        print("You have entered a invalid response.\n")
                        initiator.display_menu()
                case "3":
                    print("Thanks for using the program. Bye!")
                    # os.exit terminates the program when user is finished using it
                    os._exit(0)
                case _:
                    print("You have entered a invalid response.\n")
                    initiator.display_menu()


# Initiating objects to start the program
initiator = Display()
initiator.display_menu()

