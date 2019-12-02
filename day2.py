from common import read_int_inline
from copy import deepcopy


class StopProgram(Exception):
    pass


def run_program(numbers, cursor=0):
    if cursor+4 > len(numbers):
        raise ValueError("BOOM")

    opcode = numbers[cursor]
    if opcode == 99:
        raise StopProgram()

    value_1 = numbers[numbers[cursor+1]]
    value_2 = numbers[numbers[cursor+2]]
    result_pos = numbers[cursor+3]

    if opcode == 1:
        numbers[result_pos] = value_1 + value_2
    elif opcode == 2:
        numbers[result_pos] = value_1 * value_2
    else:
        raise ValueError("Unknown opcode.")

    cursor += 4
    run_program(numbers, cursor)


def init_and_run(input_data, noun=12, verb=2):
    data = deepcopy(input_data)
    data[1] = noun
    data[2] = verb

    try:
        run_program(data)
    except StopProgram:
        return data[0]


def produce_output(output=19690720):
    for noun in range(100):
        for verb in range(100):
            result = init_and_run(data, noun, verb)
            if result == output:
                return noun, verb


if __name__ == '__main__':

    data = read_int_inline('day2.txt')
    result = init_and_run(data)
    print(f'First: {result}')

    noun, verb = produce_output()
    print(f'Second: {100 * noun + verb}')

