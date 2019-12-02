from common import get_input_entries


def get_fuel_requirement(module_mass):
    """find the fuel required for a module, take its mass, divide by three, round down, and subtract 2"""
    return module_mass//3-2


def get_total_fuel_requirements(module_mass):

    result = get_fuel_requirement(module_mass)

    if result <= 0:
        return 0

    result += get_total_fuel_requirements(result)
    return result


if __name__ == '__main__':
    input_data = get_input_entries('day1.txt')

    day1_result = sum([get_fuel_requirement(int(entry)) for entry in input_data])
    print(f'day 1: {day1_result}')

    day1_result = sum([get_total_fuel_requirements(int(entry)) for entry in input_data])
    print(f'day 2: {day1_result}')
