print('2.a.1')
classs: int = 103 // 30
left: int = 103 % 30
print(f'there {classs} full classes and {left} students left in the last class')

print('2.a.2')
while True:
    try:
        students: int = int(input('enter the number of students:'))
        break
    except:
        print('must be a number...')

classes: int = students // 30
left: int = students % 30
print(f'there {classes} full classes and {left} students left in the last class')

print('2.b:')
while True:
    try:
        x: int = int(input('enter a number between 10-99:'))
        if 10 > x < 99:
            print('Invalid number...try again ')
        else:
            break
    except ValueError as str:
        print('this is not a valid number')
        continue
asarot: int = x // 10
ahdot: int = x % 10

new_number: int = ahdot * 10 + asarot * 1
print(new_number)

print('2.c:')
for number in range(1, 201):
    is_prime = True

    if number < 2:
        is_prime = False
    else:
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
    if is_prime:
        print(number, end=' ')

print('2.d:')
a_count: int = 0
b_count: int = 0
c_count: int = 0
d_count: int = 0

while True:
    answer: str = input('enter a ,b , c or d , and x to finish: ')
    if answer == 'x':
        break
    elif answer == 'a':
        a_count += 1
    elif answer == 'b':
        b_count += 1
    elif answer == 'c':
        c_count += 1
    elif answer == 'd':
        d_count += 1
    else:
        print('Invalid answer, try again..')
print(f"Number of answer choices:'a'={a_count},'b'={b_count},'c'={c_count},'d'={d_count} ")
abcd_list: list[int] = [a_count, b_count, c_count, d_count]
print(f'the least', min(abcd_list))
print(f'the most', max(abcd_list))
