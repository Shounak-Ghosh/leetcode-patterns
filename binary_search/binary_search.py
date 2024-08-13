def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (right + left) // 2
        # can add check for problem condition here
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    # not found, left is the insert position
    return left


def main():
    nums = [1, 3, 5, 6]
    target = 5
    print(search(nums, target))


if __name__ == '__main__':
    main()
