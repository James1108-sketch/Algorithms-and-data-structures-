import csv
import time

def load_data(filename):
    with open(filename, 'r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile, delimiter='\t')
        headers = next(reader)
        headers = [header.strip() for header in headers]
        records = [tuple(row) for row in reader]

    return headers, records

def bubble_sort(records, key_index, numeric_key=False):
    n = len(records)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            left = records[j][key_index]
            right = records[j+1][key_index]

            if numeric_key:
                left = float(left)
                right = float(right)

            if left > right:
                records[j], records[j+1] = records[j+1], records[j]
                swapped = True

            if not swapped:
                break

        return records
def run_dataset(filename, primary_key, load_data, numeric_key=False):
    print("\ndataset:", filename)

    try: 
        headers, records = load_data(filename) 

        if primary_key not in headers:
            print("Primary key not found:", primary_key)
            print("Available headers:", headers)
            return

        key_index = headers.index(primary_key)

        print("records loaded:", len(records))

        start_time = time.time()

        sorted_records = bubble_sort(
            records, key_index, numeric_key
        )

        end_time = time.time()

        elapsed_time = end_time - start_time

        print("Sorting Algorithm: Bubble Sort")
        print(f"Elapsed time: {elapsed_time:.4f} seconds")

        for record in sorted_records[:5]:
            print(record)

    except FileNotFoundError:
        print("File not found:", filename)
        print("Please check the file path and try again.")
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
        "Electric_Vehicle_Population_Data(2).txt",
        "VIN(1-10)",
        load_data,
        numeric_key=False
    )

if __name__ == "__main__":
    main()