import random
students = ["William", "Asher", "John", "Alex", "Allan", 
            "Shouwang", "Samantha", "Iwona", "Matias", "Christopher"]

def randomRoom(list):
    room_1 = []
    room_2 = []
    room_3 = []
    room_4 = []
    room_5 = []
    counter = len(list)
    while counter > 0:
        while len(room_1) < 2 and counter > 0:
            x = random.choice(list)
            room_1.append(x)
            counter-=1
            list.remove(x)
        while len(room_2) < 2 and counter > 0:
            x = random.choice(list)
            room_2.append(x)
            counter-=1
            list.remove(x)
        while len(room_3) < 2 and counter > 0:
            x = random.choice(list)
            room_3.append(x)
            counter-=1
            list.remove(x)
        while len(room_4) < 2 and counter > 0:
            x = random.choice(list)
            room_4.append(x)
            counter-=1
            list.remove(x)
        while len(room_5) < 2 and counter > 0:
            x = random.choice(list)
            room_5.append(x)
            counter-=1
            list.remove(x)
    print(room_1)
    print(room_2)
    print(room_3)
    print(room_4)
    print(room_5)

randomRoom(students)


