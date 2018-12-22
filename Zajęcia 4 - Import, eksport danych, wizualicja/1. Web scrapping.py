import re
import pandas as pd

# zad1
print("===zad1===")
allowed_sites = pd.read_html("http://wolneodpracy.pl/")

results = {}
for subpage_index in allowed_sites[0]:
    site_url = allowed_sites[0][subpage_index]
    for subpage_url in site_url:
        matcher = re.search(r"(days|weekends)(.+).php", subpage_url)

        type = matcher.group(1)
        year = matcher.group(2)
        if type not in results:
            results[type] = {}
        results[type][year] = pd.read_html(subpage_url, header=0)[0]

print(results.keys())
print(results["days"].keys())
print(results["weekends"].keys())

# zad2
print("===zad2===")


# def append_default_set(dataFrame_object, header, element_to_add):
#     print("->" + element_to_add)
#     if header in dataFrame_object:
#         dataFrame_object[header].append(element_to_add)
#     else:
#         dataFrame_object[header] = element_to_add
#
#     return dataFrame_object


def append_default_set(dataFrame_object, elements):
    for element_name in elements:
        value = elements[element_name]
        for i in value:
            print(i)

    return dataFrame_object


free_days = pd.DataFrame()
long_weekends = pd.DataFrame()

new_map = {
    "Data": "Date",
    "Dzień": "Day",
    "Święta": "Name"
}

print(results["days"]["2018"].keys())

# for year in results["days"].keys():
#     print("Year: " + year)
#     fd = results["days"][year]
#     newRecordT = {"k1": [1,2], "k2": [1,2]}
#     # newRecord = {"k1": [1,2], "k2": [1,2]}
#     index += 1
#     # for key in fd.keys():
#     #     newRecord.append(key)
#     #     for y in fd[key]:
#     #         newRecord.append(y)
#     #     newRecord.append(year)
#     # print(newRecord)
#     free_days["Date"] = fd["Data"]
#     free_days["Day"] = fd["Dzień"]
#     free_days["Name"] = fd["Święta"]
#     free_days["Year"] = year
#

print(free_days )
