import time

infile = open('data.txt', encoding='utf-8')

table = list()

for data in infile:
    table.append(tuple(data.split('\t')))

infile.close()

def locate(table, key):
    count = 0
    for rec in table:
        record_key = int(rec[0])
        if key == record_key:
            return count

        if record_key > key:
            return -1
        count += 1
    return -1

for i in range(10):
    rec_num = int(input("Enter Rec Num: "))
    start_time = time.time()
    found = locate(table, rec_num)
    end_time = time.time()
    elasped_time= end_time - start_time

    if found != -1:
        print("Found at Index:", found)
        print("record: ", table[found])
    else:
        print("record not found.")

    print("elsaped time:", format(elasped_time, ".9f"), "seconds")
    print()

print("Done")