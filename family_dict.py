my_family = {
    "sister": {
        "name": "Krista",
        "age": 42
    },
    "mother": {
        "name": "Cathie",
        "age": 70
    }
}



for (member, info) in my_family.items():
    sentence = info['name'] + ' is my ' + member + ' and is ' + str(info['age']) + ' years old.'
    print(sentence)