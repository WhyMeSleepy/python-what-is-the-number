import random

def main():
    score = 0
    print('Guess the number between 1-10')
    for i in range(1,4):
        print(f'\n Round {i}')
        correct_number = random.randint(1,10)
        for repeat in range(1,4):
            number_input = int(input('Input your number :'))
            if correct_number != number_input:
                print('Wrong!!',end=' ')
                if repeat != 3:
                    print(f'You can try again in {3-repeat} times')
            else:
                print('Correct!!')
                score += 1
                break
        
    print(f'\n Your score is {score}')


if __name__ == '__main__':
    main()