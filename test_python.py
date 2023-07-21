# Problem 1 : The Largest Unique Number

numbers_input = input("PROBLEM 1. Enter numbers separated by space or comma: ")
numbers_input = numbers_input.replace(',', ' ')

numbers_list = [int(num) for num in numbers_input.split()]


def largest_unique_number(numbers):
    # repetitive numbers
    rep_num = {}

    # we calculate the repetition of each number in the list
    for num in numbers:
        rep_num[num] = rep_num.get(num, 0) +1


    # we are looking for the largest unique number in the list
    largest_uniqueNumber = -1
    for num, rep in rep_num.items():
        if rep == 1 and num > largest_uniqueNumber:
            largest_uniqueNumber = num

    return largest_uniqueNumber

result = largest_unique_number(numbers_list)
print("The largest unique number in the list is:", result)


# Problem 2: Remove Duplicat

def remove_duplicates(input_str):

  processed_list = []

  words = input_str.split()

  for word in words:

    try:
      num = int(word)
      processed_list.append(num)
    except ValueError:

      try:
        num = float(word)
        processed_list.append(num)
      except ValueError:

        processed_list.append(word)

  return processed_list


user_input = input("Problem 2. Enter elements separated by space or comma: ")
user_input = user_input.replace(',', ' ')


result_list = remove_duplicates(user_input)
doubled_list = [element * 2 for element in result_list]

# print(result_list)
print(doubled_list)

# Problem 3: Reverse Words

def reverse_words(input_str):

    words = input_str.split()

    reversed_words = words[::-1]

    reversed_str = ' '.join(reversed_words)

    return reversed_str


user_input = input("PROBLEM 3. Enter a string of words separated by spaces: ")

result_str = reverse_words(user_input)

print(f"The reversed string is: {result_str}")


# Problem 4

def find_missing_number(nums):
  N = len(nums) + 1
  sum0 = (N * (N + 1)) // 2
  sum1 = sum(nums)
  missing_number = sum1 - sum0
  return missing_number


nums_list = input("PRBLEM 4. Enter a numbers of separated by spaces: ")
nums_list = [int(num) for num in nums_list.split()]

missing_number = find_missing_number(nums_list)

print(f"The Number is: {missing_number}")


# PROBLEM 5 
string1 = input("PROBLEM 5. The first string: ")
string2 = input("PR0BLEM 5. The second string: ")

def is_anagram(str1, str2):
  
  if len(str1) != len(str2):
    return False

  lens_str1 = {}
  lens_str2 = {}

  for char in str1:
    lens_str1[char] = lens_str1.get(char, 0) + 1

  for char in str2:
    lens_str2[char] = lens_str2.get(char, 0) + 1

  return lens_str1 == lens_str2


print(is_anagram(string1, string2))


# problem 6

import re

string_input = input("PRoblem 6. Enter a palindrome: ")


def validate_palindrome(input_str):

  cleaned_str = re.sub(r'[^a-zA-Z0-9]', '', input_str)

  return cleaned_str.lower() == cleaned_str.lower()[::-1]


if validate_palindrome(string_input):
    print("True")
else:
    print("False")

    

# PROBLEM 7

number_input = int(input("Problem 7. Enter the number integer: "))


def prime_factors(number):

  prime_factors = []


  for i in range(2, number + 1):
    while number % i == 0:
      prime_factors.append(i)
      number //= i

  return prime_factors


prime_result = prime_factors(number_input)

print("List of its prime factors", prime_result)

# Problem 8

input_string = input("Problem 8. Enter the text:")


def count_words(input_str):
  word_count = {}

  words = input_str.split()

  for word in words:
    word = word.lower()
    word_count[word] = word_count.get(word, 0) + 1

  return word_count


word_count_dict = count_words(input_string)

print("Dictionary with word counts:")
for word, count in word_count_dict.items():
  print(f"{word}: {count}")


# Problem 9

import numpy as np


def matrix_transpose(matrix):
  np_matrix = np.array(matrix)

  transpose_matrix = np.transpose(np_matrix)

  return transpose_matrix


print(
    "Problem 9.Introduceți elementele matricei separate prin spații și rânduri separate"
    "prin virgule:")
matrix_input = input()

matrix_list = [list(map(int, row.split())) for row in matrix_input.split(',')]

transposed_matrix = matrix_transpose(matrix_list)

print("\nMatricea de intrare:")
for row in matrix_list:
  print(row)

print("\nMatricea transpusă:")
for row in transposed_matrix:
  print(row)

# Problem 10

list_input = input(
    "PROBLEM 10.  Introduceți elementele listei sortate separate prin spațiu: ")
list = [int(num) for num in list_input.split()]

target_num = int(input("Target: "))


def binary_search(list, target):
  left = 0
  right = len(list) - 1

  while left <= right:
    mid = left + (right - left) // 2
    mid_value = list[mid]

    if mid_value == target:
      return mid
    elif mid_value < target:
      left = mid + 1
    else:
      right = mid - 1

  return -1

index = binary_search(list, target_num)

if index != -1:
  print(f"Numărul {target_num} se află la indexul {index} în listă.")
else:
  print(f"Numărul {target_num} nu a fost găsit în listă. -1")

