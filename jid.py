
users = [
    {
        'id': 1,
        "name": "Ismoil",
        "lastname": "Murodov",
        "interests": ['football', 'playing', 'coding'],
        ('address', 'bank'): {
            'address': "Tashkent",
            'bank': "SQB"
        }
    },
    {
        'id': 2,
        "name": "Shoilhom",
        "lastname": "Abdullayev",
        "interests": ['tennis', 'playing', 'coding'],
        ('address', 'bank'): {
            'address': "Tashkent",
            'bank': "SQB"
        }
    }
]
marks = {
    1: {
        'python': 3,
        "js": 4
    },
    2: {
        'python': 5,
        "js": 3
    }
}

for user in users:
    for key, value in user.items():
        if type(value) is list:
            print(f"---{key}")
            for item in value:
                print(f"--- {item}")
        elif type(value) is dict:
            print(f"-{key}")
            for k, v in value.items():
                print(f"-----{k} {v}")
        elif type(value) is int:
            print(key, value)
            for course, mark in marks[value].items():
                print(f"---{course}: {mark}")
        else:
            print(key, value)
    print('--------------------------------------------')
