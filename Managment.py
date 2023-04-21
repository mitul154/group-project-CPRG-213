# import DoctorManager
# import patient
import patient_manager
# import Doctor


class Display:
    # def new_doc_inputs(self):
    #     new_doctor_id = input("Enter the doctor Id: ")
    #     new_doctor_name = input("Enter the doctor name: ")
    #     new_doctor_specialty = input("Enter the doctor’s speciality: ")
    #     new_doctor_hours = input("Enter the doctor’s timing (e.g., 7am-10pm): ")
    #     new_doctor_qualifications = input("Enter the doctor’s qualification: ")
    #     new_doctor_room_number = input("Enter the doctor’s room number: ")
    #     new_doctor = Doctor(new_doctor_id, new_doctor_name, new_doctor_specialty, new_doctor_hours,
    #                         new_doctor_qualifications, new_doctor_room_number)
    #     return new_doctor

    @staticmethod
    def display_menu():
        first_display_input = input("Welcome to Alberta Hospital (AH) Managment system \n"
                                    "Select from the following options, or select 3 to stop: \n1 - 	Doctors\n"
                                    "2 - 	Patients\n3 -	Exit Program \n>>>")

        while first_display_input != 3:
            match first_display_input:
                case "1":
                    first_doctor_input = input("Doctors Menu:\n1 - Display Doctors list\n2 - Search for doctor by ID\n"
                                               "3 - Search for doctor by name\n4 - Add doctor\n5 - Edit doctor info\n"
                                               "6 - Back to the Main Menu\n>>>")
                    match first_doctor_input:
                        case "1":
                            display_doctors_list()

                        case "2":
                            id_input = input("Enter the doctor Id: ")
                            search_doctor_by_id(id_input)

                        case "3":
                            name_input = input("Enter the doctor name: ")
                            search_doctor_by_name(name_input)
                        case "4":
                            add_dr_to_file(self.new_doc_inputs())
                        case "5":
                            search_id = input("Please enter the id of the doctor that you want to edit their information: ")
                            if search_doctor_by_id(search_id) == "Can’t find the doctor.":
                                print("Doctor ID Doesn't exist")
                            else:
                                edit_doctor_info(self.new_doc_inputs())
                case "2":
                    patient_menu = input("Patients Menu:\n1 - Display patients list\n2 - Search for patient by ID"
                                         "\n3 - Add patient\n4 - Edit patient info\n5 - Back to the Main Menu\n>>>")
                    if patient_menu == "1":
                        c.display_patients_list()
                    elif patient_menu == "2":
                        c.search_patient_by_id()
                    elif patient_menu == "3":
                        c.add_patient_to_file()
                    elif patient_menu == "4":
                        c.edit_patient_info_by_id()
                    elif patient_menu == "5":
                        test.display_menu()
                    else:
                        print("You have entered a invalid response.\n")
                        test.display_menu()
                case "3":
                    print("Thanks for using the program. Bye!")
                    break
                case _:
                    print("You have entered a invalid response.\n")
                    test.display_menu()


c = patient_manager.PatientManager()


test = Display()
test.display_menu()

