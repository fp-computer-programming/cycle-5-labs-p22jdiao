# Author: JD 10/27/2021

first = input("The first word: ")

second = input("The second word: ")

if first > second:
    print(second, " comes before", first)
elif second > first:
    print(first, "comes before", second)
else:
    print("The two words are equal.")