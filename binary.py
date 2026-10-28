import time

infile = open("data.txt", encoding="utf-8")

table = list()

for data in infile:
    table.append(tuple(data.split("\t")))

infile.close()

def locate(table,key):
    low = 0
    high = len(table) -1

    while low <= high:
        mid = (low + high) //2

        record_key = int(table[mid][0])

        if record_key == key:
            return mid

        elif record_key < key:
            low = mid +1
        else:
            high = mid -1
    return -1

for i in range(10):
    rec_num = int(input("Enter rec number: "))

    start_time = time.perf_counter()

    found = locate(table, rec_num)

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time

    if found != -1:
        print("Found at Index: ", found)
        print("Record: ", table[found])
    else:
        print("Record not found.")

    print("Elasped time: ", format(elapsed_time, ".9f"), "seconds")
    print()

print("Done")