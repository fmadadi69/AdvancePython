genres = {'Horror': 0, 'Romance': 0, 'Comedy': 0, 'History': 0, 'Adventure': 0, 'Action': 0}

input_numbers = int(input())


def get_input(num):
    input_list = []
    for i in range(num):
        input_list.append(str(input()))
    return input_list


def analyze_input(input_list):
    for item in input_list:
        fav_genres = item.split()
        for g in fav_genres[1:]:
            genres[g] += 1
    return genres


analyze_input(get_input(input_numbers))

sorted_genres_alphabetic ={ i: genres[i] for i in  sorted(genres)}
sorted_genres_values = sorted(sorted_genres_alphabetic.items(),key=lambda x: x[1], reverse=True)

# print(sorted_genres_values)

def get_results(sorted_genres):
    for item in sorted_genres:
        print(f'{item[0]} : {item[1]}')

get_results(sorted_genres_values)
