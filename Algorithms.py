# 1 Second largest number in List [1, 3, 4, 5, 0, 2]
import pprint

given_list = [1, 3, 4, 5, 0, 2, 3, 7, 10, 9]


def second_largest(given_list):
    largest = None
    second_largest = None
    for current_number in given_list:
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


print second_largest(given_list)
print second_largest([-2, -1])
print second_largest([2, 2, 1])
print second_largest([])


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


print larger_than("2", "1")


# 3 Palindrome

# p1 = "-12"
# p2 = "1221"
# p3 = "123421"


def palindrome(string1):
    string2 = string1[::-1]
    if int(string1) < 0:
        print "{} it is negative number".format(string1)
    elif string1 == string2:
        print "{} it is a palindrome".format(string1)
    else:
        print "{} it is not a palindrome".format(string1)


#input = raw_input("Enter number: ")
#print palindrome(input)

# print palindrome(p1)
# print palindrome(p2)
# print palindrome(p3)

# 4 Sum of elements devided per 3 and 5 between 1 and 100

total = 0
for i in range(1, 101):
    if i % 3 == 0 or i % 5 == 0:
        total += i
print total

# or how many numbers
total2 = 0
for i in range(1, 101):
    if i % 3 == 0 or i % 5 == 0:
        total2 += 1
print total2

# 5 Reverse

s = "Hello world!"
s2 = 12345
s3 = [1, 2, 3, 4, 5]


def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str


print (reverse(s))
# print (reverse(s2))
# print (reverse(s3))

# 6 Print unique numbers

n1 = [1, 2, 1, 2, 3, 4, 5, 4]

set1 = set()
for i in n1:
    set1.add(i)
print set1

# 7 print unique letters

n4 = list(dict.fromkeys('aaabcabccd'))
print n4

# 8 count unique letters

n5 = 'aaabcabccd'
print n5.count('a')

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


print find_max(given_list2)

# 10 Find the overlap between two lists

list1 = [1, 2, 3, 5, 6, 9, 14]
list2 = [1, 5, 6, 15, 17, 21]

def find_overlap(list1, list2):
    for i in list1:
        if i in list2:
            print i
    pass

print find_overlap(list1, list2)

# 11 count characters in message

message = 'Hello. Try count all letters in this message.'
count = {}

for character in message.upper():
    count.setdefault(character, 0)
    count[character] += 1

pprint.pprint (count)


# 12

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
    print string1

print firstLetterCapitalized(string1)

# 14 Print longest word

words = ["alpha", "omega", "up", "down", "over", "under", "purple", "red", "blue", "green"]
sortedwords = sorted(words, key=len)
print "The longest word in the list is: %s." % (sortedwords[-1])

# 15 Index

List = [1, 2, 3]
print List.index(2)

for i in List:
    if i == 2:
        print i, "with index: ", List.index(i)

# 16 check if digit

List = ['1', '#2', '3']

for i in List:
    if i.isdigit():
        print i, 'with index:', List.index(i)
    else:
        print False

# 17 Find biggest difference between two numbers

a = [1,2,3,5]

def maxDifference(a):
    max_diff = a[1] - a[0]

    for i in range(0, len(a)):
        for j in range(i + 1, len(a)):
            if (a[j] - a[i] > max_diff):
                max_diff = a[j] - a[i]

    return max_diff


print maxDifference(a)

# 18 Print duplicates numbers

numbers = [1,2,3,2,1,5,6,5,5,5]

def countDuplicates(numbers):
    import collections
    return [item for item, count in collections.Counter(numbers).items() if count > 1]

print countDuplicates(numbers)

# 19 Delete letter, missing_char('kitten', 1) -> 'ktten'

def missing_char(str, n):
  string1 = str.replace(str[n], "")
  return string1

print missing_char("Hello", 1)

# 20 Return string when first and last chars have been exchange

str = 'Hello'

def front_back(str):
    if len(str) <= 1:
        return str

    mid = str[1:len(str)-1]
    return str[len(str)-1] + mid + str[0]

print front_back(str)