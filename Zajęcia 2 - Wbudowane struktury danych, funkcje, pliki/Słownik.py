month_numbers_and_names = {
    1: 'Styczen',
    2: 'Luty',
    3: 'Marzec',
    4: 'Kwiecien',
    5: 'Maj',
    6: 'Czerwiec',
    7: 'Lipiec',
    8: 'Sierpien',
    9: 'Wrzesien',
    10: 'Pazdziernik',
    11: 'Listopad',
    12: 'Grudzien'
}


def get_month_name_From_Numbers(month_number):
    try:
        month_number = int(month_number)
    except ValueError as err:
        print("ERROR! Given value is not a number. Please, try again...")
        print("{}".format(err))

    if month_number < 1 or month_number > 12:
        raise ValueError("ERROR! Given value is not a proper month number. Please, try again...")

    return month_numbers_and_names[month_number]

print(get_month_name_From_Numbers("6"))
