x = [[5, 2, 3], [10, 8, 9]]
students = [{'first_name': 'Michael', 'last_name': 'Jordan'},
            {'first_name': 'John', 'last_name': 'Rosales'}]
sports_directory = {'basketball': [
    'Kobe', 'Jordan', 'James', 'Curry'], 'soccer': ['Messi', 'Ronaldo', 'Rooney']}
z = [{'x': 10, 'y': 20}]

x[1][0] = 15

students[0]['last_name'] = 'Bryant'

sports_directory['soccer'][0] = 'Andres'

z[0]['y'] = 30


students = [{'first_name': 'Michael', 'last_name': 'Jordan'},
            {'first_name': 'John', 'last_name': 'Rosales'},
            {'first_name': 'Mark', 'last_name': 'Guillen'},
            {'first_name': 'KB', 'last_name': 'Tonel'}]


def iterateDictionary(some_list):
    for x in some_list:
        for key in x:
            print(key, " - ", x[key])


def iterateDictionary2(key_name, some_list):
    for x in some_list:
        print(x[key_name])


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(some_dict):
    for x in some_dict:
        print(len(some_dict[x]), x)
        for y in some_dict[x]:
            print(y)
