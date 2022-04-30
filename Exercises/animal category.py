animal = input()

animal_info = {
    "dog": "mammal",
    "crocodile": "reptile",
    "tortoise": "reptile",
    "snake": "reptile",
    "others": "unknown"
}

if animal in animal_info:
    print(animal_info.get(animal))
else:
    print(animal_info["others"])