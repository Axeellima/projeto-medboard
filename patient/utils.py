import random, string


def generatePatientCode():
    letters = string.ascii_uppercase
    random_string = "".join(random.choice(letters) for i in range(4))

    random_number = random.random()
    round_number = round((random_number * 10000))

    patient_code = f"{random_string}{round_number}"
    return patient_code


def generatePatientPassword():
    random_number = random.random()
    password = round((random_number * 1000000))

    return password
