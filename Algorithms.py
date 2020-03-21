# 1 Second largest number in List [1, 3, 4, 5, 0, 2, 5]

given_list = [1, 3, 4, 5, 0, 2, 3, 7, 10, 9, 10]

def second_largest(given_list):
    set1 = set()
    for i in given_list:
        set1.add(i)

    largest = None
    second_largest = None
    for current_number in set1:
        if largest == None:
            largest = current_number
        elif current_number > largest:
            second_largest = largest
            largest = current_number
        elif second_largest == None:
            second_largest = current_number
        elif current_number > second_largest:
            second_largest = current_number
    return second_largest

print(second_largest(given_list))
print(second_largest([-2, -1]))
print(second_largest([2, 2, 1]))

# 2 A larger than B

def larger_than(a, b):
    if len(a) > len(b):
        return True
    elif len(a) < len(b):
        return False
    for i in range(len(a)):
        if a[i] == b[i]:
            continue
        elif a[i] > b[i]:
            return True
        elif a[i] < b[i]:
            return False
    return False

print(larger_than("2", "1"))

# 3 Palindrome

p1 = "-12"
p2 = "1221"
p3 = "123421"

def palindrome(string1):
    string2 = string1[::-1]
    if int(string1) < 0:
        print ("{} it is negative number".format(string1))
    elif string1 == string2:
        print ("{} it is a palindrome".format(string1))
    else:
        print ("{} it is not a palindrome".format(string1))

#input = raw_input("Enter number: ")
#print palindrome(input)

palindrome(p1)
palindrome(p2)
palindrome(p3)

# 4 Sum of elements divided per 3 and 5 between 1 and 100

total = 0
for i in range(1, 101):
    if i % 3 == 0 or i % 5 == 0:
        total += i
print(total)

# or how many numbers
total2 = 0
for i in range(1, 101):
    if i % 3 == 0 or i % 5 == 0:
        total2 += 1
print(total2)

# 5 Reverse

s = "Hello world!"

def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str

print(reverse(s))

# + list

A1 = [1, 2, 3, 4, 5]

