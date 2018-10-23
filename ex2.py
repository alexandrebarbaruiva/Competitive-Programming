import sys

times = int(input())
for time in range(times):
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

        sequence = list(sequence)
        sequence = [x for x in sequence if x != " "]
        sequence[contador] = '1'
        sequence = " ".join(sequence)
        print('Q', sequence.strip())
        sys.stdout.flush()
        correct_bits = int(input())
        if last_correct_bits-correct_bits == 1:
            sequence = list(sequence)
            sequence = [x for x in sequence if x != " "]
            sequence[contador] = '1'
            sequence = " ".join(sequence)

        if correct_bits <= last_correct_bits:
            sequence = list(sequence)
            sequence = [x for x in sequence if x != " "]
            sequence[contador] = '0'
            sequence = " ".join(sequence)

        if (contador+2) == query_size:
            if correct_bits == query_size - 2 \
                    and correct_bits + 1 == last_correct_bits:
                pos = contador + 1
                print(pos, len(sequence))
                sequence = list(sequence)
                sequence = [x for x in sequence if x != " "]
                sequence[pos] = sequence[pos].replace('0', '*')
                sequence[pos] = sequence[pos].replace('1', '0')
                sequence[pos] = sequence[pos].replace('*', '1')
                sequence = " ".join(sequence)
                break
        last_correct_bits = correct_bits
        contador = contador+1
        if contador >= query_size:
            break
    print('A', sequence.strip())
    sys.stdout.flush()
