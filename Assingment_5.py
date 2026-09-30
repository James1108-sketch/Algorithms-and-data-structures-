def find_sum_indices(X, target):

    def backtrack(index, current_sum, indices):
        if current_sum == target:
            return indices.copy()

        if index == len(X):
            return []

        indices.append(index)
        result = backtrack(
            index + 1,
            current_sum + X[index],
            indices
        )

        if result:
            return result

        indices.pop()

        return backtrack(
            index + 1,
            current_sum,
            indices
        )
    return backtrack(0, 0, [])

#Test 1
X = [3, 4, 7, 8]
target = 11

answer = find_sum_indices(X, target)

print("List:", X)
print("Target:", target)
print("Indices:", answer)

#Test 2
X = [2, 5, 6, 10]
target = 16

answer = find_sum_indices(X, target)

print("List:", X)
print("Target:", target)
print("Indices:", answer)

#test 3
X = [2,4,6]
target = 18

answer = find_sum_indices(X, target)

print("List:", X)
print("Target:", target)
print("Indices:", answer)