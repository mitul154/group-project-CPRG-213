from Doctor import Doctor, Doctor1


class DoctorManager:

    def __init__(self):
        self.doctors = []


    def format_dr_info(self, doctor_object):
        return f"{doctor_object.get_doctor_id()}_{doctor_object.get_doctor_name()}_{doctor_object.get_specialization()}_{doctor_object.get_working_time()}_{doctor_object.get_qualification()}_{doctor_object.get_room_number()}"
    
    
    def enter_doctor_info(self):
         new_doctor_object = Doctor()
         new_doctor_object.set()

    


DM1 = DoctorManager()
print(DM1.format_dr_info(Doctor1))
