from random import sample


def bubble_sort(unsorted_list):
    n = len(unsorted_list)

    for i in range(n):
        for j in range(0, n-i-1):
            if unsorted_list[j] > unsorted_list[j+1]:
                unsorted_list[j], unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[j]

    return unsorted_list


def binary_search(target, sorted_list):
    left, right = 0, len(sorted_list) - 1
    iteration_count = 0

    while left <= right:
        middle = (left + right) // 2
        print(f'left = {left}, right = {right}')

        if target == sorted_list[middle]:
            print(f"Number {target} found at index {middle}")
            break
        else:
            if target > sorted_list[middle]:
                left = middle + 1
            else:
                right = middle - 1
        iteration_count += 1

    print(f"Number of iterations: {iteration_count}")


def main():
    numbers_list = sample(range(1, 80), 50)
    print("Original list:", numbers_list)

    if not numbers_list:
        print("The list is empty.")
        return

    sorted_list = bubble_sort(numbers_list.copy())
    print("Sorted list:", sorted_list)

    target_number = int(input('Enter the number to search: '))

    binary_search(target_number, sorted_list)


if __name__ == "__main__":
    main()