def reverse(A):
    print(A)
    N = len(A)
    for k in range(N//2):
        A[k], A[N - 1 - k] = A[N - 1 - k], A[k]
    print(A)

reverse(A1)

# 6 Print unique numbers

n1 = [1, 2, 1, 2, 3, 4, 5, 4]

set1 = set()
for i in n1:
    set1.add(i)
print(set1)

# 7 Print unique letters

n4 = list(dict.fromkeys('aaabcabccd'))
print(n4)

# 8 Count unique letters

n5 = 'aaabcabccd'
print(n5.count('a'))

# 9 Find max number

given_list2 = [-2, 1, 3, 5, 0]

def find_max(given_list2):
    current_max = None
    for item in given_list2:
        if current_max == None:
            current_max = item
        elif item > current_max:
            current_max = item
    return current_max

print(find_max(given_list2))

# 10 Find the overlap between two lists

a = [1, 3, 4, 6, 7, 9]
b = [1, 2, 4, 5, 9, 10]

def common_element(a, b):
    p1 = 0
    p2 = 0
    result = []
    while p1 < len(a) and p2 < len(b):
        if a[p1] == b[p2]:
            result.append(a[p1])
            p1 += 1
            p2 += 1
        elif a[p1] > b[p2]:
            p2 += 1
        else:
            p1 += 1
    return result

print(common_element(a, b))


#list1 = [1, 2, 3, 5, 6, 9, 14]
#list2 = [1, 5, 6, 15, 17, 21]

#def find_overlap(list1, list2):
#    for i in list1:
#        if i in list2:
#            print i
#    pass

#find_overlap(list1, list2)

# 11 Count characters in message

message = 'Hello. Try count all letters in this message.'
count = {}

for character in message.upper():
    count.setdefault(character, 0)
    count[character] += 1

print(count)

# 12 Anagram Palindrome

def anagramPalindrome(string1):
    count = {}
    for character in string1:
        count.setdefault(character, 0)
        count[character] += 1

    total = 0
    for character in count:
        if count[character] % 2 != 0:
            total += 1

    if total > 1:
        return False
    else:
        return True

print(anagramPalindrome("carrace"))  # True
print(anagramPalindrome("cutoo"))  # False

# 13 Change first letter for capitalize in every word of string

string1 = 'create your document today'

def firstLetterCapitalized(string1):
    upperWords = [word[0].upper() + word[1:] for word in string1.split()]
    string1 = ' '.join(upperWords)
    print (string1)

print(firstLetterCapitalized(string1))

# 14 Print longest word

words = ["alpha", "omega", "up", "down", "over", "under", "purple", "red", "blue", "green"]
sortedwords = sorted(words, key=len)
print("The longest word in the list is: %s." % (sortedwords[-1]))

# 15 Check if digit

List = ['1', '#2', '3']

for i in List:
    if i.isdigit():
        print (i, 'with index:', List.index(i))
    else:
        print(i, "is not a digit")

# 16 Find biggest difference between two numbers

a = [1,2,3,5]

def maxDifference(a):
    max_diff = a[1] - a[0]

    for i in range(0, len(a)):
        for j in range(i + 1, len(a)):
            if (a[j] - a[i] > max_diff):
                max_diff = a[j] - a[i]
    return max_diff

print(maxDifference(a))

# 17 Print duplicates numbers

numbers = [1,2,3,2,1,5,6,5,5,5]

def countDuplicates(numbers):
    import collections
    return [item for item, count in collections.Counter(numbers).items() if count > 1]

print(countDuplicates(numbers))

# or

numbers = [1,2,3,2,1,5,6,5,5,5]

def countDuplicates(numbers):

    count = {}

    for number in numbers:
        if number in count:
            count[number] += 1
        else:
            count[number] = 1

    return (dict((k, v) for k, v in count.items() if v > 1))

print(countDuplicates(numbers))

# 18 Delete letter, missing_char('kitten', 1) -> 'ktten'

def missing_char(str, n):
    string1 = str.replace(str[n], "")
    return string1

print(missing_char("Hello", 1))

# 19 Return string when first and last chars have been exchange

str = 'Hello'

def front_back(str):
    if len(str) <= 1:
        return str
    return str[-1] + str[1:len(str)-1] + str[0]

print(front_back(str)) # oellH

# + numbers

list = [1,2,3,4,5]

def changeFL(list):
    mid = list[1:len(list)-1]
    first = list[0]
    last = list[-1]
    mid.insert(0, last)
    mid.insert(len(list)-1, first)
    return mid

print(changeFL(list))  # [5, 2, 3, 4, 1]

# 20 Return double_char('Hi-There') -> 'HHii--TThheerree'

def double_char(str):
    c = ''
    for i in range(len(str)):
        c += str[i] * 2
    return c

print(double_char('Hi-There'))

# 21 First Recurring Character

def first_reccuring(given_string):
    counts = {}
    for char in given_string:
        if char in counts:
            return char
        else:
            counts[char] = 1
    return None

print(first_reccuring('DBCABA')) # B

# 22 Find non_repeating

def non_repeating(a):
    count = {}
    for c in a:
        if c in count:
            count[c] += 1
        else:
            count[c] = 1

    for c in a:
        if count[c] == 1:
            return c
    return None


me = 'aabce'
print(non_repeating(me)) # b

# 23 Return the number of times that the string "code" appears anywhere in the given string,
#  except we'll accept any letter for the 'd', so "cope" and "cooe" count.

def count_code(str):
    total = 0
    for i in range(0,len(str)-3):
        if str[i:i+2] == 'co' and str[i+3] == 'e':
            total += 1
    return total

print(count_code('aaacodebbb')) # 1
print(count_code('codexxcode')) # 2

# 24 Create new dictionary with elements from 2 other dictionaries

d1 = {'apple': 10, 'banana': 5}
d2 = {'apple': 5, 'pears': 3}
d3 = {}

d3 = d1
for i in d2:
    if i in d1:
        d3[i] += d2[i]
    elif i not in d1:
        d3[i] = d2[i]

print(d3)

del d3['pears']
print(d3)

# 25 Prime numbers

for n in range(51):
    if (n == 0 or n == 1):  # Handles case for n == 0 or n == 1
        continue
    if (n == 2):    # Handles case for n == 2
        print(n, " is prime")
    for i in range(2, n):
        if (n % i == 0):  # If n%i == 0 then we know n cannot be prime. Ex: 4%2, 8%2.
            break
        if (i == n - 1):  # This means we have evaluated every possible divisor besides n.
            print(n, " is prime.")

# 26 Linear search - O(N) - best case O(1)

a1 = [4, 8, 15, 16, 23, 42]
def linearSearch(a1):
    for i in range(len(a1)):
        if a1[i] == 50:
            print("Found")
    print("Not found")

linearSearch(a1)    # Not found

#or

names = ["EMMA", "RODRIGO", "BRIAN", "DAVID"]

def searchNames(names):
    for i in range(len(names)):
        if names[i] == "EMMA":
            print("Found")
            return 0
    print("Not found")
    return 1

searchNames(names)  # Found

# 27 Binary search | O (log n)

list = [4, 7, 8, 12, 45, 99, 102, 702]
target = 7

# Iterative Binary Search
def binary_search(list, target):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        if target == list[mid]:
            return True
        elif target < list[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False

print(binary_search(list, target))

# 28 Recursion | Fibonacci Numbers 0, 1, 1, 2, 3, 5, 8, 13, 21, 34,..

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

print (fibo(5))      # 5

# 29 Iteration | Fibonacci Numbers 0, 1, 1, 2, 3, 5, 8, 13, 21, 34,..
def iterFibo(n):
    a,b = 0,1
    for i in range(0, n):
        a,b = b, a + b
    return a
print (iterFibo(5))   # 5

# 30 Most frequent number in array

a = [1,3,1,3,2,1]

def most_frequent(a):
    max_count = -1
    max_item = None
    count = {}

    for item in a:
        if item not in count:
            count[item] = 1
        else:
            count[item] += 1
        if count[item] > max_count:
            max_count = count[item]
            max_item = item
    return max_item

print(most_frequent(a))

# 31 Two lists are rotation from each other but in different order

a = [1,2,3,4,5,6,7]
b = [4,5,6,7,1,2,3]

def is_rotation(a,b):
    if len(a) != len(b):
        return False

    key = a[0]
    key_i = -1
    for i in range(len(b)):
        if b[i] == key:
            key_i = i
            break
    if key_i == -1:
        return False
    for i in range(len(a)):
        j = (key_i + i) % len(a)
        if a[i] != b[j]:
            return False
    return True

print(is_rotation(a, b))

# 32 How many times letters forming word "BALLOON" (B=1, A=1, L=2, O=2, N=1) appears in string S

S = 'BBAAAONXXOLL'
S2 = 'BAOOLLNNOLOLGBAX'

def solution(S):

    a1 = (S.count("B"))
    a2 = (S.count("A"))
    a3 = (S.count("L")/2)
    a4 = (S.count("O")/2)
    a5 = (S.count("N"))
    result = (int(min(a1, a2, a3, a4, a5)))
    return result

print(solution(S))  # 1
print(solution(S2)) # 2