# Problem 1
def hash_string(key, table_size):
    total = 0

    for character in key:
        total += ord(character)

    return total % table_size

key = "abcd"
table_size = 10
print(hash_string(key, table_size))

# Problem 2
def hash_integer(key, table_size):
    return key % table_size

print(hash_integer(37, 21))

# Problem 3
def mid_sqaure(key, table_size):
    squared = key ** 2

    value = str(squared)

    middle = len(value) //2

    if len(value) % 2 == 0:
        middle_digits = value[middle - 1:middle + 1]
    else:
        middle_digits = value[middle]
    return int(middle_digits) % table_size

print(mid_sqaure(12,10))

# Problem 4
def polynomial_hash(key, table_size):
    hash_value = 0
    base = 31

    for charachter in key:
        hash_value = hash_value * base + ord(charachter)
    
    return hash_value % table_size

print(polynomial_hash("abcd", 10))

# Problem 5
def partition_hash(key, table_size):
    key = str(key)

    groups = []

    for i in range(0, len(key), 2):
        groups.append(int(key[i:i + 2]))

    total = sum(groups)
    return total % table_size

key = int(input("Enter a key: "))
table_size = int(input("Enter table size: "))

print("Hash Value:", partition_hash(key, table_size))