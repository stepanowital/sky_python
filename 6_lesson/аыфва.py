fish = [

    {"specie": "Белуга", "water": "fresh"},
    {"specie": "Карась", "water": "fresh"},
    {"specie": "Красноперка", "water": "fresh"},

    {"specie": "Морской окунь", "water": "sea"},
    {"specie": "Тунец", "water": "sea"},
    {"specie": "Скумбрия", "water": "sea"},

]


def get_fish(fish_name):
    for item in range(len(fish)):
        for key, value in fish[item].items():
            if fish_name == value:
                return fish[item][key], fish[item]['water']


fish_name = input()
fish, water = get_fish(fish_name)
print(fish, water)
