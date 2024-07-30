Question Name  : Permutation

def generate_permutations(nums):
    def backtrack(start):
        if start == len(nums):
            permutations.append(nums[:])
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]  # Swap
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]  # Swap back (backtrack)

    permutations = []
    backtrack(0)
    return sorted(permutations)  # Sort permutations to ensure lexicographical order

def print_permutations(permutations):
    for perm in permutations:
        print(' '.join(map(str, perm)))

if __name__ == "__main__":
    n = int(input("Enter the number of elements: "))
    nums = list(map(int, input("Enter the elements separated by space: ").split()))
    perms = generate_permutations(nums)
    print_permutations(perms)

