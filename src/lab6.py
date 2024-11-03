class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password

    def set_pass(self,new_pass):
        self.__password = new_pass

    def check_pass(self, password):
        return self.__password == password
    
user = UserAccount("user", "use", "password")
user.set_pass("new_password")
print(user.check_pass("wrong_password"))
print(user.check_pass("new_password")) 


class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        return f"manufacturer: {self.make}, model: {self.model}"


class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, fuel type: {self.fuel_type}"
    

car = Car("Tesla", "Model X", "Electricity")
print(car.get_info())