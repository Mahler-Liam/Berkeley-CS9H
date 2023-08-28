def print_banner():
    """
    Print the program banner. You may change the banner message.
    """
    # START OF YOUR CODE
    print(
    "Welcome to our Python-powered Unit Converter v1.0 by weiyuchoumou!\n "
    "You can convert Distances, Weights, Volumes to one another, but only\n "
    "within units of the same category, which are shown below. E.g.: 1 mi in ft \n"
    "\n"
    "\n"
    "  Distances: ft cm mm mi m yd km in\n"
    "    Weights: lb mg kg oz g\n "
    "    Volumes: floz qt cup mL L gal pint\n"
    )
    # END OF YOUR CODE


def convert(command):
    """
    Handle a SINGLE user input, which given the command, either print
    the conversion result, or print an error, or exit the program.
    Please follow the requirements listed on project website.
    :param command: User input

    >>> convert("1 m in km")
    1 m = 0.001000 km
    """
    # START OF YOUR CODE

    def is_numeric(string):
        try:
            float(string)
            return True
        except:
            return False
        
    distances_list = ['m', 'cm', 'mm', 'km', 'in', 'ft', 'yd', 'mi']
    volumes_list = ['L', 'mL', 'floz', 'cup', 'pint', 'qt', 'gal']
    weights_list = ['g', 'kg', 'mg', 'oz', 'lb']

    if command == "q":
        print("Thanks for converting with us. Y'll come back now, y'hear?")
        return False 
    else:
        command_words = command.split()
        if len(command_words) != 4:
            print('Error: Wrong Format!')
        else:
            command_tuple = tuple(command_words)
            amount, source_unit, prep, destination_unit = command_tuple
            whether_convert = 1

            if source_unit in distances_list:
                if destination_unit not in distances_list:
                    whether_convert = 0
                    print('Error: Units Mismatch!')
                if not is_numeric(amount):
                    whether_convert = 0
                    print('Error: Source_unit is not an amount!')
                if prep != 'in':
                    whether_convert = 0
                    print('Error: Wrong prep!')
            elif source_unit in volumes_list:
                if destination_unit not in volumes_list:
                    whether_convert = 0
                    print('Error: Units Mismatch!')
                if not is_numeric(amount):
                    whether_convert = 0
                    print('Error: Source_unit is not an amount!')
                if prep != 'in':
                    whether_convert = 0
                    print('Error: Wrong prep!')
            elif source_unit in weights_list:
                if destination_unit not in weights_list:
                    whether_convert = 0 
                    print('Error: Units Mismatch!')
                if not is_numeric(amount):
                    whether_convert = 0
                    print('Error: Source_unit is not an amount!')
                if prep != 'in':
                    whether_convert = 0
                    print('Error: Wrong prep!')
            elif (source_unit not in distances_list) and (source_unit not in volumes_list) and (source_unit not in weights_list):
                whether_convert = 0
                print('Error: Units Undefined!')

            if whether_convert:
                if source_unit in distances_list:
                    convert_distances(amount, source_unit, destination_unit)
                if source_unit in volumes_list:
                    convert_volumes(amount, source_unit, destination_unit)
                if source_unit in weights_list:
                    convert_weights(amount, source_unit, destination_unit)
        

    # END OF YOUR CODE


# TODO: Add Other Functions Here




