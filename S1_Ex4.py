number_of_inputs = int(input())
accepted_person = {'gender':"",'name':"", 'pl':""}
list_of_persons = []
def get_input(num):
    for i in range(num):
        person = str(input())
        list_of_persons.append({'gender': person.split('.')[0], 'name': person.split('.')[1], 'pl': person.split('.')[2]})
    return list_of_persons

get_input(number_of_inputs)

for i in range(len(list_of_persons)):
    list_of_persons[i]["name"] = list_of_persons[i]["name"].lower().capitalize()

list_of_persons.sort(key=lambda e:(e['gender'],e['name']), reverse=False)

def get_results(persons):
    for i in range(len(persons)):
        print( f'{persons[i]["gender"]} {persons[i]["name"]} {persons[i]["pl"]}')


get_results(list_of_persons)
