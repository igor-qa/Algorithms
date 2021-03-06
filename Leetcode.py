
#1 - #1. Two Sum

def twoSum(nums, target):
    for i in range(len(nums)):
        a = target - nums[i]
        if a in nums and i != nums.index(a):
            return i, nums.index(a)

target = 9
nums = [2, 7, 11, 15]

print (twoSum(nums, target))    # (0, 1)

#2 - #9. Palindrome Number

x = 121
x2 = -121

def isPalindrome(x):
    x2 = str(x)[::-1]
    if int(x) < 0:
        return False
    elif str(x) == x2:
        return True
    else:
        return False

print(isPalindrome(x))  # True
print(isPalindrome(x2)) # False

#3 - 14. Longest Common Prefix

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

print (longestCommonPrefix(str))

#4 - #20. Valid Parentheses

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

print (isValid(s))    # True
print (isValid(s1))   # False

#5 - #27. Remove Element

nums = [3,2,2,3]
val = 3

def removeElement(nums, val):
    for i in nums[:]:
        if i == val:
            nums.remove(i)
    return len(nums)

print(removeElement(nums, val)) # 2

#6 - #121. Best Time to Buy and Sell Stock

def maxProfit(prices):
    if len(prices) == 0:
        return 0
    else:
        low = 99999
        profitmax = 0
        for price in prices:
            if price > low:
                if price - low > profitmax:
                    profitmax = price - low
            elif price < low:
                low = price
        return profitmax

shares = [7, 1, 5, 3, 6, 4]
print (maxProfit(shares))

#7 - #217. Contains Duplicate

list1 = [1,2,3,1]
list2 = [1,2,3,4]

def containsDuplicate(nums):
    count = {}
    if len(nums) == 0:
        return False

    for number in nums:
        if number in count:
            return True
        else:
            count[number] = 1
    return False

print(containsDuplicate(list1)) # True
print(containsDuplicate(list2)) # False

#8 - #242. Valid Anagram

def isAnagram(s, t):
    count1 = {}
    count2 = {}

    for char1 in s:
        if char1 in count1:
            count1[char1] += 1
        else:
            count1[char1] = 1

    for char2 in t:
        if char2 in count2:
            count2[char2] += 1
        else:
            count2[char2] = 1

    if count1 == count2:
        return True
    else:
        return False

print (isAnagram("anagram","nagaram")) # True
print (isAnagram("anagram","nagamam")) # False

#9 - 509. Fibonacci Number

def iterFibo(n):
    a,b = 0,1
    for i in range(0, n):
        a,b = b, a + b
    return a
print (iterFibo(5))   # 5

#10 - 557. Reverse Words in a String III

Input = "Let's take LeetCode contest"
#Output: "s'teL ekat edoCteeL tsetnoc"

def reverse_words(Input):
    Input = Input.split(" ")
    reverse = []

    for word in Input:
        reverse.append(word[::-1])
    reverse = " ".join(reverse)
    return reverse

print(reverse_words(Input))

#11 - #771. Jewels and Stones

def numJewelsInStones(j, s):
    return sum(stone in j for stone in s)

print (numJewelsInStones('aAA','aAAbbbB')) # 3
print (numJewelsInStones('zas','ZZAASS')) # 0

#12 - #819. Most Common Word

def mostCommonWord(paragraph, banned):
    for c in "!?',;.":
        paragraph = paragraph.replace(c, " ")
    d, res, count = {}, "", 0
    for word in paragraph.lower().split():
        if word in banned:
            continue
        elif word in d:
            d[word] += 1
        else:
            d[word] = 1
        if d[word] > count:
            count = d[word]
            res = word
    return res

print (mostCommonWord('Hello hello are Are are', 'are')) # hello

#13 - 1108. Defanging an IP Address, Input: address = "1.1.1.1" - Output: "1[.]1[.]1[.]1"

address = "1.1.1.1"

def defanging (address):
    for i in ".":
        address = address.replace(i, "[.]")
    return address

print(defanging(address))
