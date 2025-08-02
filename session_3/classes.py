# classes are blueprints
# ojects are building built on blueprints

class Human:
    # TODO 1: What is self keyword?
    def __init__(
        self,
        name: str,
        date_of_birth: str,
        place: str,
        gender: str,
        alive: bool,
        profession: str,
        height: int,
        weight: int
    ):
        # constructor
        self.name = name
        self.date_of_birth = date_of_birth
        self.place = place
        self.gender = gender
        self.alive = alive
        self.profession = profession
        self.height = height
        self.weight = weight

    def eat(self, food: str):
        if food == "energy drink":
            self.height+=1
            return f"{self.name} has grown from {self.height-1} to {self.height} because of energy drink"
        elif food == "protein":
            self.weight+=1
            return f"{self.name} has grown from {self.weight-1} to {self.weight} because of protein"
        else:
            # TODO 2: Fix this
            self.vomit()

    def vomit(self):
        return f"{self.name} is Vomiting"

    def __repr__(self):
        return f"This object is of a human named {self.name} from {self.place}"
