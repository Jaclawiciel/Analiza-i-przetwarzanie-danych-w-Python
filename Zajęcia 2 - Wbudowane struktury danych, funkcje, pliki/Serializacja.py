import json

class Person:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_person_as_dict(self):
        person_dict = {
            "first_name": first_name,
            "last_name": last_name,
            "age": age
        }
        return person_dict

    def get_person_as_string(self):
        return "Imie: {}, Nazwisko: {}, Wiek: {}".format(first_name, last_name, age)



def get_first_name():
    try:
        text_input = input("Podaj imie: > ")
        while(text_input == "" or not text_input.isalpha()):
            text_input = input("Bledna wartosc! \nPodaj imie: > ")

    except AttributeError as err:
        print("Bledna wartosc! Imie zawiera bledne znaki...")
        print("{}".format(err))

    return text_input


def get_last_name():
    try:
        text_input = input("Podaj nazwisko: > ")
        while text_input == "" or not text_input.isalpha():
            text_input = input("Bledna wartosc! \nPodaj nazwisko: > ")

    except AttributeError as err:
        print("Bledna wartosc! Nazwisko zawiera bledne znaki...")
        print("{}".format(err))

    return text_input


def get_age():
    try:
        text_input = int(input("Podaj wiek: > "))
        while text_input == "":
            text_input = input("Bledna wartosc! \nPodaj wiek: > ")

    except ValueError as err:
        print("Bledna wartosc! Wiek zawiera bledne znaki...")
        print("{}".format(err))

    return text_input


people_json = []
people_text = ""

file_json = open("people_json.txt", "wt")
file_txt = open("people.txt", "wt")

print("Wprowadz kolejno dane osob, ktore chcesz zapisac do pliku\nWprowadz pusta wartosc, aby zakonczyc\n")

should_continue = input("Kontynuowac? (T/N) > ")

counter = 1
while should_continue.lower() == "t":
    first_name = get_first_name()
    last_name = get_last_name()
    age = get_age()
    person = Person(first_name, last_name, age)
    people_json.append(person.get_person_as_dict())
    people_text += "{}. {} \n".format(counter, person.get_person_as_string())
    counter += 1
    should_continue = input("Kontynuowac? (T/N) > ")

people_JSON = json.dumps(people_json)

file_json.write(people_JSON)
file_txt.write(people_text)

print("People as JSON: {}".format(people_JSON))
print("People as STRING: {}".format(people_text))
