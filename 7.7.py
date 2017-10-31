
title = str(input('Enter a title for the data:\n'))
print('You entered:', title)
print()

column1 = str(input('Enter column 1 heading:\n'))
print('You entered:', column1)
print()

column2 = str(input('Enter column 2 heading:\n'))
print('You entered:', column2)
print()

data_points_strings = []
data_points_ints = []


def get_data_points():
    data = input('Enter a data point (-1 to stop input):')
    while input != '':
        if data == '-1':
            display_table()
            display_bar()
            break
        elif ',' not in data:
            print('Error. No comma in string')
            get_data_points()
        elif data.count(',') >= 2:
            print('Error. Too many commas in input.')
            get_data_points()
            #FIXME: 'Comma not followed by integer' condition
        else:
            #renamed your data_points array to single_data_points
            single_data_points = data.split(',')
            i = 0
            while i < len(single_data_points):
                single_data_points[i] = single_data_points[i].strip()
                i += 1
            if not single_data_points[1].isnumeric():
                print('Error: Comma not followed by an integer.')
                get_data_points()
            print('Data string:', single_data_points[0])
            print('Data integer:', single_data_points[1])
            data_points_strings.append(single_data_points[0])
            data_points_ints.append(single_data_points[1])
            get_data_points()
        return


def display_table():
    print(f'{title:>33}')
    print(f'{column1:20}|{column2:>23}')
    print('--------------------------------------------')
    i = 0
    while i < len(data_points_ints):
        print(f'{data_points_strings[i]:20}|{data_points_ints[i]:>23}')
        i +=1


def display_bar():
    i = 0
    while i < len(data_points_ints):
        stars = str('*' * int(data_points_ints[i]))
        print(f'{data_points_strings[i]:>20} {stars}')
        i += 1

get_data_points()
