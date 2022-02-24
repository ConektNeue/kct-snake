def generate_canvas(coordinates_x, coordinates_y):
    last_coordinate_x = 0
    last_coordinate_y = 0

    less_number_y = 1
    less_number_x = 1

    first_iteration = True

    print('********************')
    for i in range(0, len(coordinates_x)):
        is_other_line = False
        if coordinates_y[i] == 1 and first_iteration:
            print('*', end='')
            first_iteration = False
        if i != 0:
            less_number_y = coordinates_y[i - 1]
            less_number_x = coordinates_x[i - 1] + 1
        nan = True
        if i > 0:
            if coordinates_x[i] == coordinates_x[i - 1] + 1 and coordinates_y[i] == coordinates_y[i - 1]:
                print('0', end='')
                nan = False
        if nan:
            if coordinates_y[i] != coordinates_y[i - 1] and i != 0:
                less_number_x = 1
                for j in range(0, 18 - coordinates_x[i - 1]):
                    print(' ', end='')
                print('*')
            for j in range(0, coordinates_y[i] - less_number_y):
                is_other_line = True
                print('*                  *')
            if is_other_line:
                print('*', end='')
            for j in range(0, coordinates_x[i] - less_number_x):
                print(' ', end='')
            print('0', end='')
        last_coordinate_x = coordinates_x[i]
        last_coordinate_y = coordinates_y[i]
    for i in range(0, 18 - last_coordinate_x):
        print(' ', end='')
    print('*')
    for i in range(0, 18 - last_coordinate_y):
        print('*                  *')
    print('********************')


generate_canvas([7, 9, 17], [1, 3, 18])
