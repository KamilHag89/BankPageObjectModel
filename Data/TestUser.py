class User:
    def __init__(self, name="Kamil", lastname="Kowalski", adress="Random", city="Warsaw", state="CBA", zipCode="03-190",
                 phoneNr="546123123", ssn="123", password="123456789"):
        self.name = name
        self.lastname = lastname
        self.adress = adress
        self.city = city
        self.state = state
        self.zipCode = zipCode
        self.phone = phoneNr
        self.ssn = ssn
        self.username = f"{self.name}.{self.lastname}"
        self.password = password
