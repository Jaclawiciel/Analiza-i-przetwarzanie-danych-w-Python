months_1_3 = {'Styczen', 'Luty', 'Marzec'}
months_4_6 = {'Marzec', 'Kwiecein', 'Maj'}


def sum_of_sets(set1, set2):
    return set1.union(set2)


def intersection_of_sets(set1, set2):
    return set1.intersection(set2)


def difference_of_sets(set1, set2):
    return set1.difference(set2)

print("Suma zbiorow: {}".format(sum_of_sets(months_1_3, months_4_6)))
print("Czesc wspolna zbiorow: {}".format(intersection_of_sets(months_1_3, months_4_6)))
print("Roznica zbiorow: {}".format(difference_of_sets(months_1_3, months_4_6)))
