def is_city_name_after_letter_in_alphabet(city_name, test_letter):
    if not test_letter.isalpha():
        raise ValueError("Podana wartosc nie jest litera! Sprobuj ponownie...")

    if len(test_letter) != 1:
        raise ValueError("Podana wartosc nie jest pojedyncza litera! Sprobuj ponownie...")

        city_name = city_name.lower()
        test_letter = test_letter.lower()
    return city_name > test_letter


def is_city_name_longer_than(city_name, test_length):
    return len(city_name) > test_length


cities = ['Amsterdam', 'Berlin', 'London', 'Paris', 'Warsaw']
test_letter = "K"
test_length = 6

print('Nazwy miast wystepujace w alfabecie po {}'.format(test_letter))
for city in cities:
    if is_city_name_after_letter_in_alphabet(city, 'K'):
        print(city)
print("-" * 10)
print("")

print("Nazwy miast dluzsze niz {}".format(test_length))
for city in cities:
    if is_city_name_longer_than(city, 6):
        print(city)

print("-" * 10)
print("")
