import csv
import time

def load_data(filename):
    with open(filename, 'r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile, delimiter='\t')
        headers = next(reader)
        headers = [header.strip() for header in headers]
        records = [tuple(row) for row in reader]

    return headers, records

def merge_sort(records, key_index, numeric_key=False):
    if len(records) <= 1:
        return records

    middle = len(records) // 2

    left = merge_sort(records[:middle], key_index, numeric_key)
    right = merge_sort(records[middle:], key_index, numeric_key)

    return merge(left, right, key_index, numeric_key)

def merge(left, right, key_index, numeric_key):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        left_value = left[i][key_index]
        right_value = right[j][key_index]

        if numeric_key:
            left_key = int(left_key)
            right_key = int(right_key)

        if left_key <= right_key:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1


    result.extend(left[i:])
    result.extend(right[j:])
    return result

def run_dataset(filename, primary_key, load_data, numeric_key=False):
    print("\ndataset:", filename)

    try:
        headers, records = load_data(filename)

        if primary_key not in headers:
            print("Primary key not found:", primary_key)
            print("Available headers:", headers)
            return

        key_index = headers.index(primary_key)
        print("records loaded;",len(records))

        start_time = time.time()

        sorted_records = merge_sort(records, key_index, numeric_key)

        end_time = time.time()

        print("Algorithm: Merge Sort")
        print(f"Elapsed time: {end_time - start_time:.4f} seconds")
        print("\nFirst 5 sorted records:")

        print(headers)
        for record in sorted_records[:5]:
            print(record)

    except FileNotFoundError:
        print("File not found:", filename)
    except (ValueError, IndexError) as error:
        print("Unable to sort dataset:", error)

def main():
    run_dataset(
        "Crime_Data_from_2020_to_2024(2)(1).txt",
        "DR_NO",
        load_data,
        numeric_key=True
    )

    run_dataset(
        "Electric_Vehicle_Population_Data.txt",
        "VIN(1-10)",
        load_data,
        numeric_key=False
    )
if __name__ == "__main__":
    main()
