def find_max_fit(weights, values, capacity, items):
    matrix = [[0 for _ in range(capacity + 1)] for _ in range(items + 1)]

    for i in range(1, items + 1):
        for j in range(1, capacity + 1):
            if j - weights[i - 1] < 0:
                matrix[i][j] = matrix[i - 1][j]
            else:
                matrix[i][j] = max(
                    matrix[i - 1][j], values[i - 1] + matrix[i - 1][j - weights[i - 1]])

    print("Max weight with max profit that can be selected:",
          matrix[items][capacity])

    selected_coins = []
    selected_count = 0
    i, j = items, capacity

    while i > 0 and j > 0:
        if matrix[i][j] != matrix[i - 1][j]:
            selected_coins.append(i - 1)
            j -= weights[i - 1]
            i -= 1
        else:
            i -= 1

    print("\nSelected Items no's:", end=" ")
    for k in reversed(selected_coins):
        print(k + 1, end=" ")


if __name__ == "__main__":
    items = int(input("Enter the number of items: "))

    weights = list(map(int, input("Enter the weights of the items: ").split()))
    values = list(map(int, input("Enter the values of the items: ").split()))

    capacity = int(input("Enter the capacity: "))

    find_max_fit(weights, values, capacity, items)