def convert_distances(amount, source_unit, destination_unit):
    
    base_unit = 'm'
    km_m = 1000.000000
    cm_m = 0.010000
    mm_m = 0.001000
    in_m = 0.025400
    ft_m = 0.304800
    yd_m = 0.914400
    mi_m = 1609.344000
    
    if destination_unit == base_unit:
        if source_unit == 'km':
            print("%s km = %.6f m" % (amount, km_m * float(amount)))
        if source_unit == 'cm':
            print("%s cm = %.6f m" % (amount, cm_m * float(amount)))
        if source_unit == 'mm':
            print("%s mm = %.6f m" % (amount, mm_m * float(amount)))
        if source_unit == 'in':
            print("%s in = %.6f m" % (amount, in_m * float(amount)))
        if source_unit == 'ft':
            print("%s ft = %.6f m" % (amount, ft_m * float(amount)))
        if source_unit == 'yd':
            print("%s yd = %.6f m" % (amount, yd_m * float(amount)))
        if source_unit == 'mi':
            print("%s mi = %.6f m" % (amount, mi_m * float(amount)))
    elif destination_unit == 'cm':
        if source_unit == 'm':
            print("%s m = %.6f cm" % (amount, 1/cm_m * float(amount)))
        if source_unit == 'mm':
            print("%s mm = %.6f cm" % (amount, mm_m * float(amount) *(1/cm_m)))
        if source_unit == 'km':
            print("%s km = %.6f cm" % (amount, km_m * float(amount) *(1/cm_m)))
        if source_unit == 'in':
            print("%s in = %.6f cm" % (amount, in_m * float(amount) *(1/cm_m)))
        if source_unit == 'ft':
            print("%s ft = %.6f cm" % (amount, ft_m * float(amount) *(1/cm_m)))
        if source_unit == 'yd':
            print("%s yd = %.6f cm" % (amount, yd_m * float(amount) *(1/cm_m)))
        if source_unit == 'mi':
            print("%s mi = %.6f cm" % (amount, mi_m * float(amount) *(1/cm_m)))
    elif destination_unit == 'mm':
        if source_unit == 'm':
            print("%s m = %.6f mm" % (amount, 1/mm_m * float(amount)))
        if source_unit == 'cm':
            print("%s cm = %.6f mm" % (amount, cm_m * float(amount) *(1/mm_m)))
        if source_unit == 'km':
            print("%s km = %.6f mm" % (amount, km_m * float(amount) *(1/mm_m)))
        if source_unit == 'in':
            print("%s in = %.6f mm" % (amount, in_m * float(amount) *(1/mm_m)))
        if source_unit == 'ft':
            print("%s ft = %.6f mm" % (amount, ft_m * float(amount) *(1/mm_m)))
        if source_unit == 'yd':
            print("%s yd = %.6f mm" % (amount, yd_m * float(amount) *(1/mm_m)))
        if source_unit == 'mi':
            print("%s mi = %.6f mm" % (amount, mi_m * float(amount) *(1/mm_m)))
    elif destination_unit == 'km':
        if source_unit == 'm':
            print("%s m = %.6f km" % (amount, 1/km_m * float(amount)))
        if source_unit == 'cm':
            print("%s cm = %.6f km" % (amount, cm_m * float(amount) *(1/km_m)))
        if source_unit == 'mm':
            print("%s mm = %.6f km" % (amount, mm_m * float(amount) *(1/km_m)))
        if source_unit == 'in':
            print("%s in = %.6f km" % (amount, in_m * float(amount) *(1/km_m)))
        if source_unit == 'ft':
            print("%s ft = %.6f km" % (amount, ft_m * float(amount) *(1/km_m)))
        if source_unit == 'yd':
            print("%s yd = %.6f km" % (amount, yd_m * float(amount) *(1/km_m)))
        if source_unit == 'mi':
            print("%s mi = %.6f km" % (amount, mi_m * float(amount) *(1/km_m)))
    elif destination_unit == 'in':
        if source_unit == 'm':
            print("%s m = %.6f in" % (amount, 1/in_m * float(amount)))
        if source_unit == 'cm':
            print("%s cm = %.6f in" % (amount, cm_m * float(amount) *(1/in_m)))
        if source_unit == 'mm':
            print("%s mm = %.6f in" % (amount, mm_m * float(amount) *(1/in_m)))
        if source_unit == 'km':
            print("%s km = %.6f in" % (amount, km_m * float(amount) *(1/in_m)))
        if source_unit == 'ft':
            print("%s ft = %.6f in" % (amount, ft_m * float(amount) *(1/in_m)))
        if source_unit == 'yd':
            print("%s yd = %.6f in" % (amount, yd_m * float(amount) *(1/in_m)))
        if source_unit == 'mi':
            print("%s mi = %.6f in" % (amount, mi_m * float(amount) *(1/in_m)))
    elif destination_unit == 'ft':
        if source_unit == 'm':
            print("%s m = %.6f ft" % (amount, 1/ft_m * float(amount)))
        if source_unit == 'cm':
            print("%s cm = %.6f ft" % (amount, cm_m * float(amount) *(1/ft_m)))
        if source_unit == 'mm':
            print("%s mm = %.6f ft" % (amount, mm_m * float(amount) *(1/ft_m)))
        if source_unit == 'km':
            print("%s km = %.6f ft" % (amount, km_m * float(amount) *(1/ft_m)))
        if source_unit == 'in':
            print("%s in = %.6f ft" % (amount, in_m * float(amount) *(1/ft_m)))
        if source_unit == 'yd':
            print("%s yd = %.6f ft" % (amount, yd_m * float(amount) *(1/ft_m)))
        if source_unit == 'mi':
            print("% mi = %.6f ft" % (amount, mi_m * float(amount) *(1/ft_m)))
    elif destination_unit == 'yd':
        if source_unit == 'm':
            print("%s m = %.6f yd" % (amount, 1/yd_m * float(amount)))
        if source_unit == 'cm':
            print("%s cm = %.6f yd" % (amount, cm_m * float(amount) *(1/yd_m)))
        if source_unit == 'mm':
            print("%s mm = %.6f yd" % (amount, mm_m * float(amount) *(1/yd_m)))
        if source_unit == 'km':
            print("%s km = %.6f yd" % (amount, km_m * float(amount) *(1/yd_m)))
        if source_unit == 'in':
            print("%s in = %.6f yd" % (amount, in_m * float(amount) *(1/yd_m)))
        if source_unit == 'ft':
            print("%s ft = %.6f yd" % (amount, ft_m * float(amount) *(1/yd_m)))
        if source_unit == 'mi':
            print("%s mi = %.6f yd" % (amount, mi_m * float(amount) *(1/yd_m)))
    elif destination_unit == 'mi':
        if source_unit == 'm':
            print("%s m = %.6f mi" % (amount, 1/mi_m * float(amount)))
        if source_unit == 'cm':
            print("%s cm = %.6f mi" % (amount, cm_m * float(amount) *(1/mi_m)))
        if source_unit == 'mm':
            print("%s mm = %.6f mi" % (amount, mm_m * float(amount) *(1/mi_m)))
        if source_unit == 'km':
            print("%s km = %.6f mi" % (amount, km_m * float(amount) *(1/mi_m)))
        if source_unit == 'in':
            print("%s in = %.6f mi" % (amount, in_m * float(amount) *(1/mi_m)))
        if source_unit == 'ft':
            print("%s ft = %.6f mi" % (amount, ft_m * float(amount) *(1/mi_m)))
        if source_unit == 'yd':
            print("%s yd = %.6f mi" % (amount, yd_m * float(amount) *(1/mi_m)))
        





