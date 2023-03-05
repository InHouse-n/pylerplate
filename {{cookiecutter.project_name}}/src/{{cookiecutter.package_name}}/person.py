class Person:
    """This is an example class, you can delete this"""

    def __init__(self, name: str, age: int, eye_color: str):
        self.name = name
        self.age = age
        self.eye_color = eye_color

    def change_name(self, name: str):
        self.name = name

    def birthday(self):
        self.age += 1

    def present_yourself(self):
        print(
            f"Hey! my name is {self.name} and I'm {self.age} years old."
            f"I have {self.eye_color} eyes"
        )
