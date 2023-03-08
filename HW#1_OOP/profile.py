class Profile:
    def __init__(self, name, last_name,
                 phone_number, address, email,
                 birthday, age, sex):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex

    def info(self):
        return f"""
        Name: {self.name}
        Last name: {self.last_name}
        Phone number: {self.phone_number}
        Address: {self.address}
        Email: {self.email}
        Birthday: {self.birthday}
        Age: {self.age}
        Sex: {self.sex}
        """


class Profile_extended(Profile):
    def info(self):
        params = [self.name, self.last_name,
                  self.phone_number, self.address, self.email,
                  self.birthday, self.age, self.sex]
        return params


test = Profile_extended("Yaryna", "Ost", "0226457730", "Ternopil, Valova street", "test@gmail.com", "14/05/99", "23",
                        "female")
print(test.info())
