from classes import Human

manish = Human(
    name="Manish",
    date_of_birth = "07-01-1999",
    place= "Pune",
    gender= "Male",
    alive = True,
    profession = "IT",
    height = 153,
    weight = 62
)

print(manish)
print(manish.weight)
print(manish.eat("protein"))
print(manish.weight)

print(manish.eat("chicken"))

print(manish.vomit())
