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

print second_largest(given_list)
print second_largest([-2, -1])
print second_largest([2, 2, 1])

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

p1 = "-12"
p2 = "1221"
p3 = "123421"

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

palindrome(p1)
palindrome(p2)
palindrome(p3)

# 4 Sum of elements divided per 3 and 5 between 1 and 100

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

def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str

print (reverse(s))

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

print common_element(a, b)


#list1 = [1, 2, 3, 5, 6, 9, 14]
#list2 = [1, 5, 6, 15, 17, 21]

#def find_overlap(list1, list2):
#    for i in list1:
#        if i in list2:
#            print i
#    pass

#find_overlap(list1, list2)

# 11 count characters in message

message = 'Hello. Try count all letters in this message.'
count = {}

for character in message.upper():
    count.setdefault(character, 0)
    count[character] += 1

print count

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
    print string1

firstLetterCapitalized(string1)

# 14 Print longest word

words = ["alpha", "omega", "up", "down", "over", "under", "purple", "red", "blue", "green"]
sortedwords = sorted(words, key=len)
print "The longest word in the list is: %s." % (sortedwords[-1])

# 15 check if digit

List = ['1', '#2', '3']

for i in List:
    if i.isdigit():
        print i, 'with index:', List.index(i)
    else:
        print False

# 16 Find biggest difference between two numbers

a = [1,2,3,5]

def maxDifference(a):
    max_diff = a[1] - a[0]

    for i in range(0, len(a)):
        for j in range(i + 1, len(a)):
            if (a[j] - a[i] > max_diff):
                max_diff = a[j] - a[i]
    return max_diff

print maxDifference(a)

# 17 Print duplicates numbers

numbers = [1,2,3,2,1,5,6,5,5,5]

def countDuplicates(numbers):
    import collections
    return [item for item, count in collections.Counter(numbers).items() if count > 1]

print countDuplicates(numbers)

# 18 Delete letter, missing_char('kitten', 1) -> 'ktten'

def missing_char(str, n):
  string1 = str.replace(str[n], "")
  return string1

print missing_char("Hello", 1)

# 19 Return string when first and last chars have been exchange

str = 'Hello'

def front_back(str):
    if len(str) <= 1:
        return str

    mid = str[1:len(str)-1]
    return str[len(str)-1] + mid + str[0]

print front_back(str)

# + numbers

list = [1,2,3,4,5]

def changeFL(list):
    mid = list[1:len(list)-1]
    s = list[-1]
    l = list[0]
    mid.insert(0, s)
    mid.insert(len(list), l)
    print mid

print changeFL(list)

# 20 Return double_char('Hi-There') -> 'HHii--TThheerree'

def double_char(str):
    c = ''
    for i in range(len(str)):
        c += str[i] * 2
    return c

print double_char('Hi-There')

# 21 First Recurring Character

def first_reccuring(given_string):
    counts = {}
    for char in given_string:
        if char in counts:
            return char
        else:
            counts[char] = 1
    return None

print first_reccuring('DBCABA') # B

# 22 Two sum (leetcode #1)

def twoSum(nums, target):
    for i in range(len(nums)):
        a = target - nums[i]
        if a in nums and i != nums.index(a):
            return i, nums.index(a)

target = 9
nums = [2, 7, 11, 15]

print twoSum(nums, target)

# 23 Find non_repeating

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
print non_repeating(me)

# 24 Longest common prefix

str = ['one', 'onew', 'onr']

def longestCommonPrefix(str):
    if len(str) == 0:
        return ''
    res = ''
    str = sorted(str)
    for i in str[0]:
        if str[-1].startswith(res + i):
            res += i
        else:
            break
    return res

print longestCommonPrefix(str)


# 25 Return the number of times that the string "code" appears anywhere in the given string,
#  except we'll accept any letter for the 'd', so "cope" and "cooe" count.

def count_code(str):
    total = 0
    for i in range(0,len(str)-3):
        if str[i:i+2] == 'co' and str[i+3] == 'e':
            total += 1
    return total

print count_code('aaacodebbb') # 1
print count_code('codexxcode') # 2

# 26 Leetcode 121. Best Time to Buy and Sell Stock

def maxProfit(prices):
    if len(prices) == 0:
        return 0
    else:
        low = 99
        profitmax = 0
        for price in prices:
            if price > low:
                if price - low > profitmax:
                    profitmax = price - low
            elif price < low:
                low = price
        return profitmax

shares = [7, 1, 5, 3, 6, 4]
print maxProfit(shares)

# 27 Leetcode 771. Jewels and Stones Input: J = "aA", S = "aAAbbbb" Output: 3

def numJewelsInStones(j, s):
    return sum(stone in j for stone in s)

print numJewelsInStones('aAA','aAAbbbB') # 3
print numJewelsInStones('zas','ZZAASS') # 0

# 28 Leetcode 20. Valid Parentheses
s = '([]){([])}'
s1 = '([]){([])'

def isValid(s):
    bracket_map = {"(": ")", "[": "]", "{": "}"}
    open_par = set(["(", "[", "{"])
    stack = []
    for i in s:
        if i in open_par:
            stack.append(i)
        elif stack and i == bracket_map[stack[-1]]:
            stack.pop()
        else:
            return False
    return stack == []

print isValid(s)
print isValid(s1)