def convert_volumes(amount, source_unit, destination_unit):
   
    mL_L = 0.001000
    floz_L = 0.0295735296
    cup_L = 0.236588237
    pint_L = 0.473176473
    qt_L = 0.946352946
    gal_L = 3.7854117

    if destination_unit == 'L':
        if source_unit == 'mL':
            print("%s mL = %.6f L" % (amount, mL_L * float(amount)))
        if source_unit == 'floz':
            print("%s floz = %.6f L" % (amount, floz_L * float(amount)))
        if source_unit == 'cup':
            print("%s cup = %.6f L" % (amount, cup_L * float(amount)))
        if source_unit == 'pint':
            print("%s pint = %.6f L" % (amount, pint_L * float(amount)))
        if source_unit == 'qt':
            print("%s qt = %.6f L" % (amount, qt_L * float(amount)))
        if source_unit == 'gal':
            print("%s gal = %.6f L" % (amount, gal_L * float(amount)))
    elif destination_unit == 'mL':
        if source_unit == 'L':
            print("%s L = %.6f mL" % (amount, 1/mL_L * float(amount)))
        if source_unit == 'floz':
            print("%s floz = %.6f mL" % (amount, (float)(1/mL_L) * floz_L * float(amount)))
        if source_unit == 'cup':
            print("%s cup = %.6f mL" % (amount, (1/mL_L) * cup_L * float(amount)))
        if source_unit == 'pint':
            print("%s pint = %.6f mL" % (amount, (1/mL_L) * pint_L * float(amount)))
        if source_unit == 'qt':
            print("%s qt = %.6f mL" % (amount, (1/mL_L) * qt_L * float(amount)))
        if source_unit == 'gal':
            print("%s gal = %.6f mL" % (amount, (1/mL_L) * gal_L * float(amount)))
    elif destination_unit == 'floz':
        if source_unit == 'L':
            print("%s L = %.6f floz" % (amount, 1/floz_L * float(amount)))
        if source_unit == 'mL':
            print("%s mL = %.6f floz" % (amount, (1/floz_L) * mL_L * float(amount)))
        if source_unit == 'cup':
            print("%s cup = %.6f floz" % (amount, (1/floz_L) * cup_L * float(amount)))
        if source_unit == 'pint':
            print("%s pint = %.6f floz" % (amount, (1/floz_L) * pint_L * float(amount)))
        if source_unit == 'qt':
            print("%s qt = %.6f floz" % (amount, (1/floz_L) * qt_L * float(amount)))
        if source_unit == 'gal':
            print("%s gal = %.6f floz" % (amount, (1/floz_L) * gal_L * float(amount)))
    elif destination_unit == 'cup':
        if source_unit == 'L':
            print("%s L = %.6f cup" % (amount, 1/cup_L * float(amount)))
        if source_unit == 'mL':
            print("%s mL = %.6f cup" % (amount, (1/cup_L) * mL_L * float(amount)))
        if source_unit == 'floz':
            print("%s floz = %.6f cup" % (amount, (1/cup_L) * floz_L * float(amount)))
        if source_unit == 'pint':
            print("%s pint = %.6f cup" % (amount, (1/cup_L) * pint_L * float(amount)))
        if source_unit == 'qt':
            print("%s qt = %.6f cup" % (amount, (1/cup_L) * qt_L * float(amount)))
        if source_unit == 'gal':
            print("%s gal = %.6f cup" % (amount, (1/cup_L) * gal_L * float(amount)))
    elif destination_unit == 'pint':
        if source_unit == 'L':
            print("%s L = %.6f pint" % (amount, 1/pint_L * float(amount)))
        if source_unit == 'mL':
            print("%s mL = %.6f pint" % (amount, (1/pint_L) * mL_L * float(amount)))
        if source_unit == 'floz':
            print("%s floz = %.6f pint" % (amount, (1/pint_L) * floz_L * float(amount)))
        if source_unit == 'cup':
            print("%s cup = %.6f pint" % (amount, (1/pint_L) * cup_L * float(amount)))
        if source_unit == 'qt':
            print("%s qt = %.6f pint" % (amount, (1/pint_L) * qt_L * float(amount)))
        if source_unit == 'gal':
            print("%s gal = %.6f pint" % (amount, (1/pint_L) * gal_L * float(amount)))
    elif destination_unit == 'qt':
        if source_unit == 'L':
            print("%s L = %.6f qt" % (amount, 1/qt_L * float(amount)))
        if source_unit == 'mL':
            print("%s mL = %.6f qt" % (amount, (1/qt_L) * mL_L * float(amount)))
        if source_unit == 'floz':
            print("%s floz = %.6f qt" % (amount, (1/qt_L) * floz_L * float(amount)))
        if source_unit == 'cup':
            print("%s cup = %.6f qt" % (amount, (1/qt_L) * cup_L * float(amount)))
        if source_unit == 'pint':
            print("%s pint = %.6f qt" % (amount, (1/qt_L) * pint_L * float(amount)))
        if source_unit == 'gal':
            print("%s gal = %.6f qt" % (amount, (1/qt_L) * gal_L * float(amount)))
    elif destination_unit == 'gal':
        if source_unit == 'L':
            print("%s L = %.6f gal" % (amount, 1/gal_L * float(amount)))
        if source_unit == 'mL':
            print("%s mL = %.6f gal" % (amount, (1/gal_L) * mL_L * float(amount)))
        if source_unit == 'floz':
            print("%s floz = %.6f gal" % (amount, (1/gal_L) * floz_L * float(amount)))
        if source_unit == 'cup':
            print("%s cup = %.6f gal" % (amount, (1/gal_L) * cup_L * float(amount)))
        if source_unit == 'pint':
            print("%s pint = %.6f gal" % (amount, (1/gal_L) * pint_L * float(amount)))
        if source_unit == 'qt':
            print("%s qt = %.6f gal" % (amount, (1/gal_L) * qt_L * float(amount)))

def convert_weights(amount, source_unit, destination_unit):
    
    kg_g = 1000.000000
    mg_g = 0.001000
    oz_g = 28.3495231
    lb_g = 453.592370

    if destination_unit == 'g':
        if source_unit == 'kg':
            print("%s kg = %.6f g" % (amount, kg_g * float(amount)))
        if source_unit == 'mg':
            print("%s mg = %.6f g" % (amount, mg_g * float(amount)))
        if source_unit == 'oz':
            print("%s oz = %.6f g" % (amount, oz_g * float(amount)))
        if source_unit == 'lb':
            print("%s lb = %.6f g" % (amount, lb_g * float(amount)))
    elif destination_unit == 'kg':
        if source_unit == 'g':
            print("%s g = %.6f kg" % (amount, (1/kg_g) * float(amount)))
        if source_unit == 'mg':
            print("%s mg = %.6f kg" % (amount, (1/kg_g) * mg_g * float(amount)))
        if source_unit == 'oz':
            print("%s oz = %.6f kg" % (amount, (1/kg_g) * oz_g * float(amount)))
        if source_unit == 'lb':
            print("%s lb = %.6f kg" % (amount, (1/kg_g) * lb_g * float(amount)))
    elif destination_unit == 'mg':
        if source_unit == 'g':
            print("%s g = %.6f mg" % (amount, (1/mg_g) * float(amount)))
        if source_unit == 'kg':
            print("%s kg = %.6f mg" % (amount, (1/mg_g) * kg_g * float(amount)))
        if source_unit == 'oz':
            print("%s oz = %.6f mg" % (amount, (1/mg_g) * oz_g * float(amount)))
        if source_unit == 'lb':
            print("%s lb = %.6f mg" % (amount, (1/mg_g) * lb_g * float(amount)))
    elif destination_unit == 'oz':
        if source_unit == 'g':
            print("%s g = %.6f oz" % (amount, (1/oz_g) * float(amount)))
        if source_unit == 'kg':
            print("%s kg = %.6f oz" % (amount, (1/oz_g) * kg_g * float(amount)))
        if source_unit == 'mg':
            print("%s mg = %.6f oz" % (amount, (1/oz_g) * mg_g * float(amount)))
        if source_unit == 'lb':
            print("%s lb = %.6f oz" % (amount, (1/oz_g) * lb_g * float(amount)))
    elif destination_unit == 'lb':
        if source_unit == 'g':
            print("%s g = %.6f lb" % (amount, (1/lb_g) * float(amount)))
        if source_unit == 'kg':
            print("%s kg = %.6f lb" % (amount, (1/lb_g) * kg_g * float(amount)))
        if source_unit == 'mg':
            print("%s mg = %.6f lb" % (amount, (1/lb_g) * mg_g * float(amount)))
        if source_unit == 'oz':
            print("%s oz = %.6f lb" % (amount, (1/lb_g) * oz_g * float(amount)))
    


###########################################
# DO NOT MODIFY ANYTHING BELOW
###########################################

def get_user_input():
    """
    Print the prompt and wait for user input
    :return: User input
    """
    return input("Convert [AMT SOURCE_UNIT in DEST_UNIT, or (q)uit]: ")


if __name__ == '__main__':
    print_banner()
    while True:
        command = get_user_input()
        convert(command)
