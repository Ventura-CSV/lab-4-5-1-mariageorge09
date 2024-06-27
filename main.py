import random
def main():
    id = 0
    total = 0
    numbers = [0] * 5
    while ( id < 5):
        numbers[id] = random.randint (0, 100)
        total += numbers[id]
        id = id + 1
    print('Output ')
    print(numbers)
    print(f'The total sum is {total}')

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()
