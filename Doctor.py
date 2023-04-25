class Doctor:  #Creates the Doctor class with the attributes of doctor_id, doctor_name, specialization, working_time, qualification, room_number
    def __init__(self, doctor_id = "", doctor_name = "", specialization = "", working_time = "", qualification = "", room_number = 0): #Creates the constructor for the Doctor class
        self.doctor_id = doctor_id
        self.doctor_name = doctor_name
        self.specialization = specialization
        self.working_time = working_time
        self.qualification = qualification
        self.room_number = room_number

    def get_doctor_id(self):
        return self.doctor_id

    def get_doctor_name(self):
        return self.doctor_name

    def get_specialization(self):
        return self.specialization

    def get_working_time(self):
        return self.working_time

    def get_qualification(self):
        return self.qualification

    def get_room_number(self):
        return self.room_number

    def set_doctor_id(self, new_id):
        self.doctor_id = new_id

    def set_new_name(self, new_doctor_name):
        self.doctor_name = new_doctor_name

    def set_new_specialization(self, new_specialization):
        self.specialization = new_specialization

    def set_new_working_time(self, new_working_time):
        self.working_time = new_working_time

    def set_new_qualification(self, new_qualification):
        self.qualification = new_qualification

    def set_new_room_number(self, new_room_number):
        self.room_number = new_room_number

    def __str__(self):
        return f"{self.doctor_id}_{self.doctor_name}_{self.specialization}_{self.working_time}_{self.qualification}_{self.room_number}"

