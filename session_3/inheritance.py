from classes import Human

# multi level inheritance
class Vegetarians(Human):

    def __init__(
        self,
        name: str,
        date_of_birth: str,
        place: str,
        gender: str,
        alive: bool,
        profession: str,
        height: int,
        weight: int,
        diet: str = "Vegetarian"
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
        self.diet = diet

    def eat(self, food: str):
        if food == "veg energy drink":
            self.height+=1
            return f"{self.name} has grown from {self.height-1} to {self.height} because of energy drink"
        elif food == "veg protein":
            self.weight+=1
            return f"{self.name} has grown from {self.weight-1} to {self.weight} because of protein"
        else:
            # TODO 2: Fix this
            self.vomit()

    def __repr__(self):
        return f"This object is of a human named {self.name} from {self.place} is of {self.diet} diet"




class Brahmin(Vegetarians):
    def __init__(
        self,
        name: str,
        date_of_birth: str,
        place: str,
        gender: str,
        alive: bool,
        profession: str,
        height: int,
        weight: int,
        diet: str = "Vegetarian"
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
        self.diet = diet

    def do_pooja(self):
        return "Doing pooja"


veg_manish = Brahmin(
    name="Manish",
    date_of_birth = "07-01-1999",
    place= "Pune",
    gender= "Male",
    alive = True,
    profession = "IT",
    height = 153,
    weight = 62
)

print(veg_manish)

print(veg_manish.eat("veg protein"))

print(veg_manish.do_pooja())
