# DIMAS MUHAMMAD ADNAN IMRAN - JC-DS-JKT-08
# PURWADHIKA MODULE 1 DATA SCIENCE EXAM

# SOAL 1

def Hashtag(string):
    a = '#'
    for i in string.split():
        a += i.capitalize()

    if len(a) > 140:
        print(False)
    elif a == '#':
        print(False)
    else:
        print(a)

print('\nJAWABAN NO. 1:\n')
Hashtag('Hello there how are you doing')
Hashtag('Hello World')
Hashtag('')
# Hashtag('dwauidhwiuhuuhfhufhuhfuisehfuehnndnsdjkfndsbgkbsdjbfkjnkjsnfjesnfjneskfjnkesjgnesgdnjdndjndjdnjdnjdnjndjandanddjanjnwjdnwakdnksndwmasndjkwadw')

# SOAL 2

def create_phone_number(number):
    try:
        print('({}{}{}) {}{}{}-{}{}{}{}' .format(number[0],number[1],number[2],number[3],number[4],number[5],number[6],number[7],number[8],number[9]))
    except:
        print(False)

print('\nJAWABAN NO. 2:\n')
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])

# SOAL 3

def sort_odd_even(num):
    
    odd_even = [0 for i in range(len(num))]

    odd_1 = []
    odd_2 = []
    even_1 = []
    even_2 = []

    for x, y in enumerate(num):
        if y % 2 != 0:
            odd_1.append(x)
            odd_2.append(y)
        else:
            even_1.append(x)
            even_2.append(y)

    for i in range(len(odd_2)):
        for j in range(i + 1, len(odd_2)):
            if odd_2[i] > odd_2[j]:
                odd_2[i], odd_2[j] = odd_2[j], odd_2[i]
    for i in range(len(even_2)):
        for j in range(i + 1, len(even_2)):
            if even_2[i] < even_2[j]:
                even_2[i], even_2[j] = even_2[j], even_2[i]

    for x, y in zip(odd_1, odd_2):
        odd_even[x] = y
    for x, y in zip(even_1, even_2):
        odd_even[x] = y
    print(odd_even)

print('\nJAWABAN NO. 3:\n')
sort_odd_even([5, 3, 2, 8, 1, 4])

# SOAL 4

def hollowTriangle(n):
    if n == 1:
        print('#')
        return False

    top = ['_' * (n) + '#' + '_' * (n)]
    mid = []
    bottom = ['#' * ((2 * n) - 1)]

    for i in range(n - 1, 0, -1):
        mid.append(('_' * i) + '#' + ('_' * ((2 * n) - (2 * i) - 3)) + '#' + ('_' * i))
    print(top[0])

    for i in mid:
        print(i)

    for i in bottom:
        print(i)

print('\nJAWABAN NO. 4:\n')
hollowTriangle(1)
hollowTriangle(2)
hollowTriangle(3)
hollowTriangle(4)
hollowTriangle(5)
hollowTriangle(6)