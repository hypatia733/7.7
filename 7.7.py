
title = str(input('Enter a title for the data:\n'))
print('You entered:', title)
print()

column1 = str(input('Enter column 1 heading:\n'))
print('You entered:', column1)
print()

column2 = str(input('Enter column 2 heading:\n'))
print('You entered:', column2)
print()

def get_data_points():   #output data points
    data = input('Enter data points:')
    while input != '':
        if data == '-1':
            print('Exiting')
            break
        elif ',' not in data:
            print('Error. No comma in string')
            get_data_points()
        elif data.count(',') >= 2:
            print('Error. Too many commas in input.')
            get_data_points()
            #FIXME: 'Comma not followed by integer' condition
        else:
            data_points = data.split(',')
            i = 0
            while i < len(data_points):
                data_points[i] = data_points[i].strip()
                i += 1
            if not data_points[1].isnumeric():
                print('Error: Comma not followed by an integer.')
                get_data_points()
            print('Data string:', data_points[0])
            print('Data integer:', data_points[1])
            get_data_points()
        return

get_data_points()
