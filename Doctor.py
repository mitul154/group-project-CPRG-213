class Doctor:
    def __init__(self, doctor_id, name, specialization, working_time, qualification, room_number): 
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization    
        self.working_time = working_time
        self.qualification = qualification
        self.room_number = room_number
        
        
    def get_doctor_id(self):
        return self.doctor_id
    
    
    def get_name(self):
        return self.name
    
    
    def get_specialization(self):
        return self.specialization
    
    
    def get_working_time(self):
        return self.working_time
    
    
    def get_qualification(self ):
        return self.qualification
    
    
    def get_room_number(self):
        return self.room_number
    
    
    
