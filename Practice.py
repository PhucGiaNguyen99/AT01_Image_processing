from typing import List


def search(nums: List[int], target: int) -> int:
    low = 0
    high = len(nums) - 1
    while (low <= high):
        mid = (low + high) // 2
        # if mid == target, return mid
        if nums[mid] == target:
            return mid
        # if mid < target, do in the right half
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def searchInsert(nums: List[int], target: int) -> int:
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (high + low) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return high + 1


def sortedSquares(a: List[int]) -> List[int]:
    n = len(a)
    squared_arr = [0] * n
    highest_square_index = n - 1

    left = 0
    right = n - 1

    while (left <= right):
        left_square = a[left] * a[left]
        right_square = a[right] * a[right]
        print("left square: ", left_square)
        print("right square: ", right_square)

        if left_square > right_square:
            squared_arr[highest_square_index] = left_square
            highest_square_index = highest_square_index - 1
            left = left + 1
        else:
            squared_arr[highest_square_index] = right_square
            highest_square_index = highest_square_index - 1
            right = right - 1
    return squared_arr


def rotate_one_element(nums: List[int]) -> None:
    n = len(nums)
    temp = nums[n - 1]
    for i in range(n - 1, 0, -1):
        nums[i] = nums[i - 1]
    nums[0] = temp
    # print_list(nums)


def print_list(nums: List[int]):
    for i in range(len(nums)):
        print(nums[i])


def rotate(nums: List[int], k: int) -> None:
    for i in range(k):
        rotate_one_element(nums)


def reverseWords(s: str) -> str:
    words = s.split()
    result_str = ""
    for i in range(len(words)):
        result_str += reverse_word(words[i])
        if i!=len(words)-1:
            result_str+=" "
    return result_str


def reverse_word(word: str) -> str:
    reversed_characters_list = [*word][::-1]
    print(reversed_characters_list)
    temp = []
    for c in reversed_characters_list:
        temp.append(c)
    return "".join(temp)


# print(reverse_word("Hellow"))
print(reverseWords("Hello world!"))
