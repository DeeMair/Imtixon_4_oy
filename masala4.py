""""""
"""4.Masala"""
class Hayvon:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Yirtqich(Hayvon):
    def __init__(self, name, age):
        super().__init__(name, age)

    def ov_qilish(self):
        return f"{self.name} ov qilmoqda"

class Uy_hayvoni(Hayvon):
    def __init__(self, name, age):
        super().__init__(name, age)

    def oynash(self):
        return f"{self.name} o'ynayapti"

sher = Yirtqich("Sher", 13)
print(sher.ov_qilish())

mushuk = Uy_hayvoni("Mishiq", 5)
print(mushuk.oynash())
