import math

from cyclophosphamide import Cyclophosphamide
from bag import Bag

def true_divide(x, y):
    i = 0
    while x%1 != 0:
        x *= 10
        y *= 10
        i += 1
    while y%1 != 0:
        x *= 10
        y *= 10
        i += 1
    #print("x = ", x, "y = ", y, "i = ", i)
    result = (x / y) 
    return result

def true_floor_division(x, y):
    return int(true_divide(x, y))

def true_multiply(x, y):
    i = 0
    while x%1 != 0:
        x *= 10
        y *= 10
        i += 2
    while y%1 != 0:
        x *= 10
        y *= 10
        i += 2
    #print("x = ", x, "y = ", y, "i = ", i)
    result = (x * y) / (10**i)
    return result

def true_subtraction(x, y):
    i = 0
    while x%1 != 0:
        x *= 10
        y *= 10
        i += 1
    while y%1 != 0:
        x *= 10
        y *= 10
        i += 1
    result = (x - y) / (10**i)
    return result

def true_addition(x, y):
    i = 0
    while x%1 != 0:
        x *= 10
        y *= 10
        i += 1
    while y%1 != 0:
        x *= 10
        y *= 10
        i += 1
    result = (x + y) / (10**i)
    return result

def true_mod(x, y):
    i = 0
    while x%1 != 0:
        x *= 10
        y *= 10
        i += 1
    while y%1 != 0:
        x *= 10
        y *= 10
        i += 1
    result = (x % y) 
    return result

def get_increment(vol):
    increment = 0
    if vol <= 3:
        increment = 0.05
    elif vol <= 10:
        increment = 0.1
    else:
        increment = 0.5
    return increment

def is_increment(vol):
    increment = get_increment(vol)
    if true_mod(vol, increment) == 0:
        return True
    return False

def to_measurable(vol):
    increment = get_increment(vol)
    if true_mod(vol, increment) == 0:
        result = vol
    else:
        result = true_multiply(true_floor_division(vol, increment),increment)
    return result

def next_lower_measurable(vol):
    if not is_increment(vol):
        raise Exception("Error: volume must be a measurable increment")
    increment = get_increment(vol)
    result = true_subtraction(vol, increment)
    
    if not is_increment(result):
        increment = get_increment(result)
        result = true_subtraction(vol, increment)
    
    return result

def next_higher_measurable(vol):
    if not is_increment(vol):
        raise Exception("Error: volume must be a measurable increment")
    increment = get_increment(vol)
    result = true_addition(vol, increment)
    
    if not is_increment(result):
        increment = get_increment(result)
        result = true_addition(vol, increment)
    
    return result

def to_volume(dose, conc):
    return true_divide(dose, conc)

def to_dose(vol, conc):
    return true_multiply(conc, vol)

def generate_desensitization(drug, dose):
    bag_list = []
    for i in range(1, drug.total_bag_num() + 1):
        bag_list.append(Bag(drug.name(), dose * drug.bags()[i]["dose_modifier"], drug.units(), drug.bags()[i]["diluent_bag"], drug.bags()[i]["diluent_bag_size"]))

    for i in range(1, drug.total_bag_num() + 1):
        bag_dose = bag_list[i-1].dose
        dose_conc = drug.bags()[i]["drug_conc_added"]
        dose_vol = to_volume(bag_dose, dose_conc)
        dose_vol = to_measurable(dose_vol)
        new_bag_dose = to_dose(dose_vol, dose_conc)
        bag_list[i-1].dose = new_bag_dose

    new_total_dose = 0
    for bag in bag_list:
        new_total_dose = true_addition(new_total_dose, bag.dose)
    dose_difference = true_subtraction(dose, new_total_dose)

    if dose_difference != 0:
        for i in range(len(bag_list)-1, -1, -1):
            bag_dose = bag_list[i].dose
            bag_dose_up = to_dose(next_higher_measurable(to_volume(bag_dose, drug.bags()[i+1]["drug_conc_added"])), drug.bags()[i+1]["drug_conc_added"])

            adjustment = 0
            while (true_subtraction(bag_dose_up, bag_dose) <= dose_difference) and (adjustment < dose_difference):
                adjustment += true_subtraction(bag_dose_up, bag_dose)
                bag_dose = bag_dose_up
                bag_dose_up = to_dose(next_higher_measurable(to_volume(bag_dose, drug.bags()[i+1]["drug_conc_added"])), drug.bags()[i+1]["drug_conc_added"])
            
            bag_list[i].dose += adjustment
            dose_difference -= adjustment 

    return bag_list

def generate_desensitization_instructions(drug, dose):
    instructions = f"Generating {drug.name()} {dose} {drug.units()} desensitization...\n\n"
    
    instructions += "Bag List:\n" 
    bag_list = generate_desensitization(drug, dose)
    i = 1
    for bag in bag_list:
        this_dose = bag.dose
        if true_mod(this_dose, 1) == 0:
            this_dose = int(this_dose)
        instructions += f"\tBag {i}) {bag.drug} {this_dose} {bag.units} in {bag.diluent} {bag.volume} mL\n"
        i+=1

    instructions += "\nDilution Instructions:\n"
    dilution_num = drug.dilution_num()
    if dilution_num == 1:
        s = "dilution"
    elif dilution_num > 1:
        s = "dilutions"
    instructions += f"\tThis desensitization will have {dilution_num} {s}.\n\n"
    for i in range(1, drug.dilution_num() + 1):
        instructions += f"Step {i}:\n"
        instructions += f"\t[] Draw up {drug.dilutions()[i]['drug_vol']} mL of {drug.name()} at {drug.dilutions()[i]['initial_conc']} {drug.units()}/mL and add to an empty reservoir vial\n" 
        instructions += f"\t[] Draw up {drug.dilutions()[i]['diluent_amount']} mL of {drug.dilutions()[i]['diluent']} and add to the reservoir vial\n"
        x = drug.dilutions()[i]['drug_vol'] + drug.dilutions()[i]['diluent_amount']
        instructions += f"\t[] The reservoir now contains {x} mL of {drug.name()} at {drug.dilutions()[i]['final_conc']} {drug.units()}/mL\n\n"

    instructions += "Desensitization Bag Preperation:\n\n"
    for i in range (1, len(bag_list)+1):
        this_dose = bag_list[i-1].dose
        if true_mod(this_dose, 1) == 0:
            this_dose = int(this_dose)
        instructions += f"Bag {i}: {bag.drug} {this_dose} {bag.units} in {bag.diluent} {bag.volume} mL\n"
        dose_conc = drug.bags()[i]["drug_conc_added"]
        dose_vol = to_volume(bag_list[i-1].dose, dose_conc)
        dose_vol = to_measurable(dose_vol) 
        instructions += f"\t[] Draw up {dose_vol} mL of {drug.name()} at {drug.bags()[i]['drug_conc_added']} {drug.units()}/mL\n"
        instructions += f"\t[] Add drug volume to a {drug.bags()[i]['diluent_bag']} {drug.bags()[i]['diluent_bag_size']} mL bag\n\n"
    return instructions

