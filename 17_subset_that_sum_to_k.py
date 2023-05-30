"""
Subset that sums up to k.
By using recursion + memoization

Solution:
 - Time complexity: O(nk)
 - Space complexity: O(nk)
"""


def subsets_that_sums_up_to_k(arr, k):
    def rec(arr, k, i, sum, memo):
        key = str(i) + " " + str(sum)
        if memo.get(key) is not None:
            return memo[key]
        elif sum == k:
            return 1
        elif sum > k or i >= len(arr):
            return 0
        else:
            nb_subsets = (
                    rec(arr, k, i + 1, sum + arr[i], memo) +
                    rec(arr, k, i + 1, sum, memo)
            )
            memo[key] = nb_subsets
            return nb_subsets

    return rec(arr, k, 0, 0, {})


test_array = [1, 2, 3, 1]
k = 4
print(subsets_that_sums_up_to_k(test_array, k))
