def open_file ():                        # For a filename open file for read, else output error message and first two lines of table.
    '''Input a filename and the function opens a file with that name. If wrong name inputed
       an error message is outputed with the two header lines of the table.'''
    try:
        filename = input("Input filename: ")
        a_file = open(filename, 'r')
        #print("OK")                            # Use as test output for filename input
        return a_file
    except FileNotFoundError:
        print('Cannot find file ' + filename)
        print('{:<32s} {:<32s} {:<6s}'.format('Indicator', 'Min', 'Max'))
        print('-' * 87)

def extract_info (filename):
    '''docstring'''
    indicator_list = []
    temp_states_list = []
    temp_heart_list = []
    temp_motor_vehicle_list = []
    temp_teen_birth_list = []
    temp_adult_smoking = []
    temp_adult_obesity = []
    line_str = 1

    for line_str in filename:
        field_list = line_str.strip().split(',')
        temp_states_list.append(field_list[0])
        states_list = [element for element in temp_states_list[1 : ]]
        temp_heart_list.append(field_list[1])
        heart_list = [float(element) for element in temp_heart_list[1 : ]]
        temp_motor_vehicle_list.append(field_list[5])
        motor_vehicle_list = [float(element) for element in temp_motor_vehicle_list[1 : ]]
        temp_teen_birth_list.append(field_list[7])
        teen_birth_list = [float(element) for element in temp_teen_birth_list[1 : ]]
        temp_adult_smoking.append(field_list[11])
        adult_smoking_list = [float(element[ : -1]) for element in temp_adult_smoking[1 : ]]
        temp_adult_obesity.append(field_list[13])
        adult_obesity_list = [float(element[ : -1]) for element in temp_adult_obesity[1 : ]]

    return states_list, heart_list, motor_vehicle_list, teen_birth_list, adult_smoking_list, adult_obesity_list

def find_max (indicator_list):
    '''Finds the max number in a given indicator list and then return that number and the state associated with that max number'''
    for index, max_in_list in enumerate(indicator_list):
        max_value = max(indicator_list)
        if max_in_list == max_value:
            max_index = index
            max_state = states_list[max_index]
    
    return max_state, max_value

def find_min (indicator_list):
    '''Finds the max number in a given indicator list and then return that number and the state associated with that max number'''
    for index, min_in_list in enumerate(indicator_list):
        min_value = min(indicator_list)
        if min_in_list == min_value:
            min_index = index
            min_state = states_list[min_index]
    
    return min_state, min_value



# def main ():
    
# filename = input("Input filename: ")
risk_file = open_file()
# risk_file = open('riskFactors.csv', 'r')
# indicator_list = extract_info(risk_file)
# print(indicator_list)
states_list, heart_list, motor_vehicle_list, teen_birth_list, adult_smoking_list, adult_obesity_list = extract_info(risk_file)

max_heart_state, max_heart = find_max(heart_list)
min_heart_state, min_heart = find_min(heart_list)
max_motor_vehicle_state, max_motor_vehicle = find_max(motor_vehicle_list)
min_motor_vehicle_state, min_motor_vehicle = find_min(motor_vehicle_list)
max_teen_birth_state, max_teen_birth = find_max(teen_birth_list)
min_teen_birth_state, min_teen_birth = find_min(teen_birth_list)
max_smoking_state, max_adult_smoking = find_max(adult_smoking_list)
min_smoking_state, min_adult_smoking = find_min(adult_smoking_list)
max_obesity_state, max_adult_obesity = find_max(adult_obesity_list)
min_obesity_state, min_adult_obesity = find_min(adult_obesity_list)


# print(indicator_list)
# print(max_index_obesity)
# print(max_obesity_state)

empty_space = " " * 6
print('{:<33s}{:<33s}{:<6s}'.format('Indicator', 'Min', 'Max'))
print('-' * 87)
print('{:<32s} {:<21s}{:>6}{}{:<15s}{:>6}'.format("Heart Disease Death Rate (2007):", min_heart_state, min_heart, empty_space, max_heart_state, max_heart))
print('{:<32s} {:<21s}{:>6}{}{:<15s}{:>6}'.format("Motor Vehicle Death Rate (2009):", min_motor_vehicle_state, min_motor_vehicle, empty_space, max_motor_vehicle_state, max_motor_vehicle))
print('{:<32s} {:<21s}{:>6}{}{:<15s}{:>6}'.format("Teen Birth Rate (2009):", min_teen_birth_state, min_teen_birth, empty_space, max_teen_birth_state, max_teen_birth))
print('{:<32s} {:<21s}{:>6}{}{:<15s}{:>6}'.format("Adult Smoking (2010):", min_smoking_state, min_adult_smoking, empty_space, max_smoking_state, max_adult_smoking))
print('{:<32s} {:<21s}{:>6}{}{:<15s}{:>6}'.format("Adult Obesity (2010):", min_obesity_state, min_adult_obesity, empty_space, max_obesity_state, max_adult_obesity))