class Patient:
    def __init__(self):
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

    def set_pid(self, new_id):
        self.pid = new_id
        return self.pid

    def set_name(self, new_name):
        self.name = new_name
        return self.name

    def set_disease(self, new_disease):
        self.disease = new_disease
        return self.disease

    def set_gender(self, new_gender):
        self.gender = new_gender
        return self.gender

    def set_id(self, new_age):
        self.age = new_age
        return self.age
class Patient:
    def __init__(self):
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




    def __str__(self):
        return f"{self.pid}_{self.name}_{self.disease}_{self.gender}_{self.age}"