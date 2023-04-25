class Patient: # This class is used to create a patient object
    def __init__(self): # Creates the constructor for the Patient class
        self.pid = None
        self.name = None
        self.disease = None
        self.gender = None
        self.age = 0

    def get_pid(self):
        return self.pid

    def get_name(self):
        return self.name

    def get_disease(self):
        return self.disease

    def get_gender(self):
        return self.gender

    def get_age(self):
        return self.age

    def set_pid(self, pid):
        self.pid = pid

    def set_name(self, name):
        self.name = name

    def set_disease(self, disease):
        self.disease = disease

    def set_gender(self, gender):
        self.gender = gender

    def set_age(self, age):
        self.age = age

    def __str__(self):
        return f"{self.pid}_{self.name}_{self.disease}_{self.gender}_{self.age}"


