import sys

def change_2_numbers(sequence, contador, bit='1'):
    sequence = list(sequence)
    sequence = [x for x in sequence if x != " "]
    sequence[contador] = bit
    sequence[contador+1] = bit
    return " ".join(sequence)

def change_1_number(sequence, contador , first=True):
    sequence = list(sequence)
    sequence = [x for x in sequence if x != " "]
    if first:
        sequence[contador] = '0'
    else:
        sequence[contador+1] = '0'
        sequence[contador] = '1'
    return " ".join(sequence)

def print_receive(sequence):
    print('Q', sequence.strip())
    sys.stdout.flush()
    return int(input())

def calculate():
    times = int(input())
    for time in range(times):
        # first time, just creating and sending first sequence
        query_size = int(input())
        sequence = query_size * '0 '
        contador = 0
        print('Q', sequence.strip())
        sys.stdout.flush()
        correct_bits = int(input())
        last_correct_bits = correct_bits

        while True:
            # border cases
            if correct_bits == 0:
                sequence = sequence.replace('0', '*')
                sequence = sequence.replace('1', '0')
                sequence = sequence.replace('*', '1')
                break
            # border cases
            if correct_bits == query_size:
                break

            # first non automated query
            sequence = change_2_numbers(sequence, contador)

            correct_bits = print_receive(sequence)

            if correct_bits < last_correct_bits:
                sequence = change_2_numbers(sequence, contador, '0')
            elif correct_bits == last_correct_bits:
                last_correct_bits = correct_bits
                sequence = change_1_number(sequence, contador)
                correct_bits = print_receive(sequence)
                if correct_bits < last_correct_bits:
                    sequence = change_1_number(sequence, contador, first=False)
                    correct_bits = correct_bits + 2
                    if correct_bits == query_size:
                        break
                    # correct_bits = print_receive(sequence)
            if correct_bits > last_correct_bits:
                last_correct_bits = correct_bits
            contador = contador + 2
            if contador > query_size:
                break
        print('A', sequence.strip())
        sys.stdout.flush()
if __name__ == '__main__':
    calculate()
